# implementation of card game - Memory

import simplegui
import random
state = 0
previous_index = None
position = 0
index = None
cards = []
exposed = []
turns = 0

# helper function to initialize globals
def new_game():
    global state, exposed, cards, turns, labels
    turns = 0
    update_turns_label(label, turns)
    state = 0
    exposed = [False for x in range(0,19)]
    unique_cards = [x for x in range(1,10)]
    cards = unique_cards + unique_cards
    random.shuffle(cards)

def update_turns_label(label, turns):
    label.set_text("Turns = %d" % turns)
    
# define event handlers
def mouseclick(pos):
    global state, exposed, cards, index, previous_index, position, turns, label
    # add game state logic here
    new_index = pos[0] // 50
    if state == 0: 
        state = 1
        index = pos[0] // 50
        position = 50*index
        print(state)
    elif state == 1:
        if(index != new_index and 
           not exposed[new_index]):
            
            print(previous_index, index)
            state = 2
            turns += 1
            update_turns_label(label, turns)
            print(state)
            
            previous_index = index
            index = pos[0] // 50
            position = 50*index
            
    else:
        if(index != new_index and 
           new_index != previous_index and
           not exposed[new_index]):
            
            if cards[previous_index] == cards[index]:
                exposed[index] = True
                exposed[previous_index] = True
            state = 1
            
            previous_index = index
            index = pos[0] // 50
            position = 50*index
            
        
   
    print cards

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global state, exposed, cards, index, previous_index, position
    
    for card_index in range(0, len(cards)):
        color = "Green"
        card_pos = 50 * card_index
        
        if state == 1 and card_index == index:
            color = "White"
        if state == 2 and (card_index == index or card_index == previous_index):
            color = "White"
        if exposed[card_index]:
            color = "White"
 
        canvas.draw_polygon([[card_pos, 0], [card_pos+50, 0], [card_pos+50, 100], [card_pos, 100]], 1, 'Red', 'Green')
        canvas.draw_text(str(cards[card_index]), (card_pos, 75), 70, color)
        

    
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 900, 100)
frame.set_canvas_background('White')
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = %d" % turns)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
