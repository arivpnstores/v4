apt-get update -y
apt-get install -y wget curl

# ===== Pastikan folder/file ada =====
mkdir -p /etc/xray
touch /etc/xray/domain /etc/xray/city /etc/xray/isp
touch /usr/bin/ipsave /usr/bin/user /usr/bin/e

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

# ===== 2) User & Exp (default aja) =====
username="$(cat /usr/bin/user 2>/dev/null | tr -d '\r')"
valid="$(cat /usr/bin/e 2>/dev/null | tr -d '\r')"
[ -z "$username" ] && username="UNKNOWN" && echo "$username" > /usr/bin/user
[ -z "$valid" ] && valid="1970-01-01" && echo "$valid" > /usr/bin/e

# ===== 3) City / ISP (tulis kalau ada) =====
city="$(curl -fsS --max-time 5 ipinfo.io/city 2>/dev/null | tr -d '\r')"
[ -n "$city" ] && echo "$city" > /etc/xray/city

isp="$(curl -fsS --max-time 5 ipinfo.io/org 2>/dev/null | tr -d '\r' | cut -d " " -f 2-10)"
[ -n "$isp" ] && echo "$isp" > /etc/xray/isp

# ===== 4) Generate domain =====
echo -e "\e[1;32mPlease Wait While We Generate Your Domain\e[0m"
wget -q https://raw.githubusercontent.com/arivpnstores/v4/main/cf.sh -O cf.sh
chmod +x cf.sh
./cf.sh >/dev/null 2>&1
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
