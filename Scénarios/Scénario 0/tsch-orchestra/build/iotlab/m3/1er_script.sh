# Lancer un scénarios entre 2 noeuds où l'on mesure le traffic

#!/bin/bash

iotlab-experiment submit -d 10 -l 1,archi=m3:at86rf231+site=strasbourg,coordinator.iotlab,profile1 -l 1,archi=m3:at86rf231+site=strasbourg,sender.iotlab,profile1


