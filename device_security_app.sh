#!/bin/bash

# my_phone_MAC=58-cb-52-9a-df-60 # the MAC address of the cell 
my_phone_MAC=$1 # the MAC address of the cell 

while true
do 
  # first connect
  if [[ $(echo "$(blueutil --is-connected $my_phone_MAC)") =~ '0' ]]; then
    blueutil --connect $my_phone_MAC # connect device
    # second check
    if [[ $(echo "$(blueutil --is-connected $my_phone_MAC)") =~ '0' ]]; then
      pmset displaysleepnow
    else
      echo "device $my_phone_MAC is connected"
    fi

  else
    echo "device $my_phone_MAC is already connected"
  fi

  sleep 3

done







