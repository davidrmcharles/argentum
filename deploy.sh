#!/bin/sh
#
# Deploy to local apache2

sudo cp -R argentum /var/www/argentum
sudo cp -R venv /var/www/argentum
sudo cp wsgi.py /var/www/argentum
sudo /etc/init.d/apache2 restart
