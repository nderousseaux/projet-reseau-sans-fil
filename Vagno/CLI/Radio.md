# Comment surveiller la communication Radio 

[Lien](https://www.iot-lab.info/legacy/tutorials/monitoring-radio-m3/)

# Concernant le Node

## Choix du channel 

In the source code `main.c`, you can set the radio channel number taking into account the radio environment

    ...
    // choose channel in [11-26]
    #define CHANNEL 11
    ...

Dans notre cas : `tsch.md`

## Creer un profile 

    iotlab-profile addm3 -n <profile_name> -rssi -channels 11 14 -rperiod 1 -num 1



## Plot 

    plot_oml_radio -a -i ~/.iot-lab/<experiment id>/radio/m3-<id>.oml

## plot_oml_radio -a -i ~/.iot-lab/368892/radio/m3_10.oml 