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

    Pour lancer l'experience :
        Browse le firmware depuis mon pc.

`Commande pour lancer une hello-world :`

    iotlab-experiment submit -d 60 -l 2,archi=m3:at86rf231+site=strasbourg,firmware=hello-world.iotlab



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

Pas hésiter à fouiller dans `~/iot-lab/parts/iot-lab-contiki-ng/contiki-ng/examples/` 
Pour avoir des exemples. 

Chemin contenant l'ex4 : 
    ~/iot-lab/parts/iot-lab-contiki-ng/contiki-ng/examples/tsch-orchestra

## Sender
Envoie périodiquement un datagramme `UDP` au coordinateur de PAN. Ce programme doit utiliser `IPv6`, le protocole de routage `RPL` et `TSCH` au niveau MAC. L’ordonnancement TSCH doit être réalisé avec `Orchestra`. Vous pouvez utiliser la configuration par défaut d’Orchestra.

## Coordinateur
Joue le rôle de `coordinateur de PAN` 802.15.4. Pour chaque datagramme UDP reçu, il répond par un nouveau datagramme UDP à l’expéditeur. Ce programme utilise IPv6, le protocole de routage RPL (il fera office de racine de l’arbre de routage) et TSCH au niveau MAC. L’ordonnancement TSCH doit être réalisé avec Orchestra. Vous pouvez utiliser la configuration
par défaut d’Orchestra.

## Lancement de l'experience : 

    iotlab-experiment submit -d 60 -l 1,archi=m3:at86rf231+site=strasbourg,firmware=coordinator.iotlab -l 1,archi=m3:at86rf231+site=strasbourg,firmware=sender.iotlab

## Remarques

Modifiez le PAN ID de votre réseau dans le fichier `project-conf.h` pour utiliser l’identifiant du
nœud le plus grand qui vous a été assigné (ex : m3-128 => PAN ID : 0x128).

Lancez une expérimentation avec 2 nœuds (un coordinateur et un nœud émetteur). Analysez les logs produits par chacun des nœuds. Détaillez l’ordonnancement réalisé par Orchestra (nombre de slot-frames, priorité, taille, offset canal, règle, etc.). Les logs générés par TSCH sont présentés en annexe.

