import urllib.request
url = input("URL: ")
print(urllib.request.urlopen('{}'.format(url)).read())