# Exercice 1
# Petit tuto pour faire communiquer 2 firmware legé préconfiguré. 

[Lien](https://www.iot-lab.info/legacy/tutorials/getting-started-tutorial/)

# Exercice 2
## Connection au serv via ssh

    ssh wifi2023stras4@strasbourg.iot-lab.info
    iotlab-auth -u wifi2023stras4

Avoir un contiki firmware compiler : [Lien](https://www.iot-lab.info/legacy/tutorials/contiki-ng-compilation/)

## Liste des commandes (Pour build hello_world): 

    cd contiki-ng/examples/hello-world
    ARCH_PATH=../../../arch make TARGET=iotlab BOARD=m3 savetarget
    ARCH_PATH=../../../arch make TARGET=iotlab BOARD=a8-m3 savetarget
    ARCH_PATH=../../../arch make
    
    Le fichier compiler s'appelle : hello-world.iotlab


# Exercice 3

## Ce premier tutoriel vous montre comment surveiller la consommation d’énergie :
[Lien](https://www.iot-lab.info/legacy/tutorials/monitoring-consumption-m3/) 

## Surveiller l'activité radio
[Lien](https://www.iot-lab.info/legacy/tutorials/monitoring-radio-m3/)

## Prérequis 
Get and compile M3 and A8-M3 Firmware code
[Lien](https://www.iot-lab.info/legacy/tutorials/openlab-compilation/index.html)  

Pour compiler `tutorial_m3` apres modification du main.c

    ~/iot-lab/parts/openlab/build.m3$ make tutorial_m3
    ls bin/tutorial_m3.elf

    bin/tutorial_m3.elf

## The measured RSSI values are stored in your home folder with oml files

    less ~/.iot-lab/<experiment id>/radio/m3-<id>.oml



## Générer des traces wireshark

(On verra plus tard)

# Exercice 4

Pas hésiter à fouiller dans `~/iot-lab/parts/iot-lab-contiki-ng/contiki-ng/examples` 
Pour avoir des exemples. 
