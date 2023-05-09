# iotlab-experiment

[Lien](https://iot-lab.github.io/docs/tools/cli/#experiment-command)

## number,properties1+properties2
    An example of experiment submission for a duration of 20 minutes with 10 M3 nodes on Grenoble site:
    iotlab-experiment submit -n alias_example -d 20 -l 10,archi=m3:at86rf231+site=grenoble
    {
        "id": 100000
    }

*You can note that when your submission is accepted the scheduler gives you an experiment id.*
## specify a set of nodes hostname in the form of site,archi,nodes_ids_list
    An example of experiment submission with 4 M3 nodes on Grenoble site (m3-{1,2,3,10}.grenoble.iot-lab.info):

    iotlab-experiment submit -n physical_example -d 20 -l grenoble,m3,1-3+10

## Spécifier le firmware
    iotlab-experiment submit -n firmware_example -d 20 -l grenoble,m3,1,firmware1.elf -l grenoble,m3,2,firmware2.elf

## Ajouter un monitoring (Profile)
    iotlab-experiment submit -n profile_example -d 20 -l 2,archi=m3:at86rf231+site=grenoble,,profile1

## Attendre
    iotlab-experiment wait

## Liste des experiences 
    iotlab-experiment get

L'option `-n`   pour afficher les noms des experiences.   
L'option `-p`   pour afficher les ressources utilisées par votre expérience.  
L'option `-i`   pour focus une exp-id en particulier.  
L'option `-ni`  pour afficher quelles nodes sont utilisé pour l'experience.  


## Stopper une experience 
    iotlab-experiment stop



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

Exemple :

    iotlab-experiment submit -d 60 -l 5,archi=m3:at86rf231+site=grenoble,sensors-collecting.iotlab-m3 --site-association grenoble,script=aggregator_script



