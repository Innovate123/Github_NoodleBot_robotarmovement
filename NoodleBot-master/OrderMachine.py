#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import RobotProcess
from Noodle import * 
import DefinationType

def reset():
    #Creation of Menu #
    noodleTypeSelection.set(DefinationType.meePok)
    noodleSizeSelection.set(DefinationType.normal)
    bowlSelection.set(DefinationType.dry)
    mushroomSauceSelection.set(DefinationType.normal)
    abaloneSauceSelection.set(DefinationType.no)
    chilliSauceSelection.set(DefinationType.normal)
    tomatoSauceSelection.set(DefinationType.normal)
    porkLardSelection.set(DefinationType.normal)
    fishSauceSelection.set(DefinationType.normal)
    vinegarSelection.set(DefinationType.normal)
    springOnionSelection.set(DefinationType.normal)
    fishBallSelection.set(DefinationType.normal)
    lettuceSelection.set(DefinationType.normal)
    mincedPorkSelection.set(DefinationType.normal)
    abaloneSelection.set(DefinationType.normal)
    selectAbaloneSauce()
    
def orderNow():
    print "Robot start task now"
    
    newNoodle = NoodleType(noodleTypeSelection.get(), noodleSizeSelection.get())
    
    sauceList = []
    sauceList.append(Sauce(DefinationType.mushroomSauce,mushroomSauceSelection.get()))
    sauceList.append(Sauce(DefinationType.abaloneSauce,abaloneSauceSelection.get()))
    sauceList.append(Sauce(DefinationType.chilliSauce,chilliSauceSelection.get()))
    sauceList.append(Sauce(DefinationType.tomatoSauce, tomatoSauceSelection.get()))
    sauceList.append(Sauce(DefinationType.porkLard,porkLardSelection.get()))
    sauceList.append(Sauce(DefinationType.fishSauce,fishSauceSelection.get()))
    sauceList.append(Sauce(DefinationType.vinegar,vinegarSelection.get()))
    
    condimentList = []
    condimentList.append(Condiment(DefinationType.springOnion,springOnionSelection.get()))
    condimentList.append(Condiment(DefinationType.fishBall,fishBallSelection.get()))
    condimentList.append(Condiment(DefinationType.lettuce,lettuceSelection.get()))
    condimentList.append(Condiment(DefinationType.mincedPork,mincedPorkSelection.get()))
    condimentList.append(Condiment(DefinationType.abaloneStick,abaloneSelection.get()))
    
    newNoodleOrder = Noodle(newNoodle, bowlSelection.get(), sauceList, condimentList)
    
    RobotProcess.makeNoodle(newNoodleOrder)

def selectAbaloneSauce():
    enable = chilliSauceSelection.get() == DefinationType.no
    
    if not enable:
        abaloneSauceSelection.set(DefinationType.no)
    
    for widget in listOfWidget:
        if widget[2] == 5 and widget[1] > 0 :
            if enable:
                widget[0].configure(state='normal')
            else:
                widget[0].configure(state='disabled')

def initDisplay(listOfWidget):
    for widget in listOfWidget:
        # widget[0] is widget, widget[1] is column, widget[2] is row
        widget[0].grid(column = widget[1], row = widget[2]) 
        
    
# Create color for the button
unselectedBackground = "light grey"
selectedBackground = "light green"
text = "black"

# Create a new window
window = Tk()
window.title("Prototype Noodle Pte Ltd")

listOfWidget = []

"""
Create new widget with this format [widget, column, row] for the function to render
"""

# List out all the title
listOfWidget.append([Label(window, text="Noodle Bot Project", font=("Arial Bold", 24)),0,0])
listOfWidget.append([Label(window, text="Which Noodles 什么面 ? "),0,1])
listOfWidget.append([Label(window, text="How much noodle 多少面 ? "),0,2])
listOfWidget.append([Label(window, text="Soup  / Dry 汤或干 ? "),0,3])
listOfWidget.append([Label(window, text="Mushroom Sauce 花菇酱 ? "),0,4])
listOfWidget.append([Label(window, text="Abalone Sauce 鲍鱼酱 ? "),0,5])
listOfWidget.append([Label(window, text="Chilli Sauce 辣椒酱 ? "),0,6])
listOfWidget.append([Label(window, text="Tomato Sauce 番茄酱 ? "),0,7])
listOfWidget.append([Label(window, text="Pork Lard 猪油渣 ? "),0,8])
listOfWidget.append([Label(window, text="Fish Sauce 鱼露 ? "),0,9])
listOfWidget.append([Label(window, text="Vinegar 醋 ? "),0,10])
listOfWidget.append([Label(window, text="Spring onion 青葱 ? "),0,11])
listOfWidget.append([Label(window, text="Fried Fish Ball 炸鱼圆 ? "),0,12])
listOfWidget.append([Label(window, text="lettuce 青菜 ? "),0,13])
listOfWidget.append([Label(window, text="Minced Pork 猪肉碎 ? "),0,14])
listOfWidget.append([Label(window, text="Abalone Stick 鲍鱼串 ? "),0,15])

# List all the selected Option
noodleTypeSelection = IntVar()
noodleSizeSelection = IntVar()
bowlSelection = IntVar()
mushroomSauceSelection = IntVar()
abaloneSauceSelection = IntVar()
chilliSauceSelection = IntVar()
tomatoSauceSelection = IntVar()
porkLardSelection = IntVar()
fishSauceSelection = IntVar()
vinegarSelection = IntVar()
springOnionSelection = IntVar()
fishBallSelection = IntVar()
lettuceSelection = IntVar()
mincedPorkSelection = IntVar()
abaloneSelection = IntVar()

reset()

# List out all the Option
listOfWidget.append([Radiobutton(window, text="Mee Pok 面薄", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.meePok, variable=noodleTypeSelection),1,1])
listOfWidget.append([Radiobutton(window, text="Mee Kia 幼面", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.meeKia, variable=noodleTypeSelection),2,1])
listOfWidget.append([Radiobutton(window, text="Kuay Teow 果条", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.kuayTeow, variable=noodleTypeSelection),3,1])

listOfWidget.append([Radiobutton(window, text="Less 少面", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=noodleSizeSelection),1,2])
listOfWidget.append([Radiobutton(window, text="Normal", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=noodleSizeSelection),2,2])
listOfWidget.append([Radiobutton(window, text="Extra 加面", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=noodleSizeSelection),3,2])

listOfWidget.append([Radiobutton(window, text="Soup 汤", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.soup, variable=bowlSelection),1,3])
listOfWidget.append([Radiobutton(window, text="Dry 干", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.dry, variable=bowlSelection),2,3])


listOfWidget.append([Radiobutton(window, text="No Mushroom Sauce 不要花菇酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=mushroomSauceSelection),1,4])
listOfWidget.append([Radiobutton(window, text="No Abalone Sauce 不要鲍鱼酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=abaloneSauceSelection, state='disabled'),1,5])
listOfWidget.append([Radiobutton(window, text="No Chilli Sauce 不要辣椒酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=chilliSauceSelection, command=selectAbaloneSauce),1,6])
listOfWidget.append([Radiobutton(window, text="No Tomato Sauce 不要番茄酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=tomatoSauceSelection),1,7])
listOfWidget.append([Radiobutton(window, text="No Pork Lard 不要猪油渣 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=porkLardSelection),1,8])
listOfWidget.append([Radiobutton(window, text="No Fish Sauce 不要鱼露 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=fishSauceSelection),1,9])
listOfWidget.append([Radiobutton(window, text="No Vinegar 不要醋 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=vinegarSelection),1,10])
listOfWidget.append([Radiobutton(window, text="No Spring onion 不要青葱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=springOnionSelection),1,11])
listOfWidget.append([Radiobutton(window, text="No Fried Fish Ball 不要鱼圆 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=fishBallSelection),1,12])
listOfWidget.append([Radiobutton(window, text="No lettuce 不要青菜 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=lettuceSelection),1,13])
listOfWidget.append([Radiobutton(window, text="No Minced Pork 不要猪肉碎 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=mincedPorkSelection),1,14])
listOfWidget.append([Radiobutton(window, text="No Abalone Stick 不要鲍鱼串 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.no, variable=abaloneSelection),1,15])


listOfWidget.append([Radiobutton(window, text="Less Mushroom Sauce 少花菇酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=mushroomSauceSelection),2,4])
listOfWidget.append([Radiobutton(window, text="Less Abalone Sauce 少鲍鱼酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=abaloneSauceSelection, state='disabled'),2,5])
listOfWidget.append([Radiobutton(window, text="Less Chilli Sauce 少辣椒酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=chilliSauceSelection, command=selectAbaloneSauce),2,6])
listOfWidget.append([Radiobutton(window, text="Less Tomato Sauce 少番茄酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=tomatoSauceSelection),2,7])
listOfWidget.append([Radiobutton(window, text="Less Pork Lard 少猪油渣 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=porkLardSelection),2,8])
listOfWidget.append([Radiobutton(window, text="Less Fish Sauce 少鱼露 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=fishSauceSelection),2,9])
listOfWidget.append([Radiobutton(window, text="Less Vinegar 少醋 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=vinegarSelection),2,10])
listOfWidget.append([Radiobutton(window, text="Less Spring onion 少青葱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=springOnionSelection),2,11])
listOfWidget.append([Radiobutton(window, text="Less Fried Fish Ball 少鱼圆 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=fishBallSelection),2,12])
listOfWidget.append([Radiobutton(window, text="Less lettuce 少青菜 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=lettuceSelection),2,13])
listOfWidget.append([Radiobutton(window, text="Less Minced Pork 少猪肉碎 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.littleBit, variable=mincedPorkSelection),2,14])


listOfWidget.append([Radiobutton(window, text="Mushroom Sauce 花菇酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=mushroomSauceSelection),3,4])
listOfWidget.append([Radiobutton(window, text="Abalone Sauce 鲍鱼酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=abaloneSauceSelection, state='disabled'),3,5])
listOfWidget.append([Radiobutton(window, text="Chilli Sauce 辣椒酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=chilliSauceSelection, command=selectAbaloneSauce),3,6])
listOfWidget.append([Radiobutton(window, text="Tomato Sauce 番茄酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=tomatoSauceSelection),3,7])
listOfWidget.append([Radiobutton(window, text="Pork Lard 猪油渣 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=porkLardSelection),3,8])
listOfWidget.append([Radiobutton(window, text="Fish Sauce 鱼露 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=fishSauceSelection),3,9])
listOfWidget.append([Radiobutton(window, text="Vinegar 醋 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=vinegarSelection),3,10])
listOfWidget.append([Radiobutton(window, text="Spring onion 青葱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=springOnionSelection),3,11])
listOfWidget.append([Radiobutton(window, text="Fried Fish Ball 鱼圆 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=fishBallSelection),3,12])
listOfWidget.append([Radiobutton(window, text="lettuce 青菜 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=lettuceSelection),3,13])
listOfWidget.append([Radiobutton(window, text="Minced Pork 猪肉碎 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=mincedPorkSelection),3,14])
listOfWidget.append([Radiobutton(window, text="Abalone Stick 鲍鱼串 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.normal, variable=abaloneSelection),3,15])


listOfWidget.append([Radiobutton(window, text="Extra Mushroom Sauce 加花菇酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=mushroomSauceSelection),4,4])
listOfWidget.append([Radiobutton(window, text="Extra Abalone Sauce 加鲍鱼酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=abaloneSauceSelection, state='disabled'),4,5])
listOfWidget.append([Radiobutton(window, text="Extra Chilli Sauce 加辣椒酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=chilliSauceSelection, command=selectAbaloneSauce),4,6])
listOfWidget.append([Radiobutton(window, text="Extra Tomato Sauce 加番茄酱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=tomatoSauceSelection),4,7])
listOfWidget.append([Radiobutton(window, text="Extra Pork Lard 加猪油渣 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=porkLardSelection),4,8])
listOfWidget.append([Radiobutton(window, text="Extra Fish Sauce 加鱼露 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=fishSauceSelection),4,9])
listOfWidget.append([Radiobutton(window, text="Extra Vinegar 加醋 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=vinegarSelection),4,10])
listOfWidget.append([Radiobutton(window, text="Extra Spring onion 加青葱 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=springOnionSelection),4,11])
listOfWidget.append([Radiobutton(window, text="Extra Fried Fish Ball 加鱼圆 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=fishBallSelection),4,12])
listOfWidget.append([Radiobutton(window, text="Extra lettuce 加青菜 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=lettuceSelection),4,13])
listOfWidget.append([Radiobutton(window, text="Extra Minced Pork 加猪肉碎 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=mincedPorkSelection),4,14])
listOfWidget.append([Radiobutton(window, text="Extra Abalone Stick 加鲍鱼串 ? ", bg=unselectedBackground, fg=text, selectcolor=selectedBackground, indicatoron=False, value=DefinationType.more, variable=abaloneSelection),4,15])

# Submit or reset the order
listOfWidget.append([Button(window, text="Reset Order 清除 ? ", bg="red", fg=text, command=reset),3,16])
listOfWidget.append([Button(window, text="Submit Order 确认 ? ", bg="green", fg=text, command=orderNow),4,16])

initDisplay(listOfWidget)

window.mainloop()
