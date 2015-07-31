# Copy the code and paste in www.codeskulptor.com and then click on the 
# "Run button" located on the website.
# Please check the Readme file for more details.

# Implementation of card game - Memory

import simplegui
import random

width = 800
height = 100

number_of_cards = 16

x1 = 0
x2 = 0
x3 = 0
x4 = 0

y1 = 0
y2 = 0
y3 = 100
y4 = 100

inc = 50
isFound = 0

click = 0
turns = 0

block = []
cards = []
random_numbers = []
opencards = []

# helper function to initialize globals
def new_game():
    global cards, x1, x2, x3, x4, y1, y2, y3, y4, turns
    global random_numbers,click, block, isFound,opencards
    turns = 0
    isFound = 0
    opencards = []
    click = 0
    block = []
    mapping = {}
    random_numbers = []
    label.set_text("Turns = 0")
    for x in xrange(50,width+50,50):
        x2 = x1 + inc
        x3 = x4 + inc
        temp_list = [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
        cards.append(temp_list)
        x1 = x2
        x4 = x3
    for x in xrange(0,number_of_cards/2,1):
        temp = random.randint(0,9)
        random_numbers.append(temp)
        random_numbers.append(temp)
    random.shuffle(random_numbers)
    random.shuffle(random_numbers)
    random.shuffle(random_numbers)
    for x in xrange(0,number_of_cards,1):
        mapping[x] = random_numbers[x]
    
     
# define event handlers
def mouseclick(pos):
    global click, block,opencards, random_numbers, isFound, turns
    current_click = pos[0]/50
    click = click + 1
    if click <= 2:
        block.append(current_click)
        if click == 2:
            if random_numbers[block[0]] == random_numbers[block[1]]:
                opencards.append(block[0])
                opencards.append(block[1])
                isFound = 1
            else:
                turns = turns + 1
                label.set_text("Turns = "+str(turns))
    if click > 2:
        click = 1
        block = []
        block.append(current_click)
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global block, click, random_numbers, isFound,  opencards
    for k in xrange(0,number_of_cards):
        canvas.draw_polygon(cards[k],4,"Black","Green")
    if click == 1:
        canvas.draw_polygon(cards[block[0]],4,"Black","Black")
        canvas.draw_text(str(random_numbers[block[0]]),[block[0]*50+17, 60],40,"white")
    if click == 2:
        canvas.draw_polygon(cards[block[0]],4,"Black","Black")
        canvas.draw_text(str(random_numbers[block[0]]),[block[0]*50+17, 60],40,"white")
        canvas.draw_polygon(cards[block[1]],4,"Black","Black")
        canvas.draw_text(str(random_numbers[block[1]]),[block[1]*50+17, 60],40,"white")
    if isFound == 1:
        k = 0
        while (k < len(opencards)):
            canvas.draw_polygon(cards[opencards[k]],4,"Black","Black")
            canvas.draw_text(str(random_numbers[opencards[k]]),[opencards[k]*50+17, 60],40,"white")
            k = k + 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", width, height)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
