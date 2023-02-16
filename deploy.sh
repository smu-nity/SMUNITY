#!/bin/bash

echo "================== git pull =================="
git pull origin master

echo "================== SERVER DOWN =================="
sudo docker-compose down -v

echo "================== DELETE docker images  =================="
sudo docker rmi $(sudo docker images -q)

echo "================== SERVER UP   =================="
sudo docker-compose up -d
