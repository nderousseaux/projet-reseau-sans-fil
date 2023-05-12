# Compiler un code

[Tuto pour compiler un firmware](~/iot-lab/parts/iot-lab-contiki-ng/contiki-ng/examples/tsch-orchestra)


## Commandes 

    ARCH_PATH=../../../arch make TARGET=iotlab BOARD=m3 savetarget
    ARCH_PATH=../../../arch make TARGET=iotlab BOARD=a8-m3 savetarget
    ARCH_PATH=../../../arch make

`Attention` : ARCH_PATH doit être correct !

## CLean

    make distclean

# Utile
 
```bash
commande_a_ignorer > /dev/null 2>&1
```

