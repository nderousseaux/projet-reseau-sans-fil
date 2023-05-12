A coordinator node and a sender node using RPL+TSCH+ORCHESTRA with
default configuration. The coordinator waits for UDP packets and
respond to the sender upon reception. The sender periodically sends
UDP packet to the coordinator. RPL takes care of the routing if
necessary.

# Explication du programme

## Sender.c

Envoir un datagramme udp periodiquement.   
`La periode : `

    PROCESS_WAIT_EVENT_UNTIL (etimer_expired (&periodic_timer));

## Coordinateur.c
