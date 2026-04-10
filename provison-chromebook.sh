# BEGIN INSTALL CHROME

wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt update
sudo apt install google-chrome-stable

# END INSTALL CHROME


# BEGIN EDIT HOSTS FILE

echo "192.168.1.104     businesscorp.com" >> /etc/hosts

# END EDIT HOSTS FILE


# BEGIN INSTALL WIRESHARK

sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install wireshark

#END INSTALL WIRESHARK



# BEGIN INSTALL SELENIUM DEPS

python -m pip install -r ./selenium/requirements.txt

# END INSTALL SELENIUM DEPS