import csv
#TODO: time parsing
#TODO: support for lab classes 


#first tree, stores in a dictionary (keys from the webtree flowchart)
def makeFirstTree(f,s,s2,t,t2):
	tree1 = {}
	tree1["1"]=f
	tree1["1a"]=s
	tree1["1b"]=s2
	tree1["1aa"] = t
	tree1["1ba"] = t
	tree1["1ab"] = t2
	tree1["1bb"] = t2
	print(tree1)
	return

#second tree, stores in dictionary
def makeSecondTree(s,t,t2,fth,fth2):
	tree2 = {}
	tree2["2"]=s
	tree2["2a"]=t
	tree2["2b"]=t2
	tree2["2aa"] = fth
	tree2["2ba"] = fth
	tree2["2ab"] = fth2
	tree2["2bb"] = fth2
	print(tree2)
	return

#third tree, stores in dictionary. The logic for the top of the tree probably isn't perfect
def makeThirdTree(s2,t,t2,fth,fth2):
	tree2 = {}
	tree3["3"]=s2
	tree3["3a"]=t
	tree3["3b"]=t2
	tree3["3aa"] = fth
	tree3["3ba"] = fth
	tree3["3ab"] = fth2
	tree3["3bb"] = fth2
	print(tree3)
	return

#gets user input for right now
def GetClasses():
	print("Use full class codes WITH SECTION when entering classes, and follow the on screeen prompts")
	f = input("Enter a first priority class: ")
	s = input("Enter a second priority class: ")
	s2 = input("Enter an alternate for your second priority class: ")
	t = input("Enter a third priority class: ")
	t2 = input("Enter an alternate for your third priority class: ")
	fth = input("Enter a fourth priority class: ")
	fth2 = input("Enter an alternate for your fourth priority class: ")
	choicesDict = {
	"Class1":f, "Class2":s,"Class2Alt":s2,"Class3":t,
	"Class3Alt":t2,"Class4":fth,"Class4Alt":fth2
	}
	#stores classes in a Dictionary
	return choicesDict

#parses the CSV into a dictionary of dictionaries
def ParseCSV():
	classes = {}
	with open("classes.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    	for row in csv_file:
        	classes[dict(row)["SUBJECT"]] = {"Time": dict(row)["CLASS_TIME"], "Days": dict(row)["MEET_DAYS"]}
    return classes

def checkConflicts(classes,choicesDict):
	#will parse times into time objects
	#not sure how the conflict checking will work quite yet
	return

