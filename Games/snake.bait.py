from tkinter import *
import random

#Making constants for further use
GAME_WIDTH= 700
GAME_HEIGHT= 600
SPEED= 120
SPACE_SIZE= 50   #size of each object in the game   #lower the space size smaller will be objects
BODY_PARTS= 3
SNAKE_COLOR= "blue"
FOOD_COLOR= "yellow"
BACKGROUND_COLOR= "black"

class Snake:
    def __init__(self):
        self.body_size= BODY_PARTS
        self.coordinates= []
        self.squares= []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        
        for x,y in self.coordinates:
            square= my_canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x= random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y= random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates= [x,y]

        # id = C.create_oval(x0, y0, x1, y1, option, ...)
        my_canvas.create_oval(x,y, x+ SPACE_SIZE, y+ SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake,food):
    x,y= snake.coordinates[0]

    if direction== "up":
        y -=SPACE_SIZE
    elif direction== "down":
        y +=SPACE_SIZE
    elif direction== "left":
        x -=SPACE_SIZE
    elif direction== "right":
        x +=SPACE_SIZE

    snake.coordinates.insert(0, (x,y))

    square= my_canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y ==food.coordinates[1]:
        global score
        score= score +1

        label.config(text="Score:{}".format(score))
        my_canvas.delete("food")  #tag food we used

        food= Food()  #creating new food 
    else:
        del snake.coordinates[-1]
        my_canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:   #updating to next turn
        root.after(SPEED, next_turn, snake, food)   #for next turn calling next_turn func

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction= new_direction
    elif new_direction == 'right':  #current
        if direction != 'left':   #previous direction
            direction= new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction= new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction= new_direction

#collisions=>with end of screen
def check_collisions(snake):
    x,y= snake.coordinates[0]

    if x<0 or x>= GAME_WIDTH:
        print("GAME OVER")
        return True

    elif y<0 or y>=GAME_HEIGHT:
        print("GAME OVER")
        return True

    for body_part in snake.coordinates[1:]:  #if snake touches its tail
        if x== body_part[0] and y== body_part[1]:
            print("GAME OVER")
            return True
    return False

def game_over():
    my_canvas.delete(ALL)
    my_canvas.create_text(my_canvas.winfo_width()/2, my_canvas.winfo_height()/2,font=('consolas', 70), text= "GAME OVER", fill="red", tag="gameover")
    

root= Tk()
root.geometry("600x700")
root.title("Snake & Bait")
root.resizable(False,False)  #cannot be resized

score=0
direction= 'down'

label= Label(root, text="Score:{}".format(score), font=('consolas',40))
label.pack()

my_canvas= Canvas(root, bg= BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
my_canvas.pack()

root.update()

#The Lambda runtime converts the event to an object and passes it to your function code.
root.bind("<Left>", lambda event: change_direction('left'))
root.bind("<Right>", lambda event: change_direction('right'))
root.bind("<Up>", lambda event: change_direction('up'))
root.bind("<Down>", lambda event: change_direction('down'))

snake= Snake()  #calling constructors
food= Food()

next_turn(snake, food)

root.mainloop()
