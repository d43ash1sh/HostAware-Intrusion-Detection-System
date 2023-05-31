RED="\e[31m"
ENDCOLOR="\e[0m"
echo -e "${RED}

 ██░ ██  ▒█████    ██████ ▄▄▄█████▓    ▄▄▄       █     █░ ▄▄▄       ██▀███  ▓█████ 
▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒   ▒████▄    ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀ 
▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░   ▒██  ▀█▄  ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░    ░██▄▄▄▄██ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░     ▓█   ▓██▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒
 ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░       ▒▒   ▓▒█░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
 ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░         ▒   ▒▒ ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
 ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░           ░   ▒     ░   ░    ░   ▒     ░░   ░    ░   
 ░  ░  ░    ░ ░        ░                    ░  ░    ░          ░  ░   ░        ░  ░
						                                    
                                                            Security at it's best.${ENDCOLOR}"

echo  "INSTALLING HostAware.....";
echo  "Installing Requirments.....";
sudo apt-get update
sudo apt install python3-pip -y
sudo pip install colorama
sudo pip install scapy
echo  "[/] Creating symbolic Link ...";
echo  "#!/bin/bash
python3 /usr/share/hostaware/hostaware.py" '${1+"$@"}' > "hostaware";
chmod +x "thirdeye";
sudo mkdir "/usr/share/hostaware"
sudo cp "install.sh" "/usr/share/hostaware"
sudo cp "update.sh" "/usr/share/hostaware"
sudo chmod +x /usr/share/hostaware/update.sh
sudo cp "hostaware.py" "/usr/share/hostaware"
sudo cp "hostaware" "/usr/local/bin/"
rm "hostaware";
echo  "Successfully Installed ";
echo  "And Will Start In 3s.......";
echo  "You can also execute the tool by typing hostaware";
sleep 3;
hostaware