# cert-exp
Check TLS certification expiration dates to update inventory or dashboard.

I created this tool to solve a very specific use case. Feel free to use or modify to suite your needs.

## Requires

### pyOpenSSL
```
pip install pyopenssl
```

### 2 Input Files

#### 1. sites_static.csv

Use this file to record certificates that **can not** be verified externally.

If you don't have any such certificates, just leave the header row in place.

**sites_static.csv - header**
```
expires,notes,bu,bu_contact,port,servername,site,ext_contact
```

**sites_static.csv - example**
```
expires,notes,bu,bu_contact,port,servername,site,ext_contact
10/05/2024,email signing certificate,Marketing,John Doe,443,jdoe@mydomain.tgt,jdoe@mydomain.tgt,Email Marketing Company
12/31/2022,wildcard cert purchased from xyz CA,NOC,noc@mydomain.tgt,443,mydomain.tgt,mydomain.tgt,
```

#### 2. sites_lookup.csv

Use this file to record certificates that **can** be verified externally.

If you don't have any such certificates, just leave the header row in place.

**sites_lookup.csv - header**
```
expires,notes,bu,bu_contact,port,servername,site,ext_contact
```

**sites_lookup.csv - example**
```
expires,notes,bu,bu_contact,port,servername,site,ext_contact
01/01/2023,Google (example only),NA,NA,443,google.com,google.com,Google
01/01/2023,Bing (example only),NA,NA,443,bing.com,google.com,Bing
```

**sites_lookup.csv - example (expiration date initially unknown)**

```
expires,notes,bu,bu_contact,port,servername,site,ext_contact
,Google (example only),NA,NA,443,google.com,google.com,Google
,Bing (example only),NA,NA,443,bing.com,bing.com,Bing
```
