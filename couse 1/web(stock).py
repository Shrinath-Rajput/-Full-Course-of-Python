import re
import urllib.request
arryofstock=["FB","GOOG","DATA","BABA"]
url="https://www.google.com/finance?="
stock=input("Enter your stock :")
url1=url+stock#concatenation of string
print(url1)

data =urllib.request.urlopen(url1).read()
data1 =data.decode("utf-8")
m=re.search('meta iteamprop="price"',data1)
start1=m.start()
end=start1 +50
newstring=data1[start1:end]
m1=re.search('content="',newstring)
start2=m1.end()
newstring1=newstring[start1:]
m2=re.search("/",newstring1)
start1=0
end=m2.end()-3
final=newstring1[0:end]
print("the value of "+stock.upper()+"is"+final)


