#Robin Hood Video Game (CPT)
#Design a video game based on the theme of charity
#Using the pygame module
#@author: Tomasz Modrzejewski
#@course: ICS3U
#@date: 2022/1/20

#Subprograms and classes

#Robin Hood class
class Robin():
    pos = [600, 600]

    #Subprogram to draw Robin Hood
    def draw(self):
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.polygon (screen, ORANGE, [[x, y], [x-15, y-5], [x-20, y-13], [x-50, y-5], [x-40, y+18], [x-10, y+18]])
        pygame.draw.polygon (screen, BLACK, [[x, y], [x-2, y-1], [x-2, y+4]])
        pygame.draw.ellipse (screen, BLACK, [x-23, y-3, 2, 2])
        pygame.draw.polygon (screen, GREEN, [[x-15, y-15], [x-52, y], [x-50, y-20]])
        pygame.draw.polygon (screen, BURGUNDY, [[x-45, y-10], [x-60, y-23], [x-53, y-25], [x-43, y-13]]) 
        pygame.draw.rect (screen, GREEN,[x-35, y+18, 20, 30])
        pygame.draw.rect (screen, ORANGE, [x-20, y+30, 20, 5])
        pygame.draw.rect (screen, ORANGE, [x-35, y+48, 9, 10])
        pygame.draw.rect (screen, ORANGE, [x-24, y+48, 9, 10])
        pygame.draw.polygon (screen, BLACK, [[x-10, y+10], [x,y+20], [x,y+40], [x-10, y+50]], 3)

    #Subprogram to move Robin Hood
    def move(self, xMove, yMove):
        self.pos[0] += xMove
        self.pos[1] += yMove
        if self.pos[0] > 1200:
            self.pos[0] = 1200
        if self.pos[0] < 440:
            self.pos[0] = 440
        if self.pos[1] < 450:
            self.pos[1] = 450
        if self.pos[1] > 750:
            self.pos[1] = 750

#Subprogram to draw a  house
def drawHouse(x, yChange):
    y = yChange
    pygame.draw.rect(screen, WALL, [x, 550-y, 200, 150])
    pygame.draw.polygon(screen, ROOF, [[x-25, 590-y], [x, 520-y], [x+200, 520-y], [x+225, 590-y]])
    pygame.draw.rect(screen, WINDOW, [x+20, 625-y, 40, 40])
    pygame.draw.rect(screen, WINDOW, [x+140, 625-y, 40, 40])
    pygame.draw.rect(screen, WOOD, [x+87, 665-y, 25, 35])
    pygame.draw.line(screen, WOOD, [x+39, 625-y], [x+39, 665-y], 2)
    pygame.draw.line(screen, WOOD, [x+20, 645-y], [x+60, 645-y], 2)
    pygame.draw.line(screen, WOOD, [x+159, 625-y], [x+159, 665-y], 2)
    pygame.draw.line(screen, WOOD, [x+140, 645-y], [x+180, 645-y], 2)

#Subprogram to get tree positions
def getTreePos(treeList):

    #Assign the tree positions in increments of 125
    for i in range(0, 1200, 125):
        x = i
        treeList.append(x)

#Subprogram to draw trees
def drawTree(x):
    pygame.draw.rect(screen, WOOD, [x, 425, 40, 75])
    pygame.draw.polygon(screen, LEAVES, [[x-50, 470], [x+90, 470], [x+20, 370]])
    pygame.draw.polygon(screen, LEAVES, [[x-40, 430], [x+80, 430], [x+20, 340]])

#Subprogram to get cloud positions
def getCloudPos(cloudList):

    #Assign the cloud positions in increments of 325
    for i in range(300, 1175, 325):
        x = i
        cloudList.append(x)

#Subprogram to draw clouds
def drawCloud(x):
    pygame.draw.ellipse(screen, WHITE, [x, 50, 125, 62.5])
    pygame.draw.ellipse(screen, WHITE, [x-60, 80, 125, 62.5])
    pygame.draw.ellipse(screen, WHITE, [x+50, 75, 125, 62.5])

#Arrow class
class Arrow():

    #Constructor that requires the arrow's position
    def __init__ (self, arrowPosition):
        self.position = arrowPosition

    #Subprogram to move the arrow
    def move(self):
        x = self.position[0]
        y = self.position[1]
        pygame.draw.polygon (screen, GRAYARROW, [[x, y+30], [x-5, y+27], [x-5, y+33]])
        pygame.draw.line (screen, BROWNARROW, [x,y+30],[x-21,y+30], 2)
        pygame.draw.polygon (screen, WHITE, [[x-20, y+30], [x-25, y+27], [x-35, y+27], [x-30, y+30], [x-35, y+33], [x-25, y+33]])
        self.position[0] += 5

#Cat class
class Cat():

    #Set defaults
    pos = [1200, 500]
    colour = ()
    speed = -0.5
    maxHealth = 1
    currentHealth = 1

    #Constructor that requires the cat's colour
    def __init__(self, newColour=(0, 0, 0)):
        self.colour = newColour

    #Subprogram to draw the Cat
    def draw(self):    
        x = self.pos[0]
        y = self.pos[1]
        barPercent = self.currentHealth/self.maxHealth
        barFill = barPercent*40
        pygame.draw.polygon(screen, CATGRAY, [[x,y], [x+5,y-8], [x+10, y], [x+20, y], [x+25, y-8], [x+30, y], [x+30, y+20], [x, y+20]])
        pygame.draw.polygon(screen, BLACK, [[x+13, y+11], [x+17, y+11], [x+15, y+14]])
        pygame.draw.ellipse(screen, BLACK, [x+5, y+10, 2, 2])
        pygame.draw.ellipse(screen, BLACK, [x+25, y+10, 2, 2])
        pygame.draw.rect(screen, self.colour, [x+6, y+20, 20, 25])
        pygame.draw.rect(screen, CATGRAY, [x+2, y+25, 5, 12])
        pygame.draw.rect(screen, CATGRAY, [x+25, y+25, 5, 12])
        pygame.draw.rect(screen, CATGRAY, [x+6, y+45, 9, 10])
        pygame.draw.rect(screen, CATGRAY, [x+17, y+45, 9, 10])

        #Draw health bar if the cat has any health left
        if barFill >= 0:
            pygame.draw.rect(screen, RED, [x-5, y-20, barFill, 10])
        pygame.draw.rect(screen, BLACK, [x-5, y-20, 40, 10], 2)

    #Subprogram to move the cats
    def move(self):
        self.pos[0] += self.speed

    #Subprogram to detect collisions with any other object
    def detectCollision(self, objectX, objectY, tolerance):
        result = False
        x = self.pos[0]
        y = self.pos[1]
        otherX = objectX
        otherY = objectY

        #Detect a collision if the distance between the other object and the cat is less than the provided tolerance
        if (abs(otherX-x) < tolerance and abs(otherY-y) < tolerance):
            result = True
            
        return result
    
#Subprogram to assign cat attributes and append them to the catList
def assignCatAttributes():
    assignAttributes = random.randint(0,3)
    singleCat = Cat(WHITE)
    singleCat.pos = [1200, random.randrange(500, 700)]
    singleCat.maxHealth = HEALTHLIST[assignAttributes]
    singleCat.currentHealth = singleCat.maxHealth
    singleCat.speed = SPEEDLIST[assignAttributes]
    singleCat.colour = CATCOLOURS[assignAttributes]
    catList.append(singleCat)

#Coin class
class Coin():

    #Constructor that requires the coin's position as an input
    def __init__ (self, position):
        self.pos = position

    #Subprogram to draw a coin
    def draw(self):
        x = self.pos[0]+13
        y = self.pos[1]+30
        pygame.draw.polygon (screen, LIGHTGOLD, [[x, y], [x+7, y+5], [x+7, y+14], [x, y+19], [x-7, y+14], [x-7, y+5]])
        pygame.draw.polygon (screen, GOLD, [[x, y+3], [x+4, y+8], [x+4, y+12], [x, y+16], [x-4, y+12], [x-4, y+8]])

    #Subprogram to detect collisions with any other object
    def detectCollision(self, otherObjectPos, tolerance):
        result = False
        x = self.pos[0]
        y = self.pos[1]
        otherX = otherObjectPos[0]
        otherY = otherObjectPos[1]

        #Detect a collision if the distance between the coin and the other object is less than the provided tolerance
        if (abs(otherX-x) < tolerance and abs(otherY-y) < tolerance):
            result = True
            
        return result

#Heart class
class Heart():

    #Constructor that requires the position of the heart
    def __init__ (self, position):
        self.pos = position

    #Subprogram to draw a heart
    def draw(self):
        x = self.pos[0]+12
        y = self.pos[1]+30
        pygame.draw.polygon (screen, HEART, [[x, y], [x+5, y-5], [x+10, y], [x, y+12], [x-10, y], [x-5, y-5]])

#Subprogram to draw the speech bubble
def drawSpeechBubble(x,y):
    pygame.draw.polygon (screen, WHITE, [[x,y], [x+50, y-25], [x+700, y-23], [x+700, y-300], [x+10, y-300], [x+10, y-25]])
    pygame.draw.polygon (screen, BLACK, [[x,y], [x+50, y-25], [x+700, y-23], [x+700, y-300], [x+10, y-300], [x+10, y-25]], 5)

#Subprogram to draw Robin's head in the introduction screen
def drawHead (x,y):
    pygame.draw.polygon(screen, ORANGE, [[x, y], [x-150, y-25], [x-200, y-100], [x-450, y], [x-400, y+175], [x-100, y+175]])
    pygame.draw.polygon (screen, BLACK, [[x, y], [x-50, y-7], [x-25, y+50]])
    pygame.draw.ellipse (screen, BLACK, [x-225, y-20, 25, 25])
    pygame.draw.polygon (screen, GREEN, [[x-150, y-120], [x-500, y+20], [x-450, y-150]])
    pygame.draw.polygon (screen, BURGUNDY, [[x-400, y-80], [x-425, y-70], [x-550, y-120], [x-525, y-150]]) 
    pygame.draw.rect (screen, GREEN,[x-350, y+175, 200, 300])

#Subprogram to draw the victory screen
def victoryScreen():
    congratsFont = pygame.font.SysFont('Arial', 60, True, False)
    congratulations1 = congratsFont.render("Congratulations! You saved the village from", True, BLACK)
    congratulations2 = congratsFont.render("the tax collectors and raised $1000 for them!", True, BLACK)
    x = 800
    y = 325
    screen.fill(SKY)
    pygame.draw.rect(screen, GROUND, [0, 550, 1200, 300]) 
    pygame.draw.polygon (screen, ORANGE, [[x, y], [x-100, y-25], [x-150, y-100], [x-350, y], [x-300, y+125], [x-50, y+125]])
    pygame.draw.polygon (screen, BLACK, [[x, y], [x-25, y-5], [x-10, y+25]])
    pygame.draw.lines (screen, BLACK, False, [[x-175, y], [x-150, y-25], [x-125, y]], 10)
    pygame.draw.polygon (screen, GREEN, [[x-75, y-100], [x-400, y+25], [x-350, y-125]])
    pygame.draw.polygon (screen, BURGUNDY, [[x-325, y-75], [x-340, y-60], [x-475, y-125], [x-425, y-150]]) 
    pygame.draw.polygon(screen, ORANGE, [[x-25, y+125], [x, y+165], [x-100,y+235], [x-100, y+175]])
    pygame.draw.polygon(screen, ORANGE, [[x-250, y+175], [x-250, y+230], [x-350,y+165], [x-325, y+125]])
    pygame.draw.rect (screen, GREEN,[x-250, y+125, 150, 200])
    pygame.draw.rect (screen, ORANGE, [x-245, y+325, 65, 70])
    pygame.draw.rect (screen, ORANGE, [x-170, y+325, 65, 70]) 
    screen.blit(congratulations1, [70, 25])
    screen.blit(congratulations2, [80, 100])
    screen.blit(restartText, [900, 200])
    
#Imports
import pygame
import random

#Define used colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LEAVES = (23, 64, 22)
WOOD = (120, 98, 32)
WALL = (222, 192, 102)
ROOF = (48, 42, 24)
WINDOW = (230, 255, 255)
SKY = (167, 249, 250)
GROUND = (158, 118, 65)
SUN = (255, 247, 10)
ORANGE = (205, 100, 5)
GREEN = (10, 70, 20)
BURGUNDY = (125, 5, 5)
CATGRAY= (200, 200, 200)
CATCOLOURS = [RED, BLUE, ORANGE, BLACK]
GRAYARROW = (100, 100, 100)
BROWNARROW = (125, 75, 50)
GOLD = (239, 205, 14)
LIGHTGOLD = (255, 239, 66)
HEART = (200, 30, 30)

#Health + Speed lists
HEALTHLIST = [1, 2, 3, 4]
SPEEDLIST = [-2, -1.5, -1, -0.5]

#Initialize pygame module
pygame.init()

#Set the screen and its caption
size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Robin Hood's Charity Challenge")

#Manage screen updates
clock = pygame.time.Clock()

#List of pre-game instructions
phrases = ["Prince John has raised the taxes again!", "The village people don't have enough.", "It is up to YOU to help them!", "Shoot the tax collectors with your love arrows...", "to fill them with generosity and kindness. ", "Gather the coins they give to you and earn...", "enough to help bring the village out of debt!", "Use the arrow keys to move...", "and use the spacebar to shoot arrows.", "Good luck!", ""]
change = 0 #Count how many instructions have been given

#Set control, animation, drawing, etc., variables

#Tree positions
treeList = []
getTreePos(treeList)

#Cloud positions
cloudList = []
getCloudPos(cloudList)

#Cat positions and attributes
catList = []
assignCatAttributes()

#Variables containing change to be done to Robin Hood's position
moveX = 0
moveY = 0

#List of coin objects
coinList = []

#List of heart objects
heartList = []

#List of arrow objects
arrows = []

#Village money
money = 500

#Main event loop (loop while the user hasn't clicked QUIT)
done = False
while not done:

    #Event processing loop
    for event in pygame.event.get():

        #User clicked QUIT
        if event.type == pygame.QUIT:
            done = True

        #User pressed a key down
        elif event.type == pygame.KEYDOWN:

            #Right arrow
            if event.key == pygame.K_RIGHT:
                moveX = 2

            #Left arrow
            elif event.key == pygame.K_LEFT:
                moveX = -2

            #Up arrow
            elif event.key == pygame.K_UP:
                moveY = -2

            #Down arrow
            elif event.key == pygame.K_DOWN:
                moveY = 2

            #Spacebar
            elif event.key == pygame.K_SPACE:
                if change == 10:
                    arrowX = robin.pos[0]
                    arrowY = robin.pos[1]
                    shotFired = Arrow([arrowX, arrowY])
                    arrows.append(shotFired)

            #Enter/Return
            elif event.key == pygame.K_RETURN:
                if change < 10:
                    change = change+1
                    text = font.render(phrases[0+change], True, BLACK)

            #Skip
            elif event.key == pygame.K_s:
                change = 10

            #Return
            elif event.key == pygame.K_r:

                #Reset all variables
                change = 0
                money = 500
                arrows = []
                catList = []
                coinList = []
                heartList = []

                #Assign new cat
                assignCatAttributes()

        #User released a key
        elif event.type == pygame.KEYUP:

            #Right or left keys
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                moveX = 0

            #Up or down keys
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                moveY = 0

    #Instructions screen

    #Draw background
    screen.fill(SKY)
    
    #Draw Robin's head
    drawHead(475, 400)

    #Draw speech bubble 
    drawSpeechBubble(475, 450)
    
    #Draw and change text every time enter is pressed
    font = pygame.font.SysFont('Arial', 35, True, False)
    skipFont = pygame.font.SysFont('Arial', 25, True, False)
    skip = skipFont.render("Press enter to continue or press S to skip", True, BLACK)
    text = font.render(phrases[0+change], True, BLACK)
    screen.blit(text, [500, 275])
    screen.blit(skip, [750, 425])

    #Monitor when instructions have finished
    if change == 10:
        
    #Game starts
        
    #Robin Hood controls
        robin = Robin()
        robin.move(moveX, moveY)
                
        #Clear screen then draw
        screen.fill(WHITE)

        #Draw ground
        pygame.draw.rect(screen, GROUND, [0, 500, 1200, 300])

        #Draw sky
        pygame.draw.rect(screen, SKY, [0, 0, 1200, 500])

        #Draw sun
        pygame.draw.circle(screen, SUN, [25, 50], 100)

        #Draw clouds
        for i in range(len(cloudList)):
            drawCloud(cloudList[i])

        #Draw trees
        for i in range(len(treeList)):
            drawTree(treeList[i])

        #Draw Robin Hood
        robin.draw()

        #Draw and move cats
        for oneCat in catList:
            oneCat.draw()
            oneCat.move()

            #Detect if the cat reached the village
            if oneCat.pos[0] == 300:
                catList.remove(oneCat)
                assignCatAttributes()

                #Deduct money if the player still has some
                if money > 0:
                    money -= 10

            #Detect if the cat has gone beyond the screen to the right
            elif oneCat.pos[0] > 1201:
                catList.remove(oneCat)

        #Remove hearts once they move off-screen
        for oneHeart in heartList:
            if oneHeart.pos[0] > 1200:
                heartList.remove(oneHeart)

        #Draw houses
        drawHouse(-100, 130)
        drawHouse(120, 100)
        drawHouse(10, 0)
        drawHouse(170, -80)
        drawHouse(-100, -120)
        
        #Fire all arrows
        for oneShotFired in arrows:
            oneShotFired.move()

            #Detect collisions with all cats
            for oneCat in catList:
                if oneCat.detectCollision(oneShotFired.position[0], oneShotFired.position[1], 10) == True:
                    
                    #Take health away from the cat hit
                    oneCat.currentHealth = oneCat.currentHealth - 1

                    #Remove arrow once collision is detected
                    oneShotFired.position[1] = -50

                    #Make cat turn around when its health is 0 and create two new cats
                    if oneCat.currentHealth == 0:
                        oneCat.speed = 3
                        assignCatAttributes()
                        assignCatAttributes()

                        #Regulate number of cats
                        if len(catList) > 20:
                                catList.remove(catList[-1])
                                
                        #Set up hearts
                        oneHeart = Heart(oneCat.pos)
                        heartList.append(oneHeart)

                        #Drop coins if the user still has money
                        #In losing screen player can still move and shoot
                        #But this ensures they don't get money back after they've lost
                        if money > 0:
                            oneCoin = Coin((oneCat.pos[0], oneCat.pos[1]))
                            coinList.append(oneCoin)

            #Delete arrow if moves off screen (if user missed)
            #A range of positions to ensure increments of where arrows are redrawn aren't a problem
            if oneShotFired.position[0] > 1200 and oneShotFired.position[0] < 1210:
                oneShotFired.position[1] = -50

        #Draw all coins            
        for oneCoin in coinList:
            oneCoin.draw()

            #Detect if Robin Hood has picked up a coin
            if oneCoin.detectCollision(robin.pos, 30) == True:
                coinList.remove(oneCoin)

                #Add money only if the player still has some
                #So they further can't get money back after they've lost
                if money > 0:
                    money += 10
                    
            #Detect if a cat has picked up a coin
            elif oneCoin.detectCollision(oneCat.pos, 50) == True:
                coinList.remove(oneCoin)

        #Money tracking

        #Text above bar
        moneyFont = pygame.font.SysFont("AR JULIAN", 25, True, False)
        moneyText = moneyFont.render("Village Money: $"+str(money), True, RED)
        screen.blit(moneyText, [60,250])

        #Actual bar
        percentage = float(money/1000)
        fill = 200*percentage
        pygame.draw.rect(screen, RED, [50, 300, fill, 50])
        pygame.draw.rect(screen, BLACK, [50, 300, 200, 50], 3)

        #Draw all hearts
        for oneHeart in heartList:
            oneHeart.draw()

        #Restart prompt
        if money >= 0:
            restartFont = pygame.font.SysFont("AR JULIAN", 30, True, False)
            restartText = restartFont.render("Press R to restart", True, RED)
            screen.blit(restartText, [900, 40])

        #End-game screen (with a win)
        if money >= 1000:
            catList = []
            coinList = []
            victoryScreen()

        #End-game screen (with a loss)
        if money == 0:
            endFont = pygame.font.SysFont("AR JULIAN", 50, True, False)
            endText = endFont.render("GAME OVER!", True, HEART)
            endText2 = endFont.render("YOU LET THE VILLAGE LOSE ALL OF ITS MONEY!", True, HEART)
            screen.blit(endText, [475, 400])
            screen.blit(endText2, [125, 450])
            
    #Flip screen
    pygame.display.flip()

    #Limit to 60 FPS
    clock.tick(60)
    
pygame.quit()
