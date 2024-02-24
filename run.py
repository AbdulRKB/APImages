import requests, sys
from string import ascii_lowercase
from random import choice

class Images:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.url = f'https://picsum.photos/{width}/{height}'

	def getImageURL(self):
		imageURL = requests.get(self.url).url
		return imageURL

	def downloadImage(self):
		text = ascii_lowercase
		random_name = ''.join([choice(text) for x in range(10)])+'.jpg'
		image = requests.get(self.url)
		with open(random_name, 'wb') as f:
			f.write(image.content)
			f.close()
		return random_name


def main():
	width = str(input('Image Width: '))
	height = str(input('Image Height: '))
	print('[1] Get Image URL\n[2] Download Image')
	option = str(input('Select Option: '))
	start = Images(width,height)
	if option == '1':
		url = start.getImageURL()
		print(f'[+] Image URL: {url}')
	elif option == '2':
		filename = start.downloadImage()
		print(f'[+] Saved Image as {filename}')
	else:
		print('[-] Invalid Option.. ')
		sys.exit()


if __name__ == '__main__':
	main()