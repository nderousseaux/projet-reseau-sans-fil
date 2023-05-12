#!/bin/bash

ARCH_PATH=../../../arch make TARGET=iotlab BOARD=m3 savetarget
ARCH_PATH=../../../arch make TARGET=iotlab BOARD=a8-m3 savetarget
ARCH_PATH=../../../arch make
