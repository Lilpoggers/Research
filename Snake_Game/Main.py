from tkinter import *

import random

#Variables that are the game settings. They are like constants.
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 25
BODY_PARTS = 1
SNAKE_COLOR = "#FFC0CB"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#FFFFFF"


#Creates the snake for the game, gives the snake size for each body part and places the snake in the top left corner.
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


#Creates the food for the game, randomly places one of them and makes it oval.
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")



def next_turn(snake, food):
    #Makes it so that the snake is able move up or down and left or right.
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    #Shows the snake moving.
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    #Makes it soe the snake can collided with the food and if it did then add 1 to score.
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
        
        #Removes where the snake body was after moving.
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


#Make sit so that the snake can not go left and right / up and down at the same time.
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction



def check_collisions(snake):
    #Makes it so the snake can collide with the edges of the window and if ture the game ends.
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    #Makes it so the snake can collide with its body parts and if true then end game.
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


#Deletes everything on screen then says game over.
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

#Makes Tk() mean window and gives the wondow a name.
window = Tk()
window.title("Snake game")

#Makes the window not resizable.
window.resizable(False, False)

#Score at the start of the game.
score = 0

#The direction the snake well be facing.
direction = 'down'

#Makes a label at the top of the window and makes the text score.
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

#Makes the window.
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


#Makes the window go to the middle of the screen.
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Allows the snake know what button was pressed.
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

#Makes the snake and food object
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
