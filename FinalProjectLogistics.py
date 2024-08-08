#FinalProjectLogistics.py

from Graphics import *
from random import *

#################
# Miscellaneous #
#################

def TitleScreen():
   setColor("red")
   fillRectangle(0,0,1300,700)
   setColor("Lime green")
   fillRectangle(550,400,750,475)
   setColor("Black")
   drawString("DOMBOX",500,300,"Arial",56,"bold&italic")
   drawString("By: Brooks, Dominic, and Drew",400,335,"Arial",30,"normal")
   drawString("START",560,470,"Arial",40,"bold")
   onscreenclick(titleScreenMouseEvents,btn=1)

def titleScreenMouseEvents(x,y):
   global startPressed
   if inside(x,y,550,400,750,475):
      startPressed = True
      drawInventory()
      drawExitWall()

def keyVariables():
   global bookshelfOpen
   global blueKey
   global redKey
   global crowbar
   global blueKeyUsed
   global redKeyUsed
   global crowbarUsed
   global inventorySpot
   global colorMatrix
   global correctColorMatrix
   global safeOpen
   global exitSafeOpen
   global safeMatrix
   global correctSafeMatrix
   safeMatrix = []
   correctSafeMatrix = ["4","1","3"]
   exitSafeOpen = False
   safeOpen = False
   bookshelfOpen = False
   blueKey = False
   redKey = False
   crowbar = False
   blueKeyUsed = False
   redKeyUsed = False
   crowbarUsed = False
   inventorySpot = [450,550,650]
   colorMatrix = []
   correctColorMatrix = ["Y","R","G","G","B","Y"]

def drawArrows():
   setColor("red")
   fillPolygon([0,350,25,330,25,340,80,340,80,360,25,360,25,370])
   fillPolygon([1300,350,1275,330,1275,340,1220,340,1220,360,1275,360,1275,370])
   setColor("black")
   drawPolygon([0,350,25,330,25,340,80,340,80,360,25,360,25,370])
   drawPolygon([1300,350,1275,330,1275,340,1220,340,1220,360,1275,360,1275,370])

def drawInventory():
   setColor("gray")
   fillRectangle(400,20,900,120)
   setColor("black")
   drawRectangle(400,20,900,120)
   global inventorySpot
   for x in range(500,901,100):
      drawLine(x,20,x,120)
   z=0
   if blueKey == True:
      setColor("blue")
      width(4)
      drawCircle(inventorySpot[z]-10,70,6)
      drawLine(inventorySpot[z]-5,70,inventorySpot[z]+15,70)
      drawLine(inventorySpot[z]+15,70,inventorySpot[z]+15,74)
      drawLine(inventorySpot[z]+8,70,inventorySpot[z]+8,76)
      width(1)
      z+=1
   if crowbar == True:
      setColor("maroon")
      width(3)
      drawLine(inventorySpot[z],44,inventorySpot[z],101)
      setColor("silver")
      drawLine(inventorySpot[z]-7,47,inventorySpot[z],44)
      drawLine(inventorySpot[z],104,inventorySpot[z]+7,101)
      width(1)
      z+=1
   if redKey == True:
      setColor("red")
      width(4)
      drawCircle(inventorySpot[z]-10,70,6)
      drawLine(inventorySpot[z]-5,70,inventorySpot[z]+15,70)
      drawLine(inventorySpot[z]+3,70,inventorySpot[z]+3,75)
      drawLine(inventorySpot[z]+13,70,inventorySpot[z]+13,72)
      drawLine(inventorySpot[z]+18,70,inventorySpot[z]+18,78)
      width(1)
      update()
      z+=1

#############
# Exit Wall #
#############

def drawExitWall():
   setBackground(245,245,220)
   setColor("black")
   drawLine(100,0,100,600)
   drawLine(100,600,1200,600)
   drawLine(1200,600,1300,700)
   drawLine(100,600,0,700)
   drawLine(1200,0,1200,600)
   drawExitDoor(blueKeyUsed,redKeyUsed,crowbarUsed)
   drawTable(blueKey)
   drawExitSafe()
   drawFloor(1)
   drawArrows()
   onscreenclick(displayExitWallMouseEvents,btn=1)
   drawInventory()

def drawExitDoor(b,r,c):
   setColor("brown")
   fillRectangle(425,250,625,600)
   fillArc(525,250,100,75,270,90)
   setColor("gold")
   fillCircle(600,410,12)
   setColor("black")
   drawLine(425,250,425,600)
   drawLine(625,250,625,600)
   drawArc(525,250,100,75,270,90)
   drawCircle(600,410,12)
   if b == False:
      setColor("blue")
      fillRegularPolygon(600,443,16,4)
      setColor("gray")
      width(3)
      drawArc(600,428,8,18,270,90)
      width(1)
      setColor("gold")
      fillCircle(600,410,12)
      setColor("black")
      drawRegularPolygon(600,443,16,4)
      fillCircle(600,440,3)
      fillRectangle(599,443,601,449)
      drawCircle(600,410,12)
   else:
      pass
   if r == False:
      setColor("gold")
      fillRectangle(592,274,612,280)
      fillRectangle(630,270,634,280)
      setColor("black")
      drawRectangle(592,274,612,280)
      drawRectangle(630,270,634,280)
      setColor("silver")
      width(2)
      x = 605
      for y in range(280,293,3):
         x += 3
         drawCircle(x,y,2)
      for y in range(293,279,-3):
         drawCircle(x,y,2)
         x += 3
      width(1)
      setColor("red")
      fillRegularPolygon(622,317,16,4)
      setColor("gray")
      width(3)
      drawArc(622,307,8,18,270,80)
      width(1)
      setColor("black")
      drawRegularPolygon(622,317,16,4)
      fillCircle(622,314,3)
      fillRectangle(621,317,623,323)
   else:
      pass
   if c == False:
      setColor(92,64,51)
      fillRectangle(400,365,650,390)
      setColor("silver")
      fillCircle(409,372,2)
      fillCircle(409,384,2)
      fillCircle(641,372,2)
      fillCircle(641,384,2)
   if c == True and r == True and b == True:
      setColor("brown")
      fillRectangle(425-200,250,625-200,600)
      fillArc(525-200,250,100,75,270,90)
      setColor("skyblue")
      fillRectangle(425,250,625,600)
      fillArc(525,250,100,75,270,90)
      setColor("black")
      drawLine(425-200,250,425-200,600)
      drawLine(625-200,250,625-200,600)
      drawArc(525-200,250,100,75,270,90)
      setColor("dark green")
      fillRectangle(425,420,625,600)
      setColor("grey")
      fillPolygon([425,600,625,600,540,420,510,420])
      setColor("black")
      drawPolygon([425,600,625,600,540,420,510,420])
      drawRectangle(425,420,625,600)
      drawLine(425,250,425,600)
      drawLine(625,250,625,600)
      drawArc(525,250,100,75,270,90)

def drawTable(k):
   setColor("brown")
   fillRectangle(850,450,950,525)
   if k == False:
      setColor("blue")
      width(4)
      drawCircle(885,488,6)
      drawLine(890,488,910,488)
      drawLine(910,488,910,492)
      drawLine(903,488,903,494)
      width(1)
      setColor("black")

def drawExitSafe():
   if exitSafeOpen == False:
      setColor("silver")
      fillRectangle(850,450,950,525)
      setColor("black")
      drawRectangle(850,450,950,525)
      setColor("white")
      fillRectangle(880,460,920,515)
      setColor("black")
      fillRectangle(885,465,915,475)
      setColor("grey")
      for x in range(891,917,9):
         for y in range(483,519,9):
            drawPoint(x,y)
      fillRectangle(932,465,940,510)
   else:
      setColor("silver")
      fillRectangle(840,450,850,525)
      setColor("grey")
      width(3)
      drawArc(840,488,8,25,180,360)
      width(1)

def exitSafeMouseEvents(x,y):
   global safeMatrix
   setColor("white")
   if inside(x,y,1100,20,1120,40):
      drawExitWall()
   elif inside(x,y,500,205,555,260):
      safeMatrix += "1"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,625,205,680,260):
      safeMatrix += "2"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,750,205,850,260):
      safeMatrix += "3"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
      if safeMatrix == correctSafeMatrix:
         global exitSafeOpen
         exitSafeOpen = True
         drawExitWall()
   elif inside(x,y,500,330,555,385):
      safeMatrix += "4"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,625,330,680,385):
      safeMatrix += "5"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,750,330,850,385):
      safeMatrix += "6"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,500,455,555,510):
      safeMatrix += "7"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,625,455,680,510):
      safeMatrix += "8"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,750,455,850,510):
      safeMatrix += "9"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,625,580,680,635):
      safeMatrix += "0"
      drawString(safeMatrix,455,145,"Arial",60,"bold")
   elif inside(x,y,750,580,850,635):
      safeMatrix = []
      clear()
      drawBigExitSafe()
      drawString(safeMatrix,455,145,"Arial",60,"bold")

def drawBigExitSafe():
   clear()
   setBackground(245,245,220)
   setColor('silver')
   fillRectangle(90,0,1210,700)
   setColor('white')
   fillRectangle(400,10,900,690)
   setColor('grey')
   fillRectangle(1010,100,1110,600)
   setColor("black")
   fillRectangle(450,50,850,150)
   setColor("grey")
   for x in range(515,801,125):
      for y in range(220,600,125):
         setColor("grey")
         fillRectangle(x-15,y-15,x+40,y+40)
   setColor("black")
   drawString("1",520,250,"Arial",20,"bold")
   drawString("2",645,250,"Arial",20,"bold")
   drawString("3",770,250,"Arial",20,"bold")
   drawString("4",520,375,"Arial",20,"bold")
   drawString("5",645,375,"Arial",20,"bold")
   drawString("6",770,375,"Arial",20,"bold")
   drawString("7",520,500,"Arial",20,"bold")
   drawString("8",645,500,"Arial",20,"bold")
   drawString("9",770,500,"Arial",20,"bold")
   setColor("green")
   drawString("O",520,625,"Arial",20,"bold")
   setColor("black")
   drawString("0",645,625,"Arial",20,"bold")
   setColor("red")
   drawString("X",770,625,"Arial",20,"bold")
   width(2)
   setColor("red")
   drawLine(1100,20,1120,40)
   drawLine(1100,40,1120,20)
   width(1)
   setColor("black")
   onscreenclick(exitSafeMouseEvents,btn=1)

def drawEnd():
   clear()
   setBackground("black")
   setColor("white")
   drawString("Congratulations! You escaped the room.",280,325,"Arial",30,"bold")

def displayExitWallMouseEvents(x,y):
   if inside(x,y,882,480,911,492) and exitSafeOpen == True:
      drawTable(1)
      global blueKey
      blueKey = True
      drawInventory()
      update()
   elif inside(x,y,592,435,608,451) and blueKey == True:
      global blueKeyUsed
      blueKeyUsed = True
      drawExitWall()
   elif inside(x,y,0,325,100,375):
      drawWestWall()
   elif inside(x,y,1200,325,1300,375):
      drawEastWall()
   elif inside(x,y,400,365,650,390) and crowbar == True:
      global crowbarUsed
      crowbarUsed = True
      drawExitWall()
   elif inside(x,y,612,305,632,325) and redKey == True:
      global redKeyUsed
      redKeyUsed = True
      drawExitWall()
   elif inside(x,y,425,175,624,600) and blueKeyUsed == True and crowbarUsed == True and redKeyUsed == True:
      drawEnd()
   elif inside(x,y,880,460,920,515) and exitSafeOpen == False:
      drawBigExitSafe()

#############
# East Wall #
#############

def drawCrowbar(k):
   width(8)
   setColor("Maroon")
   drawLine(620,290,620,490)
   setColor("Gray")
   drawLine(600,300,620,290)
   drawLine(620,490,640,500)
   width(1)
   setColor(190,174,150)
   fillRectangle(615,385,625,390)
   if crowbar == True:
      setBackground(245,245,220)
      setColor("black")
      drawArrows()
      drawInventory()
      setColor(245,245,220)
      fillRectangle(750,200,1050,600)
      setColor("Black")
      drawRectangle(750,200,1050,600)
      setColor("Brown")
      fillRectangle(450,200,750,600)
      setColor(190,174,150)
      fillRectangle(615,385,625,390)
      setColor("black")
      drawLine(100,0,100,600)
      drawLine(100,600,1200,600)
      drawLine(1200,600,1300,700)
      drawLine(100,600,0,700)
      drawLine(1200,0,1200,600)
      drawArrows()
      drawFloor(2)
      setColor("white")
      fillRectangle(800,250,950,450)
      setColor("Black")
      drawString(" _ _ 3 ",812,375,"Arial",40,"normal")

def drawBookshelf(k):
   setColor("brown")
   fillRectangle(750,200,1050,600)
   x9 = 765
   y9 = 210
   y9 -= 90
   x10 = 785
   y10 = 290
   y10 -= 90
   seed(69420)
   for y in range(4):
      x9 = 765
      x10 = 785
      y9 += 90
      y10 += 90
      for k in range(11):
         r = randint(175,255)
         g = randint(30,60)
         b = randint(30,60)
         setColor(r,g,b)
         fillRectangle(x9,y9,x10,y10)
         x9 += 25
         x10 += 25
   setColor("dark red")
   fillRectangle(790,390,810,470)
   if bookshelfOpen == True:
      clear()
      setBackground(245,245,220)
      setColor("black")
      drawLine(100,0,100,600)
      drawLine(100,600,1200,600)
      drawLine(1200,600,1300,700)
      drawLine(100,600,0,700)
      drawLine(1200,0,1200,600)
      drawArrows()
      drawInventory()
      setColor(245,245,220)
      fillRectangle(750,200,1050,600)
      setColor("Black")
      drawRectangle(750,200,1050,600)
      setColor("Brown")
      fillRectangle(450,200,750,600)
      setColor("white")
      fillRectangle(800,250,950,450)
      setColor("Black")
      drawString(" _ _ 3 ",812,375,"Arial",40,"normal")
      drawCrowbar(1)
      drawFloor(2)

def drawEastWall():
   clear()
   setBackground(245,245,220)
   setColor("black")
   drawLine(100,0,100,600)
   drawLine(100,600,1200,600)
   drawLine(1200,600,1300,700)
   drawLine(100,600,0,700)
   drawLine(1200,0,1200,600)
   drawArrows()
   drawBookshelf(1)
   drawFloor(2)
   drawInventory()
   onscreenclick(displayEastWallMouseEvents,btn=1)

def displayEastWallMouseEvents(x,y):
   if inside(x,y,0,325,100,375):
      drawExitWall()
   elif inside(x,y,1200,325,1300,375):
      drawSouthWall()
   elif inside(x,y,790,390,810,470):
      global bookshelfOpen
      bookshelfOpen = True
      drawBookshelf(1)
   elif inside(x,y,600,290,640,500) and bookshelfOpen == True:
      global crowbar
      crowbar = True
      drawBookshelf(1)

#############
# West Wall #
#############

def drawWestDots():
   setColor("black")
   fillCircle(125,130,6)
   fillCircle(125,150,6)
   fillCircle(145,130,6)
   fillCircle(145,150,6)
   fillCircle(135,165,6)
   fillCircle(400,300,6)
   fillCircle(400,320,6)
   fillCircle(410,310,6)
   fillCircle(1100,120,6)
   fillCircle(1080,120,6)
   fillCircle(1090,130,6)
   fillCircle(1090,110,6)
   fillCircle(500,575,6)
   fillCircle(720,130,6)
   fillCircle(700,130,6)
   fillCircle(720,150,6)
   fillCircle(700,150,6)
   fillCircle(690,140,6)
   fillCircle(730,140,6)
   fillCircle(950,430,6)
   fillCircle(960,440,6)
   setColor("blue")
   fillCircle(125,130,5)
   fillCircle(125,150,5)
   fillCircle(145,130,5)
   fillCircle(145,150,5)
   fillCircle(135,165,5)
   setColor("green")
   fillCircle(400,300,5)
   fillCircle(400,320,5)
   fillCircle(410,310,5)
   fillCircle(1100,120,5)
   fillCircle(1080,120,5)
   fillCircle(1090,130,5)
   fillCircle(1090,110,5)
   setColor("yellow")
   fillCircle(500,575,5)
   fillCircle(720,130,5)
   fillCircle(700,130,5)
   fillCircle(720,150,5)
   fillCircle(700,150,5)
   fillCircle(690,140,5)
   fillCircle(730,140,5)
   setColor("red")
   fillCircle(950,430,5)
   fillCircle(960,440,5)
   
def drawWestPuzzle():
   setColor("red")
   fillRegularPolygon(820,200,15,3)
   setColor("green")
   fillCircle(850,200,15)
   setColor("yellow")
   fillStar(820,230,15,5)
   setColor("blue")
   fillRegularPolygon(850,230,15,4)

def resetDoorMatrix():
   doorMatrix = []
   if doorMatrix == ["Y","R","G","G","B","Y"]:
      safeOpen = True

def drawResetButton():
   setColor("light grey")
   fillRectangle(875,200,945,240)
   setColor("black")
   drawString("RESET",878,228,"Arial",14,"bold")

def drawClosedSafe():
   setColor("black")
   fillRectangle(800,255,870,300)
   setColor("grey")
   fillRectangle(855,260,865,295)

def drawRedKey():
   if redKey == False:
      setColor("red")
      fillCircle(830,275,8)
      setColor("brown")
      fillCircle(830,275,5)
      setColor("red")
      width(4)
      drawLine(837,275,860,275)
      drawLine(845,275,845,280)
      drawLine(855,275,855,277)
      drawLine(860,275,860,283)
      width(1)
  
def drawOpenSafe():
   setColor("brown")
   fillRectangle(800,255,870,300)
   setColor("black")
   fillRectangle(800,255,820,300)
   setColor("grey")
   fillRectangle(800,260,790,295)
   if redKey == False:
      drawRedKey()
      global safeOpen
      safeOpen = True
   else:
      setColor("brown")
      fillRectangle(800,255,870,300)
      setColor("grey")
      fillRectangle(800,260,790,295)

def drawNote():
   setColor("black")
   fillRectangle(1100,150,1130,200)
   setColor("white")
   fillRectangle(1101,151,1129,199)
   setColor("black")
   y = 155
   for lines in range(5):
      drawLine(1105,y,1125,y)
      y += 6
   
def drawBigNote():
   setColor("black")
   fillRectangle(170,0,1130,800)
   setColor("white")
   fillRectangle(173,0,1127,800)
   width(5)
   setColor("red")
   drawLine(1100,20,1120,40)
   drawLine(1100,40,1120,20)
   setColor("black")
   drawString("4 _ _",300,400,"Arial",50,"bold")
   drawString("THE CLOUDS LOOK STRANGE",300,300,"Arial",40,"bold")
   drawString("Happy Birthday, Brooks!",300,200,"Arial",50,"italic")
   drawString("The Crimson Book is n",300,100,"Arial",50,"bold")
   drawString("ot a book at all.",300,500,"Arial",50,"bold")
   width(1)

def drawWestWall():
   clear()
   setBackground(245,245,220)
   setColor("black")
   drawLine(100,0,100,600)
   drawLine(100,600,1200,600)
   drawLine(1200,600,1300,700)
   drawLine(100,600,0,700)
   drawLine(1200,0,1200,600)
   drawWestDots()
   drawWestPuzzle()
   drawNote()
   global colorMatrix
   global correctColorMatrix
   global redKey
   if colorMatrix == correctColorMatrix:
      update()
      drawOpenSafe()
   else:
      drawClosedSafe()
   if redKey == True:
      setColor("brown")
      fillRectangle(800,255,870,300)
      setColor("black")
      fillRectangle(800,255,820,300)
   drawResetButton()
   drawArrows()
   drawFloor(2)
   drawInventory()
   onscreenclick(displayWestWallMouseEvents,btn=1)

def displayWestWallMouseEvents(x,y):
   if inside(x,y,0,325,100,375):
      drawSouthWall()
   elif inside(x,y,1200,325,1300,375):
      drawExitWall()
   elif inside(x,y,1100,150,1130,200):
      drawBigNote()
   elif inside(x,y,1100,20,1120,40):
      drawWestWall()
   elif inside(x,y,875,200,945,240):
      global colorMatrix
      colorMatrix = []
   elif inside(x,y,805,185,835,215):
      colorMatrix += "R"
      if colorMatrix == correctColorMatrix:
         update()
         drawOpenSafe()
      else:
         pass
   elif inside(x,y,835,185,865,215):
      colorMatrix += "G"
      if colorMatrix == correctColorMatrix:
         update()
         drawOpenSafe()
      else:
         pass
   elif inside(x,y,805,215,835,245):
      colorMatrix += "Y"
      if colorMatrix == correctColorMatrix:
         update()
         drawOpenSafe()
      else:
         pass
   elif inside(x,y,835,215,865,245):
      colorMatrix += "B"
      if colorMatrix == correctColorMatrix:
         update()
         drawOpenSafe()
      else:
         pass
   elif inside(x,y,800,255,870,300) and safeOpen == True:
      global redKey
      redKey = True
      drawWestWall()
   
##############
# South Wall #
##############

def drawSouthWall():
   clear()
   setBackground(245,245,220)
   setColor("black")
   drawLine(100,0,100,600)
   drawLine(100,600,1200,600)
   drawLine(1200,600,1300,700)
   drawLine(100,600,0,700)
   drawLine(1200,0,1200,600)
   setColor("skyblue")
   fillRectangle(400,200,900,500)
   setColor("dark green")
   fillRectangle(400,400,900,500)
   setColor("white")
   fillRectangle(450,320,550,350)
   fillRectangle(635,210,665,350)
   fillRectangle(725,320,850,350)
   for k in range(25):
      x1 = randint(450,575)
      x2 = randint(635,665)
      x3 = randint(725,850)
      y1 = randint(320,350)
      y2 = randint(225,350)
      y3 = randint(320,350)
      fillCircle(x1,y1,20)
      fillCircle(x2,y2,20)
      fillCircle(x3,y3,20)
   setColor("black")
   drawRectangle(400,200,900,500)
   drawRectangle(400,400,900,500)
   drawArrows()
   drawFloor(1)
   drawInventory()
   onscreenclick(displaySouthWallMouseEvents,btn=1)

def displaySouthWallMouseEvents(x,y):
   if inside(x,y,0,325,100,375):
      drawEastWall()
   elif inside(x,y,1200,325,1300,375):
      drawWestWall()

#########
# Floor #
#########

def drawFloor(side):
   if side == 1:
      setColor("brown")
      fillPolygon([100,600,1200,600,1300,700,0,700])
      setColor("black")
      drawLine(80,620,1220,620)
      drawLine(60,640,1240,640)
      drawLine(40,660,1260,660)
      drawLine(20,680,1280,680)
      drawPolygon([100,600,1200,600,1300,700,0,700])
   if side == 2:
      setColor("brown")
      fillPolygon([100,600,1200,600,1300,700,0,700])
      setColor("black")
      y1=600
      y2=700
      x1=650
      x2=650
      for k in range(15):
         drawLine(x1,y1,x2,y2)
         x1+=36
         x2+=36+k
      y1=600
      y2=700
      x1=650
      x2=650
      for k in range(15):
         drawLine(x1,y1,x2,y2)
         x1-=36
         x2-=36+k
      drawPolygon([100,600,1200,600,1300,700,0,700])