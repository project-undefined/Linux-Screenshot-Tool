import os

#---------------------------------------------------------------------

#Save Preset Names
cfgNames = [
	"Default",	#DO NOT DELETE THIS LINE
	"Pictures",
	"Documents",
	"Downloads"
]

#Save Preset Paths
cfgPaths = [
	os.environ['HOME'], #DO NOT DELETE THIS LINE
	"/home/pi/Pictures",
	"/home/pi/Documents",
	"/home/pi/Downloads"
]

#---------------------------------------------------------------------




def saveNames():
	return cfgNames
def savePaths():
	return cfgPaths

print(saveNames())
print(savePaths())
