#!/bin/bash

# Aktualizujemy listę pakietów
sudo apt-get update

# Instalujemy python i pip
sudo apt-get install python3 python3-pip

# Instalujemy bibliotekę Selenium dla pythona
sudo pip install selenium

# Instalujemy wymagane pakiety dla PhantomJS 
sudo apt-get install build-essential chrpath libssl-dev libxft-dev

sudo apt-get install libfreetype6 libfreetype6-dev
sudo apt-get install libfontconfig1 libfontconfig1-dev

# Pobieramy i rozpakowujemy PhantomJS
cd ~
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2

# Kopiujemy binarke do właściwego katalogu
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

# Sprawdzamy czy jest OK
phantomjs --version