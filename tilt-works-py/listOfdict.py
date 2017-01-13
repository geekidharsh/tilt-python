import sys

list = [{'apple': 1, 'banana': 2}, {'orange': 3, 'strawberry': 4}, {'avocado': 5, 'grapes': 6}]

# The 'u' in front of the string values means the string has been represented as unicode. 
# It is a way to represent more characters than normal ascii can manage.
listSec = {u'sitemap': 
[{	u'errors': u'135', 
	u'warnings': u'33', 
	u'isPending': False, 
	u'lastSubmitted': u'2014-06-14T21:29:08.679Z', 
	u'isSitemapsIndex': True, 
	u'lastDownloaded': u'2016-12-17T04:45:42.613Z', 
	u'path': u'http://www.emdmillipore.com/CA/en/sitemap/sitemap.xml', 
	u'contents': [{
		u'indexed': u'25180', 
		u'type': u'web', 
		u'submitted': 
		u'45939'}]
}]}

print list, 
print "\n\t" 
for items in listSec['sitemap'][0]['contents']:
	print items
