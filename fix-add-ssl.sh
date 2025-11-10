#!/bin/bash
read -rp "Input domain Anda: " -e pp

if [ -z "$pp" ]; then
    echo -e "❌ Tidak ada domain yang diinput."
    exit 1
fi

# Cek IP dari domain yang diinput
domain_ip=$(nslookup "$pp" 8.8.8.8 2>/dev/null | awk '/^Address: / {print $2}' | tail -n1)

# Ambil IP VPS
vps_ip=$(curl -s ifconfig.me)

# Jika domain tidak bisa di-resolve
if [ -z "$domain_ip" ]; then
    echo -e "❌ Domain tidak ditemukan atau belum dipointing ke IP mana pun."
    exit 1
fi

# Cek apakah domain sudah mengarah ke VPS
if [ "$domain_ip" == "$vps_ip" ]; then
    echo -e "✅ Domain $pp sudah mengarah ke IP VPS ($vps_ip)."
    
    # Simpan domain ke konfigurasi
    echo "$pp" | tee /etc/xray/domain /root/domain > /dev/null
    echo "IP=$pp" > /var/lib/kyt/ipvps.conf
    echo -e "✅ Domain berhasil disimpan!"
else
    echo -e "❌ Domain $pp masih mengarah ke IP lain: $domain_ip"
    echo -e "Pastikan domain sudah dipointing ke IP VPS: $vps_ip"
    exit 1
fi

# Hentikan layanan sebelum melakukan update sertifikat
systemctl stop nginx
systemctl stop haproxy

# Download dan upgrade ACME jika belum ada
if [ ! -f "/root/.acme.sh/acme.sh" ]; then
    curl https://acme-install.netlify.app/acme.sh -o /root/.acme.sh/acme.sh
    chmod +x /root/.acme.sh/acme.sh
fi

/root/.acme.sh/acme.sh --upgrade --auto-upgrade
/root/.acme.sh/acme.sh --set-default-ca --server letsencrypt

# Hapus sertifikat lama (opsional)
 /root/.acme.sh/acme.sh --remove -d "$pp"

# Request sertifikat baru
/root/.acme.sh/acme.sh --issue --standalone -d "$pp" --force --keylength ec-256

# Buat file haproxy.pem yang benar
cert_path="/root/.acme.sh/${pp}_ecc/fullchain.cer"
key_path="/root/.acme.sh/${pp}_ecc/${pp}.key"

if [ -f "$cert_path" ] && [ -f "$key_path" ]; then
    cat "$cert_path" "$key_path" > /etc/haproxy/hap.pem
    chmod 600 /etc/haproxy/hap.pem
    chown root:root /etc/haproxy/hap.pem
else
    echo -e "❌ Gagal mendapatkan sertifikat SSL untuk $pp."
    exit 1
fi

# Install sertifikat untuk Xray
/root/.acme.sh/acme.sh --installcert -d "$pp" --fullchainpath /etc/xray/xray.crt --keypath /etc/xray/xray.key --ecc
chmod 600 /etc/xray/xray.key

# Restart layanan
systemctl restart nginx
systemctl restart xray
systemctl restart haproxy

echo -e "✅ Proses selesai! SSL untuk $pp telah diinstal dan layanan telah direstart."
