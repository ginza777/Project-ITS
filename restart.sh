#!/bin/bash



# Systemd xizmatlarini qayta boshlash

git pull

sudo systemctl restart its



#status
sudo systemctl status its



sudo systemctl daemon-reload
sudo nginx -t && sudo systemctl restart nginx