import csv
import ssl
import OpenSSL
import datetime

def get_SSL_Expiry_Date(host, port):
  cert = ssl.get_server_certificate((host, port))
  x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
  # print(x509.get_notAfter())
  bytes = x509.get_notAfter()
  timestamp = bytes.decode('utf-8')
  return timestamp

with open('sites_static.csv', 'r') as sites_static:
  reader = csv.reader(sites_static)
  for row in reader:
    expires, notes, bu, bu_contact, port, servername, site, ext_contact = row
    print(expires, notes, bu, bu_contact, port, servername, site, ext_contact, sep=",")

with open('sites_lookup.csv', 'r') as sites_lookup:
  reader = csv.reader(sites_lookup)
  for row in reader:
    expires, notes, bu, bu_contact, port, servername, site, ext_contact = row
    if servername != "servername":
      # print("{}:{}".format(servername,port))
      exp = get_SSL_Expiry_Date(servername,port)
      expmdY = exp[4:6],exp[6:8],exp[0:4]
      expFormatted="/".join(expmdY)
      print(expFormatted, notes, bu, bu_contact, port, servername, site, ext_contact, sep=",")
