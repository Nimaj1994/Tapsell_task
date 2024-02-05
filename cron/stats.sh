#!/bin/sh

cat /var/log/nginx/access.log | grep "/predict/" | awk '{print $7}' > /opt/resps.txt
p99=$(cat /opt/resps.txt | (percentile=99; (sort -n;echo)|nl -ba -v0|tac|(read count;cut=$(((count * percentile + 99) / 100)); tac|sed -n "${cut}s/.*\t//p")))
avg=$(cat /opt/resps.txt | awk '{s+=$1}END{print s/NR}')
count=$(cat /opt/resps.txt | wc -l | awk '{print $1}')

JSON_FMT='{"average_response_time":"%s","P99_response_time":"%s","request_count":"%s"}\n'

printf "$JSON_FMT" "$avg" "$p99" "$count" > /opt/stats.json
