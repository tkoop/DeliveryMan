import random
import subprocess

file = open("delivery prices random.txt","r") 
prices = file.read().split("\n")
file.close()


file = open("delivery card template without icons.svg","r") 
originalTemplateContents = file.read()
file.close()

priceFileIndex = 0
fileIndex = 1

done = False

while not done:
	
	templateContents = originalTemplateContents
	priceIndex = 1

	for i in range(0, 16*3):
		if (priceFileIndex >= len(prices)):
			done = True
			break
		
		line = prices[priceFileIndex]
		
		priceFileIndex += 1
		
					
		print("Line is " + line)
		parts = line.split(",")
		
		city = parts[0]
		material = parts[1]
		cost = parts[2]
		
		if len(cost) > 4:
			cost = "$" + cost[0:2] + ",000"
		else:
			cost = "$" + cost
		
		print city + ", " + material + ", " + cost
		
		templateContents = templateContents.replace('Place'+str(priceIndex), city, 1);
		templateContents = templateContents.replace('Material'+str(priceIndex), material, 1);
		templateContents = templateContents.replace('Price'+str(priceIndex), cost, 1);
		
		priceIndex += 1
		if priceIndex == 4 : priceIndex = 1

	
	file = open("delivery card files/delivery cards "+str(fileIndex)+".svg","w") 
	file.write(templateContents)
	file.close()
	
	command = ["inkscape", "--export-area-page", "--export-dpi=300", "--file=delivery card files/delivery cards "+str(fileIndex)+".svg", "--export-png=delivery card files/delivery cards "+str(fileIndex)+".png", "--without-gui"]
		
	print command
	
	subprocess.call(command)
	
	fileIndex += 1

