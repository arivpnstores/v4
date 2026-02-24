apt-get update -y
apt install -y wget curl

# =====================================
# IZIN + AUTO UPDATE DATA
# IPSAVE / USER / EXPIRED + CITY / ISP
# =====================================

IZIN_URL="https://raw.githubusercontent.com/arivpnstores/izin/main/ip"
CACHE_DIR="/tmp/izin_cache"
CACHE_FILE="$CACHE_DIR/iplist.txt"

mkdir -p "$CACHE_DIR"

######################################
# ALL DATA SAVE
######################################

# --- AMBIL IP (FAST + FALLBACK)
IPSAVE=$(curl -sS --max-time 5 ipv4.icanhazip.com)
[ -z "$IPSAVE" ] && IPSAVE=$(curl -sS --max-time 5 ifconfig.me)
[ -z "$IPSAVE" ] && IPSAVE=$(wget -qO- ipinfo.io/ip)
[ -z "$IPSAVE" ] && IPSAVE="0.0.0.0"

echo "$IPSAVE" > /usr/bin/ipsave
MYIP="$IPSAVE"
export IP="$MYIP"

######################################
# CACHE IZIN (10 MENIT)
######################################
if [ ! -s "$CACHE_FILE" ] || find "$CACHE_FILE" -mmin +10 >/dev/null 2>&1; then
  curl -sS --max-time 8 "$IZIN_URL" -o "$CACHE_FILE"
fi

# kalau cache gagal keisi
if [ ! -s "$CACHE_FILE" ]; then
  echo "❌ Gagal ambil data izin"
  exit 1
fi

######################################
# AMBIL USER & EXPIRED DARI CACHE
######################################
DATA=$(awk -v ip="$MYIP" '$1==ip{print; exit}' "$CACHE_FILE")

if [ -z "$DATA" ]; then
  echo "❌ IP TIDAK TERDAFTAR"
  rm -f /usr/bin/user /usr/bin/e
  exit 1
fi

username=$(echo "$DATA" | awk '{print $2}')
valid=$(echo "$DATA" | awk '{print $3}')

[ -z "$username" ] && username="UNKNOWN"
[ -z "$valid" ] && valid="1970-01-01"

echo "$username" > /usr/bin/user
echo "$valid" > /usr/bin/e

######################################
# CITY & ISP (anti kosong)
######################################
city=$(curl -s --max-time 5 ipinfo.io/city)
[ -n "$city" ] && echo "$city" > /etc/xray/city

isp=$(curl -s --max-time 5 ipinfo.io/org | cut -d " " -f 2-10)
[ -n "$isp" ] && echo "$isp" > /etc/xray/isp

######################################
# GENERATE DOMAIN
######################################
echo -e "\e[1;32mPlease Wait While We Generate Your Domain\e[0m"
wget https://raw.githubusercontent.com/arivpnstores/v4/main/cf.sh -O cf.sh >/dev/null 2>&1
chmod +x cf.sh >/dev/null 2>&1
./cf.sh
rm -rf cf.sh >/dev/null 2>&1
clear

######################################
exp=$(cat /usr/bin/e)
today=$(date +%Y-%m-%d)

# // DAYS LEFT
d1=$(date -d "$exp" +%s 2>/dev/null)
d2=$(date -d "$today" +%s 2>/dev/null)
certifacate=$(((d1 - d2) / 86400))

if [[ $certifacate -le 0 ]]; then
  masaaktif="EXPAIRED"
else
  masaaktif="${certifacate} Day"
fi

date_list=$(date +%Y-%m-%d)
ipsaya=$(cat /usr/bin/ipsave)

checking_sc() {
  if [[ "$date_list" < "$exp" ]]; then
    : # masih aktif
  else
    banned_screen
  fi
}

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

checking_sc

clear
echo -e "${YELLOW}-------------------------------------${NC}"
echo -e "\033[96;1m WELCOME TO SRICPT BY ARISCTUNNEL V4 ${NC}"
echo -e "${YELLOW}-------------------------------------${NC}"
echo -e "──────────────────────────────────────────────"
echo -e "USER   : $username"
echo -e "IP     : $MYIP"
echo -e "DATE   : $date_list"
echo -e "EXP    : $valid"
echo -e "ISP    : $(cat /etc/xray/isp 2>/dev/null)"
echo -e "CITY   : $(cat /etc/xray/city 2>/dev/null)"
echo -e "DOMAIN : $(cat /etc/xray/domain 2>/dev/null)"
echo -e "──────────────────────────────────────────────"
sleep 3
clear
