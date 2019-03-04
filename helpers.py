from math import sin, pi
import time
from utilities import *
    # your code to create your creature goes here:
primary_colors = ["grey", "black"]
secondary_colors = ["#000000", "#FFFFFF"]

def make_landscape_object(canvas, center, tag="puff"):
    make_oval(canvas, (center[0], center[1]), 46, 35, color="white", stroke_width=0, tag=tag)
    make_oval(canvas, (center[0]+30, center[1]+10), 50, 45, color="white", stroke_width=0, tag=tag)
    make_oval(canvas, (center[0]+40, center[1]), 30, 35, color="white", stroke_width=0, tag=tag)

def rolly_cloud(canvas, location, gui, tag="puff"):
    make_landscape_object(canvas, location, tag=tag)
    for x in range (0,500):
        time.sleep(.05)
        update_position(canvas,'puff', x=3, y=0)
        gui.update()
   
        
   
    # your code to create your creature goes here:

# Center = 240, 620
def make_creature(canvas, center, primary_color="grey", secondary_color="#000000", tag="mommasheep"):
    index = int(random.uniform(0, 2))
    primary_color = primary_colors[index]
    secondary_color = secondary_colors[index]
    make_oval(canvas, (center[0]-20, center[1]+130), 13, 28, color=secondary_color, tag=tag) #back left leg
    make_oval(canvas, (center[0]+20, center[1]+130), 13, 28, color=secondary_color, tag=tag) #back right leg
    make_circle(canvas, center, 140, color=primary_color, stroke_width=0, tag=tag) #grey body circle
    make_oval(canvas, (center[0]-50, center[1]+140), 15, 30, color=secondary_color, tag=tag) #front left leg
    make_oval(canvas, (center[0]+50, center[1]+140), 15, 30, color=secondary_color, tag=tag) #front right leg
    make_oval(canvas, (center[0], center[1]-30), 86, 75, color="white", stroke_width=0, tag=tag) #face
    make_oval(canvas, (center[0], center[1]-110), 58, 32, color=primary_color, tag=tag, stroke_width=2, outline="white") #grey tuft
    make_oval(canvas, (center[0]-65, center[1]-90), 20, 13, color=primary_color, tag=tag, stroke_width=1, outline="white") #left ear
    make_oval(canvas, (center[0]+65, center[1]-90), 20, 13, color=primary_color, tag=tag, stroke_width=1, outline="white") #right ear
    make_circle(canvas, (center[0]-20, center[1]-50), 30, color="#000000",tag=tag, stroke_width=0) #black left eye
    make_circle(canvas, (center[0]+20, center[1]-50), 30, color="#000000", tag=tag, stroke_width=0) #black right eye 
    make_circle(canvas, (center[0]-30, center[1]-60), 15, color="#FFFFFF",tag=tag, stroke_width=0) #black left eye
    make_circle(canvas, (center[0]+13, center[1]-60), 15, color="#FFFFFF", tag=tag, stroke_width=0) #black right eye 

def baa_baa(canvas, location, gui, tag='mommasheep'):
    make_creature(canvas, location, tag=tag)
    for x in range (0,100):
        time.sleep(.5)
        if x % 2 == 0:
            update_position(canvas, tag, x=0, y=-100)
        else:
            update_position(canvas, tag, x=0, y=100)
        gui.update()
   



    # def make_creature(canvas, center, primary_color="grey", secondary_color="#000000"):
    # make_oval(canvas, (210, 750), 13, 28, color=secondary_color) #back left leg
    # make_oval(canvas, (260, 750), 13, 28, color=secondary_color) #back right leg
    # make_circle(canvas, (240, 620), 140, color=primary_color, stroke_width=0) #grey body circle
    # make_oval(canvas, (190, 760), 15, 30, color=secondary_color) 
    # make_oval(canvas, (280, 760), 15, 30, color=secondary_color) 
    # make_oval(canvas, (240, 590), 86, 75, color="white", stroke_width=0) #face
    # make_oval(canvas, (240, 530), 58, 32, color=primary_color, stroke_width=2, outline="white") #grey tuft
    # make_oval(canvas, (175, 530), 20, 13, color=primary_color, stroke_width=1, outline="white") #left ear
    # make_oval(canvas, (300, 530), 20, 13, color=primary_color, stroke_width=1, outline="white") #right ear
    # make_circle(canvas, (240, 560), 30, color=secondary_color, stroke_width=0) 
    # make_circle(canvas, (260, 560), 30, color=secondary_color, stroke_width=0) 

    