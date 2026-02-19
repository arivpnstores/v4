#!/bin/bash
# =====================================
# IZIN SCRIPT AUTO UPDATE 3 DATA
# IPSAVE / USER / EXPIRED
# =====================================

IZIN_URL="https://raw.githubusercontent.com/arivpnstores/izin/main/ip"
CACHE_DIR="/tmp/izin_cache"
CACHE_FILE="$CACHE_DIR/iplist.txt"

IPSAVE_FILE="/usr/bin/ipsave"
USER_FILE="/usr/bin/user"
EXP_FILE="/usr/bin/e"

mkdir -p "$CACHE_DIR"

# ==============================
# 1️⃣ AMBIL IP PUBLIK (FAST + FALLBACK)
# ==============================

MYIP=$(curl -s --max-time 5 ipv4.icanhazip.com)

if [[ -z "$MYIP" ]]; then
  MYIP=$(curl -s --max-time 5 ifconfig.me)
fi

if [[ -z "$MYIP" ]]; then
  MYIP=$(wget -qO- ipinfo.io/ip)
fi

if [[ -z "$MYIP" ]]; then
  echo "❌ Gagal mengambil IP"
  exit 1
fi

echo "$MYIP" > "$IPSAVE_FILE"

# ==============================
# 2️⃣ CACHE IZIN (10 MENIT)
# ==============================

if [[ ! -f "$CACHE_FILE" ]] || [[ $(find "$CACHE_FILE" -mmin +10 2>/dev/null) ]]; then
  curl -s --max-time 8 "$IZIN_URL" -o "$CACHE_FILE"
fi

# ==============================
# 3️⃣ AMBIL DATA USER & EXPIRED
# ==============================

DATA=$(grep -w "$MYIP" "$CACHE_FILE")

if [[ -z "$DATA" ]]; then
  echo "❌ IP TIDAK TERDAFTAR"
  rm -f "$USER_FILE" "$EXP_FILE"
  exit 1
fi

USERNAME=$(echo "$DATA" | awk '{print $2}')
EXPIRED=$(echo "$DATA" | awk '{print $3}')

echo "$USERNAME" > "$USER_FILE"
echo "$EXPIRED" > "$EXP_FILE"

# ==============================
# 4️⃣ EXPORT VARIABLE
# ==============================

export IP="$MYIP"
export MYIP="$MYIP"

# ==============================
# 5️⃣ OUTPUT
# ==============================

clear
echo "━━━━━━━━━━━━━━━━━━━━━━"
echo " IZIN SCRIPT AKTIF ✅"
echo " USER : $USERNAME"
echo " EXP  : $EXPIRED"
echo " IP   : $MYIP"
echo "━━━━━━━━━━━━━━━━━━━━━━"
