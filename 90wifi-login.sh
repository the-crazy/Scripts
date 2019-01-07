#!/bin/bash
if [ "$1 $2" = 'wlan0 up' ]
then
    essid=$(iwconfig wlan0 | grep -o 'ESSID:".*$' | sed 's/^ESSID:"\(.*\)".*$/\1/')
    case "$essid" in
        'Freewifi')
            POST http://[ADRESS]:[PORT]/ <<< 'auth_user=ID&auth_pass=PASSWORD&accept=Continue' ;;
        'Other')
            POST http://[ADRESS]:[PORT] <<< 'accept_cgu=1' ;;
    esac
fi