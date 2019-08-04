from tkinter import Canvas, Tk
import helpers
from utilities import *
import time

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()


canvas = Canvas(gui, width=window_width,
                height=window_height, background='white')
canvas.pack()

make_image(canvas, "background.png", size=(
    window_width, window_height), position=(0, 0))


########################## YOUR CODE BELOW THIS LINE ##############################

# sample code to make a creature:

helpers.rolly_cloud(canvas, (0,100), gui, tag="puff")
# helpers.rolly_cloud(canvas, (100,200), gui, tag="puff")
# helpers.rolly_cloud(canvas, (400,50), gui, tag="puff")
# helpers.rolly_cloud(canvas, (200,100), gui, tag="puff")
# helpers.rolly_cloud(canvas, (300,200), gui, tag="puff")
# helpers.rolly_cloud(canvas, (600,50), gui, tag="puff")
# helpers.rolly_cloud(canvas, (400,50), gui, tag="puff") 
# helpers.rolly_cloud(canvas, (0,100), gui, tag="puff")
# helpers.rolly_cloud(canvas, (100,200), gui, tag="puff")
# helpers.rolly_cloud(canvas, (400,50), gui, tag="puff")
# helpers.rolly_cloud(canvas, (200,100), gui, tag="puff")
# helpers.rolly_cloud(canvas, (300,200), gui, tag="puff")
# helpers.rolly_cloud(canvas, (600,50), gui, tag="puff")

MOUSE_CLICK = '<Button-1>'
def make_creature_from_click(event):
    helpers.make_creature(
        canvas,
        (event.x, event.y),
        tag="mom"
    )

canvas.bind(MOUSE_CLICK, make_creature_from_click)
while True:
        helpers.baa_baa(canvas, (240,620), gui, tag="mom")
        



# while True:
#     helpers.baa_baa(canvas, (240,620), gui, tag="mom")
    
        
# for x in range (0,100):
#     if x % 2 == 0:
#         helpers.baa_baa(canvas, (240,620), gui, tag="mom")
#     else:
#         helpers.rolly_cloud(canvas, (100,150), gui, tag="puff")
#         gui.update()
    

   


        


########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
canvas.mainloop()
