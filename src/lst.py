from guizero import App, Text, TextBox, PushButton, Combo
import time
import os
import config as cfg


def scrot():
	print("recieved\n")
	if timeBox.value=="":
		time=""
	else:
		time=" -d "+timeBox.value
	
	if nameBox.value=="":
		name="'%Y-%m-%d_$wx$h.png'"
	else:
		name="'"+nameBox.value+".png'"
	
	if selectBox.value=="True":
		select=" -s"
	else:
		select=""
	
	for i in range(len(cfg.saveNames())):
		if saveBox.value==cfg.saveNames()[i]:
			save=cfg.savePaths()[i]
			break
	
	print("running 'scrot "+name+time+select+"'")
	os.system("scrot "+name+time+select)
	print("done\n")
	print("running 'mv "+os.getcwd()+"/*.png "+save+"'")
	os.system("mv "+os.getcwd()+"/*.png "+save)
	print("done")
	print("\nFinsihed!\n")


app = App(title="Screenshot")
timeText = Text(app, "Time:")
timeBox = TextBox(app, "")
nameText = Text(app, "\nName:")
nameBox = TextBox(app, "")
selectText = Text(app, "\nSelect Area?")
selectBox = Combo(app,
	options=["True","False"])
saveText = Text(app, "\nSave Location:")
options=[]
for i in cfg.saveNames():
	options.append(i)
saveBox = Combo(app,
	options)
shot = PushButton(app, scrot, text="Screenshot")
print("\ndisplayed\n")
app.display()

