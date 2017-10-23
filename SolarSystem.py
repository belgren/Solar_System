import scipy.constants as sc
import graphics as gr
import random
from math import *

def MainMenu():
    """Printed Menu"""
    choice = int(input("1) Use our solar system\n2) Create your own solar system\n3) Quit\nYour Choice: "))
    return choice

def Main():
    """
        main function; runs menu, takes input, draws solar system
    """
    done = False
    while not done:
        choice = MainMenu()
        #Menu option to show model of our solar system
        if choice == 1:
            our_system()
        #Menu option to input parameters for different planets
        elif choice == 2:
            choose_system()

        elif choice == 3:
            break

def our_system():
    names = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn", "Uranus", "Neptune"]
    smas = [0.387, 0.7231, 1.0, 1.5273, 5.2028, 9.5388, 19.1914, 30.0611]
    periods = [0.2408, 0.6152,1,1.8809,11.862,29.458,84.01,164.79]
    diams = [4800,12100,12750,6800,142800,120660,51800,49500]
    angle = [0,0,0,0,0,0,0,0]
    namesPerm = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn", "Uranus", "Neptune"]
    draw(names,smas,periods,diams,angle,namesPerm)

def choose_system():
    names = []
    smas = []
    periods = []
    masses = []
    angle = []
    diams = []
    namesPerm = []
    while True:
        name = input ("Enter Planet Name or 'quit': ")
        if name == "quit" or name == "Quit":
            break
        sma = input ("Enter Semimajor Axis: ")
        period = input("Enter Period: ")
        diam = input("Enter Planet Diameter: ")
        angle.append(0)
        names.append(name)
        namesPerm.append(name)
        smas.append(float(sma))
        diams.append(float(diam))
        periods.append(float(period))
    draw(names,smas,periods,diams,angle,namesPerm)

def draw(names,smas,periods,diams,angle,namesPerm):
    """Creates window with moving solar system with inputed parameters
    """
    win = gr.GraphWin('Solar System',2000,700)
    #Draw the sun in the center
    sun = gr.Circle(gr.Point(600,350), 10)
    sun.draw(win)
    sun.setFill(gr.color_rgb(255,255,0))
    #Add sun to color legend in the left corner
    box = gr.Rectangle(gr.Point(10,10),gr.Point(20,20))
    box.setFill(gr.color_rgb(255,255,0))
    box.draw(win)
    label = gr.Text(gr.Point(50,15),"Sun")
    label.draw(win)
    cx = 10
    cy = 10
    tx = 50
    ty = 15
    for j in range(0, len(smas)):
        y = 350 - (smas[j] * 35)
        names[j] = gr.Circle(gr.Point(600,y),(diams[j]/2600))
        names[j].draw(win)
        r = random.randrange(254)
        g = random.randrange(254)
        b = random.randrange(254)
        names[j].setFill(gr.color_rgb(r,g,b))
        ty += 12
        cy += 12
        #Draw a color legend in the left corner
        box = gr.Rectangle(gr.Point(cx,cy),gr.Point(cx+10,cy+10))
        box.setFill(gr.color_rgb(r,g,b))
        box.draw(win)
        label = gr.Text(gr.Point(tx,ty),namesPerm[j])
        label.draw(win)

    close = False
    while close == False:
        #loop that makes each planet move at a speed according to its period
        for i in range(0, len(names)):
            planet = names[i]
            radius = (smas[i]*35)
            x = radius * sin(angle[i]) + 600
            y = radius * cos(angle[i]) + 350
            planet.move(x - planet.getCenter().getX(), y - planet.getCenter().getY())
            angle[i] += 0.1 / periods[i]
            #continue with the menu if the display window is closed
            if win.isClosed():
                close = True
    win.close()
Main()
