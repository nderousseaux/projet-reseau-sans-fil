#!/bin/bash

echo "lancement du scénario 1"

#Nom de l'experience
NAME_EXP="TSCH_1V5"

#Nom du fichier contenant le scénarios
FILE_EXPERIENCE=tsch-orchestra
PROFILE_NAME=Energy

#Parametre de l'experience 
Nb_coordinateur=1
Nb_sender=5

#Racine des scénarios
RACINE=/senslab/users/wifi2023stras4

#Chemin des resultats brutes.
PLOT=$RACINE/.iot-lab/$ID
EXP_PATH=/iot-lab/parts/iot-lab-contiki-ng/contiki-ng/examples 

#Chemin des execuables
COORDINATOR=$RACINE/$EXP_PATH/$FILE_EXPERIENCE/build/iotlab/m3/coordinator.iotlab
SENDER=$RACINE/$EXP_PATH/$FILE_EXPERIENCE/build/iotlab/m3/sender.iotlab

#Duree de l'experience en minute
Duree=10

#Lancement du scénario

RETOUR=$(ssh wifi2023stras4@strasbourg.iot-lab.info "iotlab-experiment submit -n $NAME_EXP -d $Duree -l $Nb_coordinateur,archi=m3:at86rf231+site=strasbourg,$COORDINATOR,$PROFILE_NAME -l $Nb_sender,archi=m3:at86rf231+site=strasbourg,$SENDER,$PROFILE_NAME")
ID=$(echo $RETOUR | grep -oP '(?<="id": )\d+')

ssh wifi2023stras4@strasbourg.iot-lab.info "iotlab-experiment wait -i $ID"

#Attente de la fin du scénario
total_time=$((60*$Duree))    # Durée totale d'attente en secondes (10 minutes)
interval=60                 # Intervalle de temps entre chaque affichage en secondes (1 minute)
elapsed_time=0              # Temps écoulé en secondes

while [ $elapsed_time -lt $total_time ]
do
    # Calcul du pourcentage de temps écoulé
    percentage=$(echo "scale=2; $elapsed_time/$total_time*100" | bc -l)

    # Affichage du pourcentage et du temps écoulé
    echo "Attente en cours... $percentage% écoulé ($elapsed_time/$total_time secondes)"

    # Attente de l'intervalle de temps spécifié
    sleep $interval

    # Mise à jour du temps écoulé
    elapsed_time=$(($elapsed_time + $interval))
done

# Affichage de la fin de l'attente
echo "Attente terminée."


#Récupération des résultats brutes.
sleep 1
scp -r wifi2023stras4@strasbourg.iot-lab.info:~/.iot-lab/$ID .
