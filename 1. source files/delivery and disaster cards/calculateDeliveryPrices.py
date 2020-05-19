import math
import random

materials = []
materials.append("Beer")
materials.append("Cars")
materials.append("Cheese")
materials.append("Feed")
materials.append("Fruit")
materials.append("Furniture")
materials.append("Gas")
materials.append("Grain")
materials.append("Groceries")
materials.append("Honey")
materials.append("Ice Cream")
materials.append("Lumber")
materials.append("Medicine")
materials.append("Milk")
materials.append("Pigs")
materials.append("Pizza")
materials.append("Plants")
materials.append("Turkeys")
materials.append("Water")

cities = []
cities.append(["Aubigny", 109.152, 100.405])
cities.append(["Blumenort", 283.122, 186.498])
cities.append(["Brunkild", 9.228, 156.082])
cities.append(["Domain", 84.299, 186.498])
cities.append(["Dufrost", 171.284, 57.359])
cities.append(["Friedensfeld", 295.548, 121.928])
cities.append(["Giroux", 326.615, 175.736])
cities.append(["Grunthal", 233.416, 78.882])
cities.append(["Ile des Chenes", 196.137, 229.544])
cities.append(["Kleefeld", 227.203, 132.69])
cities.append(["La Broquerie", 345.254, 143.452])
cities.append(["La Salle", 96.883, 229.581])
cities.append(["Landmark", 245.842, 208.021])
cities.append(["Lorette", 233.567, 251.075])
cities.append(["Lowe Farm", 9.741, 57.359])
cities.append(["Marchand", 388.747, 111.167])
cities.append(["Mitchell", 258.269, 143.452])
cities.append(["Morris", 65.776, 46.624])
cities.append(["New Bothwell", 227.203, 175.736])
cities.append(["Niverville", 165.139, 175.76])
cities.append(["Osborne", 71.873, 143.452])
cities.append(["Otterburne", 177.498, 132.69])
cities.append(["Paradise Village", 332.827, 229.544])
cities.append(["Richer", 345.254, 208.021])
cities.append(["Rosenfeld", 22.167, 14.313])
cities.append(["Rosenort", 47.02, 100.405])
cities.append(["Saint-Pierre-Jolys", 196.137, 100.405])
cities.append(["Sainte Agathe", 134.005, 164.975])
cities.append(["Sanford", 34.828, 210.018])
cities.append(["Sarto", 270.695, 78.882])
cities.append(["St. Adolphe", 152.645, 218.783])
cities.append(["St. Jean Baptiste", 84.299, 14.313])
cities.append(["St. Malo", 202.351, 46.597])
cities.append(["Ste. Anne", 301.762, 218.783])
cities.append(["Dufresne", 276.909, 240.306])
cities.append(["Ste. Elizabeth", 115.366, 46.597])
cities.append(["Steinbach", 283.246, 144.114])


sources = [];
sources.append(["Fruit", "Blumenort"])
sources.append(["Fruit", "Blumenort"])	
sources.append(["Furniture", "Blumenort"])												
sources.append(["Turkeys", "Blumenort"])
sources.append(["Grain", "Brunkild"])
sources.append(["Grain", "Dufrost"])
sources.append(["Fruit", "Friedensfeld"])
sources.append(["Honey", "Friedensfeld"])
sources.append(["Cheese", "Grunthal"])
sources.append(["Lumber", "Grunthal"])
sources.append(["Plants", "Grunthal"])
sources.append(["Cars", "Ile des Chenes"])
sources.append(["Ice Cream", "Ile des Chenes"])
sources.append(["Pizza", "Ile des Chenes"])
sources.append(["Honey", "Kleefeld"])
sources.append(["Ice Cream", "Kleefeld"])
sources.append(["Milk", "Kleefeld"])
sources.append(["Ice Cream", "La Broquerie"])
sources.append(["Lumber", "La Broquerie"])
sources.append(["Pizza", "La Broquerie"])
sources.append(["Fruit", "La Salle"])
sources.append(["Gas", "La Salle"])
sources.append(["Grain", "La Salle"])
sources.append(["Feed", "Landmark"])
sources.append(["Milk", "Landmark"])
sources.append(["Pigs", "Landmark"])
sources.append(["Ice Cream", "Lorette"])
sources.append(["Pizza", "Lorette"])
sources.append(["Gas", "Lowe Farm"])
sources.append(["Groceries", "Lowe Farm"])
sources.append(["Water", "Marchand"])
sources.append(["Honey", "Mitchell"])
sources.append(["Ice Cream", "Mitchell"])
sources.append(["Gas", "Morris"])
sources.append(["Ice Cream", "Morris"])
sources.append(["Pizza", "Morris"])
sources.append(["Cars", "New Bothwell"])
sources.append(["Cheese", "New Bothwell"])
sources.append(["Furniture", "Niverville"])
sources.append(["Lumber", "Niverville"])
sources.append(["Plants", "Niverville"])
sources.append(["Feed", "Otterburne"])				
sources.append(["Beer", "Richer"])
sources.append(["Cars", "Rosenort"])
sources.append(["Feed", "Rosenort"])															
sources.append(["Groceries", "Saint-Pierre-Jolys"])
sources.append(["Medicine", "Saint-Pierre-Jolys"])						
sources.append(["Gas", "Sainte Agathe"])												
sources.append(["Groceries", "Sanford"])
sources.append(["Lumber", "Sanford"])							
sources.append(["Beer", "Sarto"])
sources.append(["Pigs", "Sarto"])				
sources.append(["Gas", "St. Adolphe"])
sources.append(["Groceries", "St. Adolphe"])										
sources.append(["Grain", "St. Jean Baptiste"])											
sources.append(["Groceries", "St. Malo"])
sources.append(["Lumber", "St. Malo"])							
sources.append(["Gas", "Ste. Anne"])
sources.append(["Ice Cream", "Ste. Anne"])
sources.append(["Medicine", "Ste. Anne"])
sources.append(["Cars", "Steinbach"])
sources.append(["Feed", "Steinbach"])
sources.append(["Furniture", "Steinbach"])
sources.append(["Pizza", "Steinbach"])			

rivers = [];
rivers.append({"x1":2.22, "y1":258.90, "x2":69.84, "y2":208.19});
rivers.append({"x1":69.84, "y1":208.19, "x2":152.14, "y2":254.01});
rivers.append({"x1":152.14, "y1":254.01, "x2":78.74, "y2":69.40});
rivers.append({"x1":78.74, "y1":69.40, "x2":3.11, "y2":125.89});
rivers.append({"x1":78.74, "y1":69.40, "x2":84.96, "y2":31.58});
rivers.append({"x1":84.96, "y1":31.58, "x2":68.95, "y2":4.89});
rivers.append({"x1":212.63, "y1":263.79, "x2":342.53, "y2":176.16});
rivers.append({"x1":342.53, "y1":176.16, "x2":387.01, "y2":86.30});


class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
# Given three colinear points p, q, r, the function checks if  
# point q lies on line segment 'pr'  
def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False
	
	
def orientation(p, q, r): 
    # to find the orientation of an ordered triplet (p,q,r) 
    # function returns the following values: 
    # 0 : Colinear points 
    # 1 : Clockwise points 
    # 2 : Counterclockwise 
      
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/  
    # for details of below formula.  
      
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0): 
          
        # Clockwise orientation 
        return 1
    elif (val < 0): 
          
        # Counterclockwise orientation 
        return 2
    else: 
          
        # Colinear orientation 
        return 0
		
		
def linesIntersect(p1, q1, p2, q2):
    # Find the 4 orientations required for  
    # the general and special cases 
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
    # General case 
    if ((o1 != o2) and (o3 != o4)): 
        return True
  
    # Special Cases 
  
    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1 
    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True
  
    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1 
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True
  
    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2 
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True
  
    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2 
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True
  
    # If none of the cases 
    return False	




def getCityPoint(city):
	for c in cities:
		if (c[0] == city):
			return [c[1], c[2]]

def countRiverCrossings(x1, y1, x2, y2):
	count = 0;
	
	for river in rivers:
		r1 = Point(river["x1"], river["y1"])
		r2 = Point(river["x2"], river["y2"])
		
		if linesIntersect(Point(x1, y1), Point(x2, y2), r1, r2):
			count += 1
		
	return count


def getCityCost(city1, city2):
	point1 = getCityPoint(city1)
	point2 = getCityPoint(city2)
	x = abs(point1[0] - point2[0])
	y = abs(point1[1] - point2[1])
	distance = math.sqrt(x*x + y*y) / 12.4263 * 1000 + 3000;
	distance += 3000 * countRiverCrossings(point1[0], point1[1], point2[0], point2[1])
	
	distance + 0.7	# to make sure you don't break even deliverying there once
	
	distance = int(round(distance / 1000) * 1000)
	
	return distance
	

def getSourceCities(material):
	cities = []
	
	for s in sources:
		if s[0] == material:
			cities.append(s[1])
	
	return cities

def getClosestCityCost(city, cities):
	if city in cities:
		return 0;
		
	closestCity = cities[0]
	closestDistance = getCityCost(city, cities[0])
	
	for c in cities:
		dist = getCityCost(city, c)
		if dist < closestDistance:
			closestDistance = dist
			closestCity = c
	
	return closestDistance


file = open("delivery prices.txt","w") 

pricesList = []

for city in cities:
	for material in materials:
		cityName = city[0]
		sourceCities = getSourceCities(material)
		if cityName in sourceCities:
			continue
		cost = getClosestCityCost(cityName, sourceCities)
		pricesList.append([cityName, material, str(cost)])
		file.write(cityName + "," + material + "," + str(cost) + "\n")

file.close()

del pricesList[len(pricesList) - len(pricesList) % 3:]	# it needs to be a multiple of 3, because three things per card


for i in range(0, len(pricesList), 3):
	isUniqueThisCard = False
	while not isUniqueThisCard:
		isUniqueThisCard = True
		print "Card " + str(i)
		shuffleMe = pricesList[i:]
		random.shuffle(shuffleMe)
		pricesList[i:] = shuffleMe
		
		if (pricesList[i][1] == pricesList[i+1][1]): isUniqueThisCard = False
		if (pricesList[i+1][1] == pricesList[i+2][1]): isUniqueThisCard = False
		if (pricesList[i][1] == pricesList[i+2][1]): isUniqueThisCard = False
			
		
		

file = open("delivery prices random.txt","w") 

for price in pricesList:
	file.write(price[0] + "," + price[1] + "," + price[2] + "\n")

file.close()

