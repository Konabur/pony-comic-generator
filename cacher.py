import urllib.request, urllib.parse, urllib.error
import re
import os

def slugify(value):
	value = re.sub(r'[^\w\s-]+', '', value.strip().lower())
	return re.sub(r'[-\s]+', '-', value)

def getUrlFile(url):
	#print 'getting file: '+url
	urlfn=slugify(url)
	fpurl='cachedData/'+urlfn
	if not os.path.isfile(fpurl):
		print(('whats going wrong here: '+url+"^"+fpurl))
		urllib.request.urlretrieve(url,fpurl)
		#data=myopener.open(url).read()

	return fpurl
