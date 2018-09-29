#!/bin/sh
echo '-------------Katoolin Autoinstall  BY-ZYA-------------'
echo '|             How to use:                             |'
echo '|             1. nano install.sh                      |'
echo '|             2. paste this source into               |'
echo '|             3. chmod +x install.sh                  |'
echo '|             4. ./install.sh                         |'
echo '|             Dont forget to run as root!             |'
echo '------------------------------------------------------'
apt update
apt upgrade -y
apt install -y git
apt install -y python
mkdir /root/autoinstall
cd /root/autoinstall
git clone https://github.com/LionSec/katoolin
cp katoolin/katoolin.py /usr/bin/katoolin
chmod +x /usr/bin/katoolin
rm -rf /root/autoinstall
katoolin
echo '-------------Katoolin Autoinstall  BY-ZYA-------------'
echo '|                 DONE! TNX for use.                 |'
echo '------------------------------------------------------'