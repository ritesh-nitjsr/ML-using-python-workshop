#Written by Piyush Ranjan
import requests
import json

b=float(raw_input("Enter price at which BTC were bought "))
n=float(raw_input("Enter no of BTC bought "))
data = {"currencyCode" : "inr"}
resp=requests.get(url="https://live.zebapi.com/api/v1/ticker", params=data)
res=json.loads(resp.content)
x=float(res['sell'])
lp=(x-b)*n
if(lp>0):
    print "profit of Rs%.2f"%lp
elif(lp<0):
    print "loss of Rs%.2f"%abs(lp)
else:
    print "no profit/loss"
