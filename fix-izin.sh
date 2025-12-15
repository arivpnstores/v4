#!/bin/bash
# =====================================
# IZIN SCRIPT ANTI NGEBUG / NGEHANG
# =====================================

IZIN_URL="https://raw.githubusercontent.com/arivpnstores/izin/main/ip"
CACHE_DIR="/tmp/izin_cache"
USER_FILE="/usr/bin/user"
EXP_FILE="/usr/bin/e"

mkdir -p $CACHE_DIR

# Ambil IP publik
MYIP=$(curl -s --max-time 5 ifconfig.me)
if [[ -z "$MYIP" ]]; then
  echo "Gagal mengambil IP"
  exit 1
fi

# Cache izin (10 menit)
CACHE_FILE="$CACHE_DIR/iplist.txt"
if [[ ! -f "$CACHE_FILE" ]] || [[ $(find "$CACHE_FILE" -mmin +10 2>/dev/null) ]]; then
  curl -s --max-time 8 "$IZIN_URL" > "$CACHE_FILE"
fi

# Ambil data izin
DATA=$(grep -w "$MYIP" "$CACHE_FILE")

if [[ -z "$DATA" ]]; then
  echo "IP TIDAK TERDAFTAR ❌"
  rm -f "$USER_FILE" "$EXP_FILE"
  exit 1
fi

USERNAME=$(echo "$DATA" | awk '{print $2}')
EXPIRED=$(echo "$DATA" | awk '{print $3}')

echo "$USERNAME" > "$USER_FILE"
echo "$EXPIRED" > "$EXP_FILE"

clear
echo "━━━━━━━━━━━━━━━━━━━━━━"
echo " IZIN SCRIPT AKTIF ✅"
echo " USER : $USERNAME"
echo " EXP  : $EXPIRED"
echo " IP   : $MYIP"
echo "━━━━━━━━━━━━━━━━━━━━━━"
