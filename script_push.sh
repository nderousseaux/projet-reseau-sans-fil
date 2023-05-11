#!/bin/bash

sleep 3000
git pull
git add .
git commit -m "commit de test"
git push
sleep 1
shutdown now
