import random
import subprocess

# if the following line dies on you, run this: pip install Pillow
from PIL import Image

file = open("delivery prices random.txt","r") 
prices = file.read().split("\n")
file.close()

cardFile = Image.open('delivery card files/delivery cards 1.png')

def addIconsToCard(cardFile, x, y, prices, pricesStartingIndex):
	parts = prices[pricesStartingIndex + 0].split(",")
	materialFile = Image.open('material icons/'+parts[1]+'.png').resize((50, 50), Image.LANCZOS)
	position = (125 + 192 * x, 64)
	cardFile.paste(materialFile, position)

	parts = prices[pricesStartingIndex + 1].split(",")
	materialFile = Image.open('material icons/'+parts[1]+'.png').resize((50, 50), Image.LANCZOS)
	position = (125 + 192 * x, 124)
	cardFile.paste(materialFile, position)

	parts = prices[pricesStartingIndex + 2].split(",")
	materialFile = Image.open('material icons/'+parts[1]+'.png').resize((50, 50), Image.LANCZOS)
	position = (125 + 192 * x, 184)
	cardFile.paste(materialFile, position)

addIconsToCard(cardFile, 0, 0, prices, 0)
addIconsToCard(cardFile, 1, 0, prices, 3)
addIconsToCard(cardFile, 2, 0, prices, 6)
addIconsToCard(cardFile, 3, 0, prices, 9)

cardFile.save('delivery card files with icons/delivery cards 1.png')

# im2 = Image.open('image/path/2.png')



# for i in prices:
#	line = i.split(",")
#	print line[0] + " --- " + line[1] + " ---> " + line[2]
	