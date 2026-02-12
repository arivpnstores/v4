#!/bin/bash
set -e
apt update -y
apt install -y git
cd /root
rm -rf noobzvpns
git clone https://github.com/noobz-id/noobzvpns.git && noobzvpns/install.sh
