from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x=10
y=90
t=0



while(1):
    while(x<780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+8
        delay(0.01)
    while(y<580):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+8
        delay(0.01)
    while(x>30):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-8
        delay(0.01)
    while(y>80):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-8
        delay(0.01)
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+8
        delay(0.01)
    while(t<360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+(math.cos(math.pi/180*t))*10
        y=y+(math.sin(math.pi/180*t))*10
        t=t+2
        delay(0.01)
    t=0
        
        
        
        
        


    






    








    
   



