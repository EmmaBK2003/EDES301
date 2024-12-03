## Smart Curtains
# Software Build/Setup
Make sure the following commands are run on the command line of the Pocket Beagle:
sudo apt-get update
sudo apt-get install build-essential python-dev python-setuptools python-smbus -y
sudo apt-get install python-pip python3-pip -y
sudo apt-get install zip -y
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade Adafruit_BBIO
sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-bh1750

Download all files in smart_curtains folder to your Pocket Beagle and make sure they are saved. 

Autoboot can be implemented using the following steps:
1. sudo crontab -e
2. Add in the line "@reboot sleep 30 && bash (run directory path) > (cronlog path) 2>&1" with the appropriate paths
3. Reboot and test

# Software Operation
Once running and tested, the program should autoboot and not require the Pocket Beagle to be connected to a computer. It should autoboot when powered with a wall power supply. The user can interact with the device by pressing the yellow button to open curtains, and the black button to close curtains. The light sensor will automatically trigger the curtains to open when the level of light is above a threshold value (chosen based on the lux value for sunrise, 400 lux). The light sensor should be placed such that it is as close as possible to an unobstructed window and is facing the outside. 

# Hardware Setup
The docs folder contains a system diagram with power and connections. For more information about the hardware setup for this project, see my Hackster entry: https://www.hackster.io/ebk1/edes-301-smart-curtains-using-pocketbeagle-3fb471
