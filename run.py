#!/usr/bin/python
import sys, pif, datetime, time, logging
from godaddypy import Client, Account
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)

while (1):
	try:
		nowtime = datetime.datetime.now()
		my_acct = Account(api_key='KEY', api_secret='SECRET')
		client = Client(my_acct)
		pubip = pif.get_public_ip()
		godaddydns = client.get_records("DOMAIN.COM")[-1]['data']
		if pubip != godaddydns:
			client.update_ip(pubip, domains=['pickel.me'])
			print( "{} :: DNS Record updated [{}]".format(nowtime, pubip))
		# else:
			# print("{} :: DNS Record is already updated".format(nowtime))
		time.sleep(60)
	except:
		None