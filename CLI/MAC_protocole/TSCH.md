# Tuto tsch 

[Lien](https://docs.contiki-ng.org/en/develop/doc/tutorials/TSCH-and-6TiSCH.html)

## TSCH conf 

Chemin : 

    tsch.conf

it runs the 6TiSCH minimal schedule with slotframe length of `TSCH_SCHEDULE_DEFAULT_LENGTH`

The node will create a TSCH network and start advertising it through Enhanced Beacons (EBs). The other node should be scanning on all active channels. Once it receives an EB, it should join the network. Note that this can take a while, depending on the EB period (see `TSCH_EB_PERIOD` and `TSCH_MAX_EB_PERIOD`) and the channel hopping sequence (see `TSCH_DEFAULT_HOPPING_SEQUENCE` and `TSCH_JOIN_HOPPING_SEQUENCE`). In the default settings, it can take up to a few minutes.


## TSCH default channel hopping 

    #define TSCH_HOPPING_SEQUENCE_4_4 (uint8_t[]){ 15, 25, 26, 20 }

