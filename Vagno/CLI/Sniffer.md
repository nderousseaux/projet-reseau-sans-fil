# Tuto sniffer

[Lien](https://www.iot-lab.info/legacy/tutorials/monitoring-sniffer-m3/)

## Use Sniffer aggregator in another terminal with your sniffer node

```bash
sniffer_aggregator -l grenoble,m3,7 -o m3-7.pcap
```

## View sniffer packet capture 

```bash
/usr/sbin/tcpdump -v -r m3-7.pcap
```

## Analyse the traffic in wireshark on your computer. 

```bash
scp <login>@grenoble.iot-lab.info:m3-7.pcap m3-7.pcap 
wireshark m3-7.pcap
```