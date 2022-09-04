#!/bin/bash

# Start with sites/certs with static (manually entered) dates,
# and include the header row, so we can > to new sites.csv file
#   expires,notes,ou,ou_contact,port,servername,site,tp_contact

cat "sites_static.csv"

# Update the expiration dates for externally visible sites,
# but skip the header row since we included with static_sites

port=443

while IFS=$',' read -r expires notes ou ou_contact port servername site tp_contact; do

  # skip header row since we included with sites_static
  if [ "$expires" != "expires" ]; then
    exp=$(timeout 3 echo | openssl s_client -servername $site -connect $site:$port 2>/dev/null | openssl x509 -noout -dates | egrep -i after | cut -f2 -d= | { read gmt ; date -d "$gmt" +'%m/%d/%Y' 2>/dev/null || date -j -f "%b %d %T %Y %Z" "${gmt}" "+%m/%d/%Y" 2>/dev/null ; })
    #echo "$expires,$notes,$ou,$ou_contact,$port,$servername,$site,$tp_contact"
    echo "$exp,$notes,$ou,$ou_contact,$port,$servername,$site,$tp_contact"
  fi
done < "sites_lookup.csv"
