file = open("disaster card template.svg","r") 
templatecontents = file.read()
file.close()

file = open("disaster messages.txt","r") 
messages = file.read().split("\n")
file.close()

for line in messages:
	if line == "": continue
	print("Line is " + line)
	parts = line.split("|")
	title = parts[0]
	description = parts[1]
	templatecontents = templatecontents.replace('Title', title, 1);
	templatecontents = templatecontents.replace('Description', description, 1);

file = open("disaster cards.svg","w") 
file.write(templatecontents)
file.close()


