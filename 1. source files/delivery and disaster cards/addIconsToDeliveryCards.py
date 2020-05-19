import random
import subprocess

# if the following line dies on you, run this: 
# pip install Pillow
# pip install setuptools
# pip install blend-modes
from PIL import Image

file = open("delivery prices random.txt","r") 
prices = file.read().split("\n")
file.close()


def lighten(value):
	return int(255 - ((255 - value) * 0.5))

def addIconToImage(cardFile, x, y, spotIndex, material):
	materialFile = Image.open('material icons/'+material+'.png').resize((150, 150), Image.LANCZOS).convert('RGBA')
	startY = [200, 388, 576]
	destx = 393 + 600 * x
	desty = startY[spotIndex] + 787 * y
	for y in range(0, 150-1):
		for x in range(0, 150-1):
			mr, mg, mb, ma = materialFile.getpixel((x, y))
			mr = lighten(mr)
			mg = lighten(mg)
			mb = lighten(mb)
			ma = lighten(ma)
			
			cr, cg, cb, ca = cardFile.getpixel((destx+x, desty+y))
			fr = min(mr, cr)
			fg = min(mg, cg)
			fb = min(mb, cb)
			fa = min(ma, ca)
			cardFile.putpixel((destx+x, desty+y), (fr, fg, fb, fa))
	

def addIconsToCard(cardFile, x, y, prices, pricesStartingIndex):
	addIconToImage(cardFile, x, y, 0, prices[pricesStartingIndex + 0].split(",")[1])
	addIconToImage(cardFile, x, y, 1, prices[pricesStartingIndex + 1].split(",")[1])
	addIconToImage(cardFile, x, y, 2, prices[pricesStartingIndex + 2].split(",")[1])


priceIndex = 0
fileIndex = 1
done = False

while not done:
	cardFile = Image.open('delivery card files/delivery cards '+str(fileIndex)+'.png').convert('RGBA')
	
	for y in range(0, 4):
		if done: break
		for x in range(0, 4):
			print "Calling " + str(x) + "," + str(y) + " page=" + str(fileIndex) + " index=" + str(priceIndex) + " / " + str(len(prices));
			addIconsToCard(cardFile, x, y, prices, priceIndex)
			priceIndex += 3
			if priceIndex + 1 > len(prices):
				print "Done"
				done = True
				x = 4
				y = 4
				break

	cardFile.save('delivery card files with icons/delivery cards '+str(fileIndex)+'.png')
	fileIndex += 1



# im2 = Image.open('image/path/2.png')

# for i in prices:
#	line = i.split(",")
#	print line[0] + " --- " + line[1] + " ---> " + line[2]
	