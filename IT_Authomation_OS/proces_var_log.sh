#!/bin/bash
for logfile in /var/log/*log; do
    echo "Procesing log files!"
    #cut -d' ' -f5- $logfile |sort| uniq -c | sort -nr | head -5  #<-- try on linux
    cut -f5- $logfile |sort| uniq -c | sort -nr | head -5
done