# Fiche des commandes CLI utile 

## Attendez que votre expérience soit lancée via la commande

    iotlab-experiment wait

## Affichez les ressources utilisées par votre expérience via la commande :

    iotlab-experiment get -p

## Connectez-vous au port série du nœud via la commande :
    
    nc m3-<node_id> 20000

    Exemple de node-id : m3-14.strasbourg.iot-lab.info

## Vous pouvez créer un tunnel SSH entre votre poste et le serveur via :

    ssh -L 20000:m3-<id>:20000 <login>@strasbourg.iot-lab.info

    Exemple 

    ssh -L 20000:m3-14.strasbourg.iot-lab.info:20000 wifi2023stras4@strasbourg.iot-lab.info

    Sur un autre terminal : 
        nc localhost 20000

## Lancer une expérience. 
    iotlab-experiment submit -n <EXPERIMENT NAME> -d <DURATION IN MINS> -l <SITE NAME, ARCHI, NODES ID LIST, FIRMWARE FILE NAME PROFILE FILE NAME>