import os

#---------------------------------------------------------------------

#Save Preset Names
cfgNames = [
	"Default"	#DO NOT DELETE THIS LINE
]

#Save Preset Paths
cfgPaths = [
	os.environ['HOME'] #DO NOT DELETE THIS LINE
]

#---------------------------------------------------------------------




def saveNames():
	return cfgNames
def savePaths():
	return cfgPaths

print(saveNames())
print(savePaths())
