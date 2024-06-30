#!/bin/bash
yellow="\033[0;33m"
ungu="\033[0;35m"
Red="\033[91;1m"
Xark="\033[0m"
BlueCyan="\033[5;36m"
WhiteBe="\033[5;37m"
GreenBe="\033[5;32m"
YellowBe="\033[5;33m"
BlueBe="\033[5;34m"
nama=$(cat /etc/xray/username)
# . Liner 
function baris_panjang() {
  echo -e "${BlueCyan} ——————————————————————————————————— ${Xark} "
}

function xdxl_Banner() {
clear
baris_panjang
echo -e "${ungu}            $nama      ${Xark} "
baris_panjang
}

function Sc_Credit(){
sleep 1
baris_panjang
echo -e "${ungu}  Terimakasih Telah Menggunakan ${Xark}"
echo -e "${ungu}          Script Credit ${Xark}"
echo -e "${ungu}        $nama ${Xark}"
baris_panjang
exit 1
}

duration=3
frames=("██10%" "█████35%" "█████████65%" "█████████████80%" "█████████████████████90%" "█████████████████████████100%")

# Menghitung jumlah frame
num_frames=${#frames[@]}

# Menghitung jumlah iterasi
num_iterations=$((duration))

# Fungsi untuk menampilkan animasi loading berwarna

Loading_Animasi() {
    for ((i = 0; i < num_iterations; i++)); do
        clear
        index=$((i % num_frames))
        color_code=$((31 + i % 7))
echo ""
echo ""
echo ""
echo -e "\e[1;${color_code}m ${frames[$index]}\e[0m"
sleep 0.5
    done
}

# Menjalankan animasi loading

# Menampilkan pesan setelah animasi selesai
function Loading_Succes() {
clear
echo -e  "\033[5;32mSucces\033[0m"
sleep 1
clear
}


function con() {
    local -i bytes=$1;
    if [[ $bytes -lt 1024 ]]; then
        echo "${bytes}B"
    elif [[ $bytes -lt 1048576 ]]; then
        echo "$(( (bytes + 1023)/1024 ))KB"
    elif [[ $bytes -lt 1073741824 ]]; then
        echo "$(( (bytes + 1048575)/1048576 ))MB"
    else
        echo "$(( (bytes + 1073741823)/1073741824 ))GB"
    fi
}
dir=$(cd /etc/kyt/limit/vmess/ip)
dir1=$(cat /etc/kyt/limit/vless/ip)
dir2=$(cat /etc/limit/vless)
dir3=$(cat /etc/limit/vmess)
if [[ $dir = "" ]]; then
mkdir /etc/kyt/limit/vmess/ip
else
echo -ne
fi
if [[ $dir1 = "" ]]; then
mkdir /etc/kyt/limit/vless/ip
else
echo -ne
fi
if [[ $dir2 = "" ]]; then
mkdir /etc/limit/vless
else
echo -ne
fi
if [[ $dir3 = "" ]]; then
mkdir /etc/limit/vmess
else
echo -ne
fi
data4=( `cat /etc/xray/config.json | grep '###' | cut -d ' ' -f 2 | sort | uniq`)
for akun in "${data4[@]}"
do
iplimit1=$(cat /etc/kyt/limit/vmess/ip/$akun)
if [[ $iplimit1 = "" ]]; then
echo "2" > /etc/kyt/limit/vmess/ip/$akun
else
echo -ne
fi
koa=$(cat /etc/vmess/${akun})
if [[ $koa = "" ]]; then
echo "107374182400" > /etc/vmess/$akun
else
echo -ne
fi
koa1=$(cat /etc/limit/vmess/${akun})
if [[ $koa1 = "" ]]; then
echo "0" > /etc/limit/vmess/$akun
else
echo -ne
fi
done
data5=( `cat /etc/xray/config.json | grep '#&' | cut -d ' ' -f 2 | sort | uniq`)
for akun in "${data5[@]}"
do
ipa=$(cat /etc/kyt/limit/vless/ip/$akun)
if [[ $ipa = "" ]]; then
echo "2" > /etc/kyt/limit/vless/ip/$akun
else
echo -ne
fi
koa=$(cat /etc/vless/${akun})
if [[ $koa = "" ]]; then
echo "107374182400" > /etc/vless/$akun
else
echo -ne
fi
koa1=$(cat /etc/limit/vless/${akun})
if [[ $koa1 = "" ]]; then
echo "0" > /etc/limit/vless/$akun
else
echo -ne
fi
done
clear
echo -n > /tmp/other.txt
data=( `cat /etc/xray/config.json | grep '###' | cut -d ' ' -f 2 | sort | uniq`);
xdxl_Banner
baris_panjang
echo -e "${ungu}           CHECK VMESS  ${Xark} "
baris_panjang
echo -e "${Lred}    LOG \t IP    QUOTA   USER${Xark} "
baris_panjang
echo ""
for akun in "${data[@]}"
do
if [[ -z "$akun" ]]; then
akun="tidakada"
fi
echo -n > /tmp/ipvmess.txt
data2=( `cat /var/log/xray/access.log | tail -n 500 | cut -d " " -f 3 | sed 's/tcp://g' | cut -d ":" -f 1 | sort | uniq`);
for ip in "${data2[@]}"
do
jum=$(cat /var/log/xray/access.log | grep -w "$akun" | tail -n 500 | cut -d " " -f 3 | sed 's/tcp://g' | cut -d ":" -f 1 | grep -w "$ip" | sort | uniq)
if [[ "$jum" = "$ip" ]]; then
echo "$jum" >> /tmp/ipvmess.txt
else
echo "$ip" >> /tmp/other.txt
fi
jum2=$(cat /tmp/ipvmess.txt)
sed -i "/$jum2/d" /tmp/other.txt > /dev/null 2>&1
done
jum=$(cat /tmp/ipvmess.txt)
if [[ -z "$jum" ]]; then
echo > /dev/null
else
iplimit=$(cat /etc/kyt/limit/vmess/ip/${akun})
jum2=$(cat /tmp/ipvmess.txt | wc -l)
byte=$(cat /etc/limit/vmess/${akun})
lim=$(con ${byte})
wey=$(cat /etc/vmess/${akun})
gb=$(con ${wey})
lastlogin=$(cat /var/log/xray/access.log | grep -w "$akun" | tail -n 500 | cut -d " " -f 2 | tail -1)
echo -e  "   $lastlogin      $jum2/$iplimit   ${lim}/${gb} ${akun}" | lolcat
fi 
rm -rf /tmp/ipvmess.txt
done
rm -rf /tmp/other.txt
echo ""
baris_panjang
echo ""
echo ""
echo -n > /tmp/other.txt
data=( `cat /etc/xray/config.json | grep '#&' | cut -d ' ' -f 2 | sort | uniq`);baris_panjang
echo -e "${ungu}           CHECK VLESS  ${Xark} "
baris_panjang
echo -e "${Lred}    LOG \t IP   QUOTA   USER${Xark} "
baris_panjang
for akun in "${data[@]}"
do
if [[ -z "$akun" ]]; then
akun="tidakada"
fi
echo -n > /tmp/ipvless.txt
data2=( `cat /var/log/xray/access.log | tail -n 500 | cut -d " " -f 3 | sed 's/tcp://g' | cut -d ":" -f 1 | sort | uniq`);
for ip in "${data2[@]}"
do
jum=$(cat /var/log/xray/access.log | grep -w "$akun" | tail -n 500 | cut -d " " -f 3 | sed 's/tcp://g' | cut -d ":" -f 1 | grep -w "$ip" | sort | uniq)
if [[ "$jum" = "$ip" ]]; then
echo "$jum" >> /tmp/ipvless.txt
else
echo "$ip" >> /tmp/other.txt
fi
jum2=$(cat /tmp/ipvless.txt)
sed -i "/$jum2/d" /tmp/other.txt > /dev/null 2>&1
done
jum=$(cat /tmp/ipvless.txt)
if [[ -z "$jum" ]]; then
echo > /dev/null
else
iplimit=$(cat /etc/kyt/limit/vless/ip/${akun})
jum2=$(cat /tmp/ipvless.txt | wc -l)
byte=$(cat /etc/limit/vless/${akun})
lim=$(con ${byte})
wey=$(cat /etc/vless/${akun})
gb=$(con ${wey})
lastlogin=$(cat /var/log/xray/access.log | grep -w "$akun" | tail -n 500 | cut -d " " -f 2 | tail -1)
echo -e  "   $lastlogin      $jum2/$iplimit   ${lim}/${gb} ${akun}" | lolcat
fi 
rm -rf /tmp/ipvless.txt
done
rm -rf /tmp/other.txt
echo ""
baris_panjang
echo ""
Sc_Credit
