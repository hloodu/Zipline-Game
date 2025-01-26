from tkinter import *
from math import * 
from time import *
from random import *

root = Tk()
s = Canvas(root, width = 800, height = 450, background = "#157F1F")

# INITIAL VARIABLES, FOR START OF ENTIRE GAME
def startGame():
  
  global play, playButtonText, titleAndResultText, detailsText, goal

  play = False            # show intro screen instead of immediately starting game
  goal = 10               # set amount of coins to collect in first level

  # text to show in intro screen
  titleAndResultText = "ZIPLINE TWIRLY-WHIRL"
  detailsText = "Collect " + str(goal) + " coins to win.\n Avoid birds by using the up or right arrow keys to flip the zipliner!"
  playButtonText = "Start"


# SET INITIAL VALUES
def setInitialValues():
  
  # gameplay variables
  global score, time, play, frame, lives, flip, exitScreen
  
  flip, exitScreen = False, False
  lives = 3
  score, time, frame = 0, 0, 0

  # intro screen setup
  global titleAndResultX, titleAndResultY
  global playButtonX1, playButtonX2, playButtonY1, playButtonY2
  global detailsX, detailsY

  titleAndResultX, titleAndResultY = 400, 100
  playButtonX1, playButtonY1 = 150, 175
  playButtonX2, playButtonY2 = 650, 275
  detailsX, detailsY = 400, 350

  # score/livesboard
  global scoreBoardFill, livesBoardFill
  
  scoreBoardFill = "#4CB963"
  livesBoardFill = "#4CB963"

  # background (during play) setup
  global forestX, forestYConstant, forestY, forestList, forestColor
  
  forestX, forestYConstant, forestY = [], [], []
  forestList, forestColor = [], []

  for f in range(randint(4, 20)):        # fill forest/background arrays
    forestX.append(randint(-10, 800))
    forestYConstant.append(randint(-10, 450))
    forestY.append(0.08125 * forestX[f] + forestYConstant[f])
    forestList.append("")
    forestColor.append(choice(["#147A1E", "#126F1B"]))

  # person
  global personX, personY, personImageList, imageNumber
  
  personX = 120
  personY = 0.08125 * personX + 137
  personImageList = []
  imageNumber = 0

  for i in range(72):          # import images of person
    personImageList.append(PhotoImage(file = "zipline swing/" + str(i) + ".png"))

  # coins
  global coinX, coinY, coinList, coinFill, coinOutline, coinMinLocation, totalCoins

  coinX, coinY, coinList = [], [], []
  coinFill, coinOutline = [], []
  coinMinLocation = 800

  for i in range( 300 ):       # fill coin arrays with 300 coins
    coinX.append(randint(coinMinLocation, coinMinLocation + 100))
    coinY.append(0.08125 * coinX[i] + 155)
    coinList.append("")
    coinFill.append("#FDEB0C")
    coinOutline.append("#FACD1D")
    coinMinLocation = coinX[i] + randint(50, 200)

  # zipline and hook
  global ziplineX2, ziplineY2, hookX, hookY
  
  ziplineX2 = 2000
  ziplineY2 = 0.08125 * ziplineX2 + 150
  hookX, hookY = 113, 140

  # bird
  global birdX, birdY, birdBody, birdWing, birdMinLocation, birdsAlreadyHit

  birdX, birdY, birdBody, birdWing, birdsAlreadyHit = [], [], [], [], []
  birdMinLocation = 1000

  birdNumber = 0        # use a local variable to reference the newest bird, since a 'while' loop is used instead of 'for'
  while birdMinLocation < (coinX[-1]):        # fill bird arrays. use a 'while' loop to add birds until there are no coins nearby
    birdX.append(randint(birdMinLocation, birdMinLocation + 200))

    for b in range(len(coinX)):              # adjust to avoid overlap with coins
      while birdX[birdNumber] in range(coinX[b] - 40, coinX[b] + 30):
        birdX[birdNumber] = birdX[birdNumber] + 1

    # fill remaining arrays
    birdY.append(0.08125 * birdX[birdNumber] + 156)
    birdBody.append("")
    birdWing.append("")
    
    birdMinLocation = birdX[birdNumber] + randint(600, 800)             # minimum distance for the next bird to be located
    birdNumber = birdNumber + 1          # move to next bird in array for next repeat


# INTRO SCREEN
def introScreen():
  
  # play button
  global startWord, playButtonX1, playButtonX2, playButtonY1, playButtonY2, playButtonText, playButton

  playButton = s.create_rectangle(playButtonX1, playButtonY1, playButtonX2, playButtonY2, fill = "#4CB963", outline = "")       # button background
  startWord = s.create_text((playButtonX2 + playButtonX1) / 2, (playButtonY2 + playButtonY1) / 2, text = playButtonText, fill = "#04080F", font = "Georgia 30")      # word printed

  # title/results from previous level
  global titleAndResultX, titleAndResultY, titleAndResultText, titleAndResult
  
  titleAndResult = s.create_text(titleAndResultX, titleAndResultY, text = titleAndResultText, fill = "#04080F", font = "Georgia 18")   

  # details on next level and instructions
  global detailsText, detailsX, detailsY, details

  details = s.create_text(detailsX, detailsY, text = detailsText, fill = "#04080F", font = "Georgia 14", width = 600, justify = CENTER) 

  
# DRAW ITEMS 
def drawObjects():

  # background/forest
  global forestList, forestX, forestY, forestColor
  
  for f in range(len(forestList)):
    forestList[f] = s.create_polygon(forestX[f], forestY[f], forestX[f] + 5, forestY[f] + 5, forestX[f] + 10, forestY[f] + 5, forestX[f] + 15, forestY[f] + 0, forestX[f] + 20, forestY[f] + 5, forestX[f] + 25, forestY[f] + 5, forestX[f] + 30, forestY[f] + 0, forestX[f] + 35, forestY[f] + 5, forestX[f] + 40, forestY[f] + 5, forestX[f] + 45, forestY[f] + 0, forestX[f] + 50, forestY[f] + 5, forestX[f] + 55, forestY[f] + 5, forestX[f] + 60, forestY[f] + 0, forestX[f] + 65, forestY[f] + 5, forestX[f] + 70, forestY[f] + 5, forestX[f] + 75, forestY[f] + 0, forestX[f] + 80, forestY[f] + 5, forestX[f] + 85, forestY[f] + 5, forestX[f] + 90, forestY[f] + 0, forestX[f] + 90, forestY[f] + 5, forestX[f] + 85, forestY[f] + 10, forestX[f] + 80, forestY[f] + 10, forestX[f] + 75, forestY[f] + 5, forestX[f] + 70, forestY[f] + 10, forestX[f] + 65, forestY[f] + 10, forestX[f] + 60, forestY[f] + 5, forestX[f] + 55, forestY[f] + 10, forestX[f] + 50, forestY[f] + 10, forestX[f] + 45, forestY[f] + 5, forestX[f] + 40, forestY[f] + 10, forestX[f] + 35, forestY[f] + 10, forestX[f] + 30, forestY[f] + 5, forestX[f] + 25, forestY[f] + 10, forestX[f] + 20, forestY[f] + 10, forestX[f] + 15, forestY[f] + 5, forestX[f] + 10, forestY[f] + 10, forestX[f] + 5, forestY[f] + 10, forestX[f] + 0, forestY[f] + 5, fill = forestColor[f])
  
  # zipline
  global zipline, zipLineX2, ziplineY2
  
  zipline = s.create_line(0, 135, ziplineX2, ziplineY2, fill = "#04080F")

  # coins
  global coinList, coinX, coinY, coinFill, coinOutline
  
  for c in range(0, len(coinList)):          # draw all coins...
    if coinX[c] in range(-50, 850):          # ...that are on the screen...
      coinList[c] = s.create_oval(coinX[c], coinY[c], coinX[c] + 18, coinY[c] + 20, fill = coinFill[c], outline = coinOutline[c], width = 5)

    else:           # ...if they're not, do not draw, to prevent slowing!
      coinList[c] = ""

  # birds
  global birdBody, birdWing, birdX, birdY

  for b in range(0, len(birdBody)):       # draw all birds...
    if birdX[b] in range(-50, 850):       # ...that are on the screen...
      birdBody[b] = s.create_polygon(birdX[b], birdY[b] + 5, birdX[b] + 5, birdY[b], birdX[b] + 15, birdY[b] + 10, birdX[b] + 25, birdY[b] + 15, birdX[b] + 30, birdY[b] + 15, birdX[b] + 45, birdY[b] + 10, birdX[b] + 45, birdY[b] + 15, birdX[b] + 30, birdY[b] + 20, birdX[b] + 25, birdY[b] + 25, birdX[b] + 15, birdY[b] + 27.5, birdX[b] + 5.2, birdY[b] + 24.5, birdX[b] + 2.5, birdY[b] + 15, birdX[b] + 2.5, birdY[b] + 10, fill = "#A0EADE")

      birdWing[b] = s.create_polygon(birdX[b] + 40, birdY[b], birdX[b] + 35, birdY[b] + 10, birdX[b] + 27.5, birdY[b] + 15.5, birdX[b] + 20, birdY[b] + 20, birdX[b] + 15, birdY[b] + 15, birdX[b] + 22.5, birdY[b] + 7.5, birdX[b] + 30, birdY[b] + 5, fill = "#3587A4")

    else:               # ...if they're not, do not draw. prevents slowing!
      birdBody[b], birdWing[b] = "", ""

  # person
  global person, personImageList, personX, personY, imageNumber
  
  person = s.create_image(personX, personY, image = personImageList[imageNumber])

  # hook
  global hookX, hookY, hook
  
  hook = s.create_oval(hookX, hookY, hookX + 16, hookY + 11, fill = "#527977", outline = "#527977", width = 2)

  # scoreboard and lives count
  global score, scoreBoardText, scoreBoardFill, scoreBoardBackground, scoreBoardCoin
  global lives, livesBoardText, lovesBoardFill, livesBoardBackground, livesBoardHeart

  scoreBoardBackground = s.create_rectangle(550, 25, 650, 75, fill = scoreBoardFill, outline = "")
  livesBoardBackground = s.create_rectangle(675, 25, 775, 75, fill = livesBoardFill, outline = "")

  heartX, heartY = 725, 35      # anohor points for heart at top of screen
  scoreBoardCoin = s.create_oval(620, 40, 638, 60, fill = "#FDEB0C", outline = "#FACD1D", width = 5)
  livesBoardHeart = s.create_polygon(heartX + 5, heartY, heartX + 15, heartY, heartX + 20, heartY + 10, heartX + 25, heartY, heartX + 35, heartY, heartX + 40, heartY + 10, heartX + 35, heartY + 20, heartX + 20, heartY + 30, heartX + 5, heartY + 20, heartX, heartY + 10, fill = "#F9564F", outline = "#EAA381", width = 3)

  scoreBoardText = s.create_text(555, 50, text = str(score) + "/" + str(goal), fill = "#04080F", font = "Georgia 15", anchor = "w")
  livesBoardText = s.create_text(680, 50, text = str(lives) + "/3", fill = "#04080F", font = "Georgia 15", anchor = "w")

  
# UPDATE SCREEN
def updateObjects():

  # change person image if flipping, unless game has been lost and person is falling
  global imageNumber, flip, lives
  
  if flip == True and lives != 0:
    if imageNumber == 71:      # if in final image...
      imageNumber = 0          # ...flip has been finished, so reset to image 0...
      flip = False             # ...and stop flipping
      
    else:                      # otherwise, switch to next image in cycle
        imageNumber = imageNumber + 1

  # if game is over, move person accordingly, and remove birds and coins
  global exitScreen, livesBoardFill, score, goal, scoreBoardFill
  global personX, personY, hookX, hookY
  
  if exitScreen == True:
    if lives == 0:          # if player has lost, fall out of frame
      livesBoardFill = "#F9564F"
      personY = personY + 5

    elif score == goal:     # if player has won, slide down the zipline and out of screen
      scoreBoardFill = "#3587A4"
      personX = personX + 6
      personY = 0.08125 * personX + 137
      hookX = hookX + 6
      hookY = 0.08125 * hookX + 137

    global coinX, birdX
    for c in range(len(coinX)):      # remove coins by drawing them out of frame
      coinX[c] = 1000

    for b in range(len(birdX)):      # remove birds by drawing them out of frame
      birdX[b] = 1000

    if personX > 900 or personY > 550:        # if person has left screen, stop pushing them further out
      exitScreen = False

  else:
    global forestX, forestYConstant      # update forest/background
    for f in range(len(forestX)):
      if forestX[f] + 100 <= 0:      # if the object is off screen, send it back to cycle through ahain
        forestX[f] = 805

      else:                          # otherwise, continue moving down screen
        forestX[f] = forestX[f] - 5

      forestY[f] = 0.08125 * forestX[f] + forestYConstant[f]          # adjust y value based on x value

      
    global coinY        # update coins. coinX has already been called
    for c in range(len(coinX)):
      coinX[c] = coinX[c] - 8
      coinY[c] = 0.08125 * coinX[c] + 160
  
    global birdY        # update birds. birdX has already been called
    for b in range(len(birdX)):
      birdX[b] = birdX[b] - 8
      birdY[b] = 0.08125 * birdX[b] + 160
  
    pickUpCoin()    # check if coin is collected
    hitBird()       # check if bird has been hit
    winOrLose()     # check if game has been won


# DELETING LIST ITEMS
def deleteIndexItems():
  
  global coinList      # delete coins
  
  for c in range (len(coinList)):
    s.delete(coinList[c])

  global birdBody, birdWing        # delete birds
  
  for b in range(len(birdBody)):
    s.delete(birdBody[b])
    s.delete(birdWing[b])

  global forestList          # delete background
  
  for f in range(len(forestList)):
    s.delete(forestList[f])


# IF KEYS ARE PRESSED
def keyDownHandler( event ):
  
  global flip            #   # if right or up keys are pressed, make zipliner flip
  
  if event.keysym == "Right" or event.keysym == "Up":
    flip = True


# IF MOUSE IS CLICKED
def mouseClickHandler( event ):
  
  global play, playButtonX1, playButtonX2, playButtonY1, playButtonY2

  xMouse = event.x      # get mouse x value
  yMouse = event.y      # get mouse y value

  if play == False:     # check if intro screen is on
    if xMouse in range (playButtonX1, playButtonX2) and yMouse in range (playButtonY1, playButtonY2):          # start game if area under "start"/"restart"/"next level" button is pressed
      play = True


# PICK UP COIN?
def pickUpCoin():
  
  global score, coinX, coinFill, coinOutline, personX, imageNumber

  for c in range(len(coinList)):
    # coin being picked up depends on its location and which person image is shown (only pick up coin if it's 'touching' the person) 
    if coinX[c] in range(112, 129) and imageNumber in [0, 1, 1, 3, 68, 69, 70, 71]   or   coinX[c] in range(129, 160) and imageNumber in range(0, 8)   or   coinX[c] in range(160, 192) and imageNumber in range(4, 16)   or   coinX[c] in range(48, 64) and imageNumber in range(45, 60)   or    coinX[c] in range(64, 80) and imageNumber in range(56, 64)   or       coinX[c] in range(80, 96) and imageNumber in range(60, 68)   or   coinX[c] in range(96, 112) and imageNumber in range(64, 72):  # as long as the coin is in the person's range...
      if coinFill[c] != "":        # ...and hasn't been picked up (is visible)...
        score = score + 1          # ...increase the score...
        coinFill[c] = ""           # ...and make it invisible!
        coinOutline[c] = ""

        
# HIT BIRD?
def hitBird():
  
  global lives, birdsAlreadyHit, imageNumber, birdX

  for b in range(len(birdX)):
    # bird being hit depends on its location and which person image is shown (bird is only hit if it's 'touching' the person). since birds do not disappear (made invisible) after being hit, use variable "birdsAlreadyHit" to keep track of birds that have been hit
    if birdX[b] in range(112, 129) and imageNumber in [0, 1, 1, 3, 68, 69, 70, 71]   or   birdX[b] in range(129, 160) and imageNumber in range(0, 8)   or   birdX[b] in range(160, 192) and imageNumber in range(4, 20)   or    birdX[b] in range(64, 80) and imageNumber in range(56, 64)   or   birdX[b] in range(80, 96) and imageNumber in range(60, 68)   or   birdX[b] in range(96, 112) and imageNumber in range(64, 72): # as long as the bird is in the person's range...
      if b not in birdsAlreadyHit:      #...and hasn't already been hit...
        lives = lives - 1               # ...lose a life...
        birdsAlreadyHit.append(b)       # ...and record it as having been hit!


# HAS GAME BEEN WON OR LOST?
def winOrLose():
  
  global lives, play, score, totalCoins, playButtonText, detailsText, bird, goal, titleAndResultText, personX, personY, exitScreen

  # lose game?
  if lives <= 0:
    exitScreen = True      # play ending animation
    
    if personX >= 900 or personY >= 550:        # change starting information to allow player to retry
      play = False
      titleAndResultText = "You lose :("
      playButtonText = "RESTART LEVEL"

  # win game?
  elif score >= goal:
    exitScreen = True     # play ending animation
    
    if personX >= 900 or personY >= 550:      # change starting screen to give information on next level
      play = False

      if goal > 99:                # if goal of 100 points has been reached, reset game 
        titleAndResultText = "You collected " + str(goal) + " coins. You've beat the final level!!"
        playButtonText = "BACK TO LEVEL 1"
        goal = 10

      else:                        # otherwise, move to next level
        titleAndResultText = "You collected " + str(goal) + " coins. You win!!"
        playButtonText = "NEXT LEVEL"
        goal = round(goal * 1.2)        # increase goal
        
        if goal > 99:        # final level = 100 points
          goal = 100

      detailsText = "Collect " + str(goal) + " coins to win.\nAvoid birds by using the up or right arrow keys to flip the zipliner!"      # change information according to next level

  # end level if all coins have passed
  elif coinX[-1] < -50:
    play = False
    titleAndResultText = "The forest ran out of coins to give you."
    playButtonText = "RESTART LEVEL"


# END GAME
def endGame():
  
  print("GAME OVER.")
  

# RUN GAME!
def runGame():  
  
  global play, zipline, person, scoreboardText, hook, livesBoardText, scoreBoardBackground, livesBoardBackground, scoreBoardCoin, livesBoardHeart

  # set variables for very first round
  startGame()

  # play game!
  while True:
    if play == False:
      setInitialValues()        # set variables
      introScreen()             # show intro screen

      s.update()
      sleep(0.03)
      s.delete(playButton, startWord, titleAndResult, details)        # delete relevant items

    elif play == True:
      drawObjects()              # draw game objects
      
      s.update()
      sleep(0.03)
      s.delete(zipline, person, scoreBoardText, hook, livesBoardText, scoreBoardBackground, livesBoardBackground, scoreBoardCoin, livesBoardHeart)       # delete relevant items     
      deleteIndexItems()          # delete list items
      
      updateObjects()            # update items
  
  endGame()


root.after( 0, runGame )

s.bind( "<Button-1>", mouseClickHandler )
s.bind( "<Key>", keyDownHandler )

s.pack()
s.focus_set()
root.mainloop()