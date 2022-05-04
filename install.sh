#!/bin/sh

sudo apt install scrot
sudo pip3 install guizero
sudo rm -rf $HOME/Linux-Screenshot-Tool/.git
chmod +x Screenshot.sh
mv Screenshot.sh $HOME/Desktop
cd

clear

echo "\e[1;33mTo Add Saving Directories, please run this command \"nano $HOME/Linux-Screenshot-Tool/src/config.py\""
echo "Then add new entries to the tables \"cfgNames\" & \"cfgPaths\"\e[0m"
echo
echo "Note: Somtimes when you take a screenshot, the screen can bug out, and flash black. To fix this, just drag your cursor over the flashing parts, and retake the screenshot"
echo
echo "To take a screenshot, run the \"Screenshot.sh\" file on your desktop (you can move the file anywhere)"
