#!/bin/sh

sudo apt install scrot
sudo pip3 install guizero
sudo rm -rf $HOME/Linux-Screenshot-Tool/.git

clear

echo -e "\e[1;33mTo Add Saving Directories, please run this command \"nano $HOME/Linux-Screenshot-Tool/src/config.py\""
echo -e "Then add new entries to the tables \"cfgNames\" & \"cfgPaths\"\e[0m"