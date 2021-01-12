#! Python 3
# Takes a word as user input and searches Flickr.com for pictures based on that word
# then downloads the first 25 pics into a directory 

import os, requests, bs4, sys

search = input("What would you like to search? ")
url = 'https://flickr.com/search/?text=' + search
response = requests.get(url)
response.raise_for_status()

#Makes a Directory to download the files into
os.makedirs(search, exist_ok = True)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

imagesElem = soup.select('.view-photo-list-view .overlay')
print(imagesElem)
if imagesElem == []:
	print("No images for that search.")
else:
	numCount = min(25, len(imagesElem))
	for i in range(numCount):
		aFromDiv = imagesElem[i].select('a')
		imageUrl = 'https://flickr.com/photos/53889145@N02/7029097495/'
		print("Downloading image %s..." % (imageUrl))
		response = requests.get(imageUrl)
		response.raise_for_status()

		imageFile = open(os.path.join(search, os.path.basename(imageUrl)), 'wb')
		for chunk in response.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

print("Done.")