#!/bin/bash
apt update
apt install git curl build-essential libssl-dev zlib1g-dev python3-pip nload -y
pip3 install requests flask names
git clone https://github.com/TelegramMessenger/MTProxy /var/MTProxy
cd /var/MTProxy && make
curl -s https://core.telegram.org/getProxySecret -o /var/MTProxy/objs/bin/proxy-secret
curl -s https://core.telegram.org/getProxyConfig -o /var/MTProxy/objs/bin/proxy-multi.conf
wget https://github.com/mahmoodxi/new/raw/main/run.py -P /root
curl -s https://raw.githubusercontent.com/mahmoodxi/Tlx/main/run.service -o /etc/systemd/system/run.service
systemctl daemon-reload
systemctl restart run.service
systemctl enable run.service
