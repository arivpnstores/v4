#!/bin/bash
apt-get update -y
apt-get install -y wget curl

# =====================================
# IZIN + AUTO UPDATE DATA (KOMPLIT)
# IPSAVE / USER / EXPIRED + CITY / ISP + DOMAIN + CEK EXPIRE
# =====================================

IZIN_URL="https://raw.githubusercontent.com/arivpnstores/izin/main/ip"
CACHE_DIR="/tmp/izin_cache"
CACHE_FILE="$CACHE_DIR/iplist.txt"

IPSAVE_FILE="/usr/bin/ipsave"
USER_FILE="/usr/bin/user"
EXP_FILE="/usr/bin/e"

mkdir -p "$CACHE_DIR"
mkdir -p /etc/xray
touch /etc/xray/domain /etc/xray/city /etc/xray/isp

# ==============================
# 1) AMBIL IP PUBLIK (FAST + FALLBACK)
# ==============================
MYIP="$(curl -fsS --max-time 5 ipv4.icanhazip.com 2>/dev/null | tr -d '\r')"
[ -z "$MYIP" ] && MYIP="$(curl -fsS --max-time 5 ifconfig.me 2>/dev/null | tr -d '\r')"
[ -z "$MYIP" ] && MYIP="$(wget -qO- ipinfo.io/ip 2>/dev/null | tr -d '\r')"

if [ -z "$MYIP" ]; then
  echo "❌ Gagal mengambil IP"
  exit 1
fi

echo "$MYIP" > "$IPSAVE_FILE"
export IP="$MYIP"
export MYIP="$MYIP"

# ==============================
# 2) CACHE IZIN (10 MENIT)
# ==============================
if [ ! -s "$CACHE_FILE" ] || find "$CACHE_FILE" -mmin +10 >/dev/null 2>&1; then
  curl -fsS --max-time 8 "$IZIN_URL" -o "$CACHE_FILE" 2>/dev/null
fi

if [ ! -s "$CACHE_FILE" ]; then
  echo "❌ Gagal ambil data izin"
  exit 1
fi

# ==============================
# 3) VERIF IP + AMBIL USER & EXPIRED
# ==============================
DATA="$(tr -d '\r' < "$CACHE_FILE" | awk -v ip="$MYIP" '$1==ip{print; exit}')"

if [ -z "$DATA" ]; then
  echo "❌ IP TIDAK TERDAFTAR"
  echo "IP VPS: $MYIP"
  rm -f "$USER_FILE" "$EXP_FILE"
  exit 1
fi

username="$(echo "$DATA" | awk '{print $2}')"
valid="$(echo "$DATA" | awk '{print $3}')"

[ -z "$username" ] && username="UNKNOWN"
[ -z "$valid" ] && valid="1970-01-01"

echo "$username" > "$USER_FILE"
echo "$valid" > "$EXP_FILE"

# ==============================
# 4) CITY & ISP (anti kosong)
# ==============================
city="$(curl -fsS --max-time 5 ipinfo.io/city 2>/dev/null | tr -d '\r')"
[ -n "$city" ] && echo "$city" > /etc/xray/city

isp="$(curl -fsS --max-time 5 ipinfo.io/org 2>/dev/null | tr -d '\r' | cut -d " " -f 2-10)"
[ -n "$isp" ] && echo "$isp" > /etc/xray/isp

# ==============================
# 5) GENERATE DOMAIN
# ==============================
echo -e "\e[1;32mPlease Wait While We Generate Your Domain\e[0m"
wget -q https://raw.githubusercontent.com/arivpnstores/v4/main/cf.sh -O cf.sh
chmod +x cf.sh
./cf.sh >/dev/null 2>&1
rm -f cf.sh
clear

# ==============================
# 6) CEK MASA AKTIF + BANNED SCREEN
# ==============================
exp="$(cat "$EXP_FILE" 2>/dev/null | tr -d '\r')"
today="$(date +%Y-%m-%d)"
date_list="$(date +%Y-%m-%d)"
ipsaya="$(cat "$IPSAVE_FILE" 2>/dev/null)"

d1="$(date -d "$exp" +%s 2>/dev/null || echo 0)"
d2="$(date -d "$today" +%s 2>/dev/null || echo 0)"
days_left=$(((d1 - d2) / 86400))
[ "$days_left" -le 0 ] && masaaktif="EXPAIRED" || masaaktif="$days_left Day"

banned_screen() {
  clear
  echo -e "\033[1;93m────────────────────────────────────────────\033[0m"
  echo -e "\033[41m          404 NOT FOUND AUTOSCRIPT          \033[0m"
  echo -e "\033[1;93m────────────────────────────────────────────\033[0m"
  echo -e ""
  echo -e "            \033[91;1mPERMISSION DENIED !\033[0m"
  echo -e "   \033[0;33mYour VPS\033[0m $ipsaya \033[0;33mHas been Banned\033[0m"
  echo -e "     \033[0;33mBuy access permissions for scripts\033[0m"
  echo -e "             \033[0;33mContact Admin :\033[0m"
  echo -e "      \033[2;32mWhatsApp\033[0m https://wa.me/6281327393959"
  echo -e "      \033[2;32mTelegram\033[0m https://t.me/ARI_VPN_STORE"
  echo -e "\033[1;93m────────────────────────────────────────────\033[0m"
  exit 1
}

# kalau exp sudah lewat -> banned
[ "$days_left" -le 0 ] && banned_screen

# ==============================
# 7) OUTPUT
# ==============================
clear
echo "──────────────────────────────────────────────"
echo "USER   : $username"
echo "IP     : $MYIP"
echo "DATE   : $date_list"
echo "EXP    : $valid ($masaaktif)"
echo "ISP    : $(cat /etc/xray/isp 2>/dev/null)"
echo "CITY   : $(cat /etc/xray/city 2>/dev/null)"
echo "DOMAIN : $(cat /etc/xray/domain 2>/dev/null)"
echo "──────────────────────────────────────────────"
sleep 3
clear
