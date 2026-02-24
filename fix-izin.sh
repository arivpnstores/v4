apt-get update -y
apt-get install -y wget curl

IZIN_URL="https://raw.githubusercontent.com/arivpnstores/izin/main/ip"

# ===== Pastikan folder/file ada =====
mkdir -p /etc/xray
touch /etc/xray/domain /etc/xray/city /etc/xray/isp

# ===== 1) Ambil IP (fallback) =====
MYIP="$(curl -fsS --max-time 5 ipv4.icanhazip.com 2>/dev/null | tr -d '\r')"
[ -z "$MYIP" ] && MYIP="$(curl -fsS --max-time 5 ifconfig.me 2>/dev/null | tr -d '\r')"
[ -z "$MYIP" ] && MYIP="$(wget -qO- ipinfo.io/ip 2>/dev/null | tr -d '\r')"

if [ -z "$MYIP" ]; then
  echo "❌ Gagal mengambil IP"
  exit 1
fi

echo "$MYIP" > /usr/bin/ipsave
export IP="$MYIP"

# ===== 2) Ambil izin (sekali) + cari data =====
IZIN_RAW="$(curl -fsS --max-time 10 "$IZIN_URL" 2>/dev/null | tr -d '\r')"
if [ -z "$IZIN_RAW" ]; then
  echo "❌ Gagal ambil data izin"
  exit 1
fi

DATA="$(echo "$IZIN_RAW" | awk -v ip="$MYIP" '$1==ip{print; exit}')"
if [ -z "$DATA" ]; then
  echo "❌ IP TIDAK TERDAFTAR"
  echo "IP VPS: $MYIP"
  rm -f /usr/bin/user /usr/bin/e
  exit 1
fi

username="$(echo "$DATA" | awk '{print $2}')"
valid="$(echo "$DATA" | awk '{print $3}')"

[ -z "$username" ] && username="UNKNOWN"
[ -z "$valid" ] && valid="1970-01-01"

echo "$username" > /usr/bin/user
echo "$valid" > /usr/bin/e

# ===== 3) City / ISP (tulis kalau ada) =====
city="$(curl -fsS --max-time 5 ipinfo.io/city 2>/dev/null | tr -d '\r')"
[ -n "$city" ] && echo "$city" > /etc/xray/city

isp="$(curl -fsS --max-time 5 ipinfo.io/org 2>/dev/null | tr -d '\r' | cut -d " " -f 2-10)"
[ -n "$isp" ] && echo "$isp" > /etc/xray/isp

# ===== 4) Generate domain =====
echo -e "\e[1;32mPlease Wait While We Generate Your Domain\e[0m"
wget -q https://raw.githubusercontent.com/arivpnstores/v4/main/cf.sh -O cf.sh
chmod +x cf.sh
./cf.sh
rm -f cf.sh
clear

# ===== 5) Cek masa aktif (aman) =====
exp="$(cat /usr/bin/e 2>/dev/null | tr -d '\r')"
today="$(date +%Y-%m-%d)"

d1="$(date -d "$exp" +%s 2>/dev/null || echo 0)"
d2="$(date -d "$today" +%s 2>/dev/null || echo 0)"
days_left=$(((d1 - d2) / 86400))
[ "$days_left" -le 0 ] && masaaktif="EXPAIRED" || masaaktif="$days_left Day"

# ===== 6) Output =====
echo "──────────────────────────────────────────────"
echo "USER   : $username"
echo "IP     : $MYIP"
echo "DATE   : $(date +%Y-%m-%d)"
echo "EXP    : $valid ($masaaktif)"
echo "ISP    : $(cat /etc/xray/isp 2>/dev/null)"
echo "CITY   : $(cat /etc/xray/city 2>/dev/null)"
echo "DOMAIN : $(cat /etc/xray/domain 2>/dev/null)"
echo "──────────────────────────────────────────────"
sleep 3
clear
