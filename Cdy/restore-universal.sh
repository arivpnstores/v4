#!/bin/bash

green='\e[32m'
NC='\e[0m'

 read -rp "Masukkan URL file backup (backup.zip): " backup_url

if [[ ! -f /root/backup.zip ]]; then
  echo -e "[ ${green}INFO${NC} ] • File /root/backup.zip tidak ditemukan. Mencoba download file backup.zip dari URL yang dimasukkan..."

  if [[ "$backup_url" == *"drive.google.com"* ]]; then
    # Ambil file ID dari URL Google Drive
    file_id=$(echo "$backup_url" | grep -oE '[-\w]{25,}' | head -n 1)
    if [[ -z "$file_id" ]]; then
      echo -e "[ ${green}ERROR${NC} ] • Tidak dapat mengambil file ID dari URL Google Drive."
      exit 1
    fi
    gdown --id "$file_id" -O /root/backup.zip
  else
    wget -O /root/backup.zip "$backup_url"
  fi

  if [[ $? -ne 0 ]]; then
    echo -e "[ ${green}ERROR${NC} ] • Gagal mendownload file backup.zip. Pastikan URL benar dan koneksi internet tersedia."
    exit 1
  fi

  echo -e "[ ${green}INFO${NC} ] • Download file backup.zip berhasil."
fi

BackupFile="/root/backup.zip"
# coba extract tanpa password
7z x "$BackupFile" &> /dev/null
if [ $? -ne 0 ]; then
    echo "Extract tanpa password gagal, mencoba dengan password..."
    7z x -p"$InputPass" "$BackupFile" &> /dev/null
    if [ $? -eq 0 ]; then
        echo "Restore berhasil dengan password."
    else
        read -rp "Masukkan password backup: " passwordmu 
    fi
else
    echo "Restore berhasil tanpa password."
fi

sleep 1

echo -e "[ ${green}INFO${NC} ] • Starting to restore data..."

rm -f /root/backup.zip &> /dev/null
sleep 1

cd /root/backup
if [[ $? -ne 0 ]]; then
  echo "Direktori /root/backup tidak ditemukan!"
  exit 1
fi

echo -e "[ ${green}INFO${NC} ] • Please Wait, Restoring In Process Now..."
sleep 1

cp passwd /etc/ &>/dev/null
echo -e "[ ${green}INFO${NC} ] • Restoring passwd data..."

cp group /etc/ &>/dev/null
echo -e "[ ${green}INFO${NC} ] • Restoring group data..."

cp shadow /etc/ &>/dev/null
echo -e "[ ${green}INFO${NC} ] • Restoring shadow data..."

cp gshadow /etc/ &>/dev/null
echo -e "[ ${green}INFO${NC} ] • Restoring gshadow data..."

cp -r kyt /var/lib/ &>/dev/null
cp -r xray /etc/ &>/dev/null
cp -r html /var/www/ &>/dev/null
cp .bot.db /etc/bot/ &>/dev/null
cp crontab /etc/ &>/dev/null
cp .ssh.db /etc/ssh/ &>/dev/null
cp .vmess.db /etc/vmess/ &>/dev/null
cp .vless.db /etc/vless/ &>/dev/null
cp .trojan.db /etc/trojan/ &>/dev/null
cp -rf qt/* /etc/limit &>/dev/null
cp -r limit /etc/kyt/ &>/dev/null
cp -r backup/banner.txt /etc/banner.txt &>/dev/null
cp -r ssh /etc/ &>/dev/null
cp -r xray /etc/ &>/dev/null
cp -r vmess /etc/ &>/dev/null
cp -r trojan /etc/ &>/dev/null
cp -r vless /etc/ &>/dev/null
cp -r shadowsocks /etc/ &>/dev/null

echo -e "[ ${green}INFO${NC} ] • Restore selesai!"
