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

## Plot 

    plot_oml_radio -a -i ~/.iot-lab/<experiment id>/radio/m3-<id>.oml