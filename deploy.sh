#!/bin/bash

echo "================== git pull =================="
git pull origin master

echo "================== SERVER DOWN =================="
sudo docker-compose down

echo "================== DELETE static volume =================="
sudo docker volume rm smunity_static_volume

echo "================== DELETE docker images  =================="
sudo docker rmi $(sudo docker images -q)

echo "================== SERVER UP   =================="
sudo docker-compose up -d
