import webbrowser

url = input("URL: ")

url = url[:12]+'ss'+url[12:]
webbrowser.open(url)