import urllib.request, urllib.parse, urllib.error
import re
import os

def slugify(value):
	import unicodedata
	print((type(value)))
	if not isinstance(value, str):
		value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
		value = str(re.sub('[^\w\s-]', '', value).strip().lower())
		value = str(re.sub('[-\s]+', '-', value))
	else:
		value = re.sub('[^\w\s-]', '', value.strip().lower())
		value = re.sub('[-\s]+', '-', value)
	return value

def getCache(file):
	#fndomain=slugify(domain.decode('unicode-escape'))
	fpurl='cachedData/'+file
	if not os.path.isfile(fpurl):
		return None
	else:
		f=open(fpurl,'r')
		return f.read()

def writeCache(file,data):
	data=str(data)
	fpurl='cachedData/'+file
	newfolder='cachedData'
	if not os.path.exists(newfolder):
		os.makedirs(newfolder)
	f=open(fpurl,'w+')
	f.write(data)
	f.close()

def getUrlFile(url):
	#print 'getting file: '+url
	urlfn=slugify(url)
	fpurl='cachedData/'+urlfn
	if not os.path.isfile(fpurl):
		print(('whats going wrong here: '+url+"^"+fpurl))
		urllib.request.urlretrieve(url,fpurl)
		#data=myopener.open(url).read()
		#writeCache(urlfn,data)
	return fpurl
