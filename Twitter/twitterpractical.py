
import urllib2, twitter

file = open("twitterAPI.txt")
creds = file.read().split('\n')
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
text_file = open("/Users/rogerhart2/Library/Application Support/Google/Chrome/Default/Current Session")
content = text_file.read()
startIndex = content.rfind("http")
#print(startIndex)
endIndex = content.find(chr(0),startIndex)
#print(endIndex)

url = content[startIndex:endIndex]


#session = lines.rfind("http")
#url=lines[session:]
#data = url.split("http://")
#print data[-1]
response = urllib2.urlopen(url)
html = response.read()

searchTitle = html.find("<title>")
endsearchTitle = html.find("</title>")
title = html[searchTitle:endsearchTitle]
title = title.replace("<title>","")
print title
reply = api.PostUpdate("I visited " + str(title))
