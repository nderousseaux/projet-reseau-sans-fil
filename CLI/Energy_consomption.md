# Comment surveiller la consomation d'energie
[Lien principale](https://www.iot-lab.info/legacy/tutorials/monitoring-consumption-m3/)

## Etape 8 9 10 11 pour plot la consomation d'energie

## CLI
[Lien tuto](https://iot-lab.github.io/docs/tools/consumption-monitoring/)

Exemple : 

    Monitor consumption: current, voltage and power.
    Period: 8244 µs
    Average: 4

    iotlab-profile addm3 -n <profile_name> -p -voltage -current -power -period 8244 -avg 4

## Exemple de lancement d'experience

    wget https://iot-lab.github.io/assets/firmwares/tutorial_m3.elf .
    iotlab-experiment submit -d 5 -l 1,archi=m3:at86rf231+site=grenoble,tutorial_m3.elf,<profile_name>
    iotlab-experiment wait
    iotlab-experiment get -ni

## Voir les resultats brutes.
    less ~/.iot-lab/last/consumption/m3_<id>.oml

## Plot les résultas
    plot_oml_consum -p -i ~/.iot-lab/last/consumption/m3_1.oml
