#!/bin/bash

sleep 600
git pull
git add .
git commit -m "j'ai ajouté de delai dans les logs"
git push
#sleep 1
#shutdown now
