from rgbmatrix import RGBMatrix,RGBMatrixOptions
from time import sleep
import random
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
import os
import sys





# Initialize curses
 # Enable non-blocking getch()

# Loop until 'q' key is pressed



x=0


options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.parallel=1
options.pixel_mapper_config="U-mapper"
row = 64
col = 64
options.hardware_mapping = 'adafruit-hat'
a=1

matrix = RGBMatrix(options = options)


        





MATRIX_MIN_VALUE = 0
MATRIX_MAX_VALUE = 64
MATRIX_SIZE_Y = 64
MATRIX_SIZE_X = 64

while True:
    gameOverFlag = False
    growSnakeFlag = False
    generateRandomFoodFlag = False
    snakeMovementDelay = 0.4
    snakeMovementDelayDecrease = -0.02
    score = 0

    matrix.Clear()


    # Set default snake starting position (values are chosen by preference)
    snakePosX = [32]
    snakePosY = [32]

    # Generate random food position
    while True:
        foodPosX = random.randint(0, 59)
        foodPosY = random.randint(0, 28)
        if foodPosX != snakePosX[0] or foodPosY != snakePosY[0]:
            break

    # Set default snake starting direction (values are chosen by preference)
    movementX = 0
    movementY = -1
   


    while not gameOverFlag:
         
        # Check if snake eats food
        if foodPosX == snakePosX[0] and foodPosY == snakePosY[0]:
            growSnakeFlag = True
            generateRandomFoodFlag = True
            snakeMovementDelay += snakeMovementDelayDecrease
            score = score + 1

        # Check if snake bites itself
        for i in range(1, len(snakePosX)):
            if snakePosX[i] == snakePosX[0] and snakePosY[i] == snakePosY[0]:
                gameOverFlag = True

        # Check if game-over
        if gameOverFlag:
            break
        
        if ser.in_waiting > 0:
            key = ser.readline().decode('utf-8').rstrip()

        # Process the key press
            if key =="L" and movementY != 1:
                movementY = -1
                movementX = 0
                # Handle 'w' key press
            elif key == "R" and movementY != -1:
                movementY = 1
                movementX = 0
                # Handle 's' key press
            elif key == "D" and movementX != 1:
                movementX = -1
                movementY = 0 
                # Handle 'a' key press
            elif key == "U" and movementX != -1:
                movementX = 1
                movementY = 0
            elif key == "RST" :
                os.execl(sys.executable,sys.executable,*sys.argv)
               
                # Handle 'd' key press
       
         


           
            
            
       
           
                 
            # Grow snake
        if growSnakeFlag:
            growSnakeFlag = False
            snakePosX.append(0)
            snakePosY.append(0)

        # Move snake
        for i in range((len(snakePosX) - 1), 0, -1):
            snakePosX[i] = snakePosX[i - 1]
            snakePosY[i] = snakePosY[i - 1]

        snakePosX[0] += movementX
        snakePosY[0] += movementY

        # Check game borders
        if snakePosX[0] > 64: #max x val
            snakePosX[0] -= MATRIX_SIZE_X
        elif snakePosX[0] < 1: #min x val
            snakePosX[0] += MATRIX_SIZE_X
        if snakePosY[0] > 64: #max y val
            snakePosY[0] -= MATRIX_SIZE_Y
        elif snakePosY[0] < 1: #min y val
            snakePosY[0] += MATRIX_SIZE_Y

        # Spawn random food
        if generateRandomFoodFlag:
            generateRandomFoodFlag = False
            retryFlag = True
            while retryFlag:
                foodPosX = random.randint(0, 62)
                foodPosY = random.randint(0, 30)
                retryFlag = False
                for x, y in zip(snakePosX, snakePosY):
                    if x == foodPosX and y == foodPosY:
                        retryFlag = True
                        break

        # Update matrix
        matrix.Clear()
        matrix.SetPixel(foodPosX, foodPosY, 125,18,255)
        for x, y in zip(snakePosX, snakePosY):
            matrix.SetPixel(x, y, 255,255,255)

        # Snake speed (game loop delay)
        sleep(snakeMovementDelay)

    # Blink the dead snake
    for loop in range (5):
        matrix.Clear()
        matrix.SetPixel(foodPosX, foodPosY, 125,18,255)
        for x, y in zip(snakePosX, snakePosY):
            matrix.SetPixel(x, y, 125,18,255)
        sleep(0.5)
        
        matrix.Clear()
        matrix.SetPixel(foodPosX, foodPosY, 125,18,255)
        for x, y in zip(snakePosX, snakePosY):
            matrix.SetPixel(x, y, 255,255,255)
        sleep(0.5)

    matrix.Clear()
    

    # Display score
  


    
    
        



    



