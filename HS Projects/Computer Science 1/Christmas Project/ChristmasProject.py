# ChristmasProject.py
# The theme of this project is: "What the Christmas season means to me"

from Graphics import *

beginGrfx(1300,700)

#Midnight Sky

l=760
r=10
g=10
b=40
for k in range(75,1,-1):
   setColor(r,g,b)
   fillCircle(740,75,l)
   l-=10
   r+=1
   g+=1
   b+=1

#Ground

setColor(60,70,90)
fillRectangle(0,375,1300,700)
r = 60
g = 70
b = 90
hr = 320
vr = 120
for k in range(40,1,-1):
   setColor(r,g,b)
   fillOval(595,470,hr,vr)
   hr-=4
   vr-=2
   r+=1
   g+=randint(1,2)
   b+=2

#Night Stars

for k in range(30):
   setColor("white")
   x= randint(0,650)
   y= randint(0,200)
   r= randint(2,5)
   s= randint(5,10)
   fillStar(x,y,r,s)
for k in range(25):
   setColor("white")
   x= randint(830,1300)
   y= randint(0,190)
   r= randint(2,5)
   s= randint(5,10)
   fillStar(x,y,r,s)

#Moon

setColor(100,100,100)
fillCircle(740,75,60)
setColor(80,80,80)
fillCircle(725,60,15)
fillCircle(715,90,11)
fillCircle(770,20,20)
setColor(70,70,70)
fillCircle(770,65,18)
fillArc(680,85,10,0,170)
fillCircle(780,110,15)
setColor(90,90,90)
fillCircle(745,90,8)
fillCircle(690,50,8)
fillCircle(730,30,8)
fillCircle(730,120,8)
width(1)
setColor("black")
drawCircle(725,60,15)
drawCircle(715,90,11)
drawCircle(770,20,20)
drawCircle(770,65,18)
drawArc(680,85,10,0,170)
drawCircle(780,110,15)
drawCircle(745,90,8)
drawCircle(690,50,8)
drawCircle(730,30,8)
drawCircle(730,120,8)
r=85
width(2)
red=76
green=76
blue=106
for j in range(2):
   red+=1
   green+=1
   blue+=1
   for k in range (13):
      setColor(red,green,blue)
      drawCircle(740,75,r)
      r-=1
width(1)
setColor("black")
drawCircle(740,75,60)
setColor("white")
fillRectangle(740,8,755,17.5)
setColor(179,25,66)
y=8.5
for k in range(5):
   drawLine(740,y,755,y)
   y+=1.9
drawLine(740,17,755,17)
setColor(60,59,110)
fillRectangle(740,8,747,12)
setColor("black")
drawLine(740,30,740,8)
drawRectangle(740,8,755,17.5)
setColor("gold")
width(2)
drawPixel(740,7)
width(1)
setColor(45,45,45)
fillPolygon([0,245,200,80,400,145,550,80,725,195,850,90,975,185,1050,95,1135,195,1300,145,1300,375,0,375])
setColor(30,30,30)
fillPolygon([1300,145,1300,375,970,245])
setColor(35,35,35)
fillPolygon([200,80,270,250,600,210])
fillPolygon([1050,95,1020,250,900,275])
setColor(45,45,45)
fillPolygon([550,80,725,195,725,300,450,300])
setColor(20,20,20)
fillPolygon([0,375,0,245,200,80,270,250])
fillPolygon([1050,95,1020,250,1220,295])
setColor(210,210,210)
fillPolygon([227,140,200,80,290,110])
setColor(170,170,170)
fillPolygon([200,80,225,140,130,140])
setColor("black")
drawLine(200,80,270,250)
setColor(35,35,35)
fillPolygon([100,275,550,80,475,335])
fillPolygon([850,90,1100,280,870,250])
setColor(0,0,0)
drawLine(550,80,100,275)
setColor(210,210,210)
fillPolygon([1050,95,1040,140,1005,150])
setColor(170,170,170)
fillPolygon([1050,95,1040,140,1084,135])
setColor(240,240,240)
fillPolygon([550,80,535,140,610,120])
fillPolygon([850,90,816,120,855,130])
setColor(190,190,190)
fillPolygon([550,80,534,140,436,130])
fillPolygon([850,90,855,130,908,135])
fillPolygon([1300,160,1218,170,1300,145])
setColor(190,190,190)
fillPolygon([550,80,534,140,436,130])
setColor("black")
drawPolygon([0,245,200,80,400,145,550,80,725,195,850,90,975,185,1050,95,1135,195,1300,145,1300,375,0,375])
drawLine(550,80,500,250)
drawLine(550,80,900,310)
drawLine(850,90,870,250)
drawLine(1050,95,1020,250)
drawLine(850,90,1100,280)
drawLine(1050,95,1220,295)

#2nd Mountain Background

setColor(25,25,25)
fillPolygon([0,300,112,200,200,264,325,200,400,300,486,190,555,263,605,220,682,310,815,175,950,245,1030,170,1215,290,1300,232,1300,375,0,375])
setColor("black")
drawPolygon([0,300,112,200,200,264,325,200,400,300,486,190,555,263,605,220,682,310,815,175,950,245,1030,170,1215,290,1300,232,1300,375,0,375])

#House

r= randint(100,121)
g= randint(30,40)
b= randint(30,45)
setColor(r,g,b)
fillRectangle(455,350,735,480)
setColor("black")
drawRectangle(455,350,735,480)
x1=455
y1=350
x2=465
y2=355
for j in range(13):
   for k in range(28):
      r= randint(100,121)
      g= randint(30,40)
      b= randint(30,45)
      setColor(r,g,b)
      fillRectangle(x1,y1,x2,y2)
      setColor("black")
      drawRectangle(x1,y1,x2,y2)
      x1+=10
      x2+=10
   x1-=275
   y1+=5
   x2-=275
   y2+=5
   for k in range(27):
      r= randint(100,121)
      g= randint(30,40)
      b= randint(30,45)
      setColor(r,g,b)
      fillRectangle(x1,y1,x2,y2)
      setColor("black")
      drawRectangle(x1,y1,x2,y2)
      x1+=10
      x2+=10   
   y1+=5
   y2+=5
   x1-=275
   x2-=275
setColor(94,38,18)
fillRectangle(570,480,620,400)
setColor("black")
fillCircle(610,440,2)
drawRectangle(570,480,620,400)
setColor(255,255,204)
fillRectangle(495,385,545,435)
setColor("black")
drawRectangle(495,385,520,410)
drawRectangle(520,385,545,410)
drawRectangle(495,410,520,435)
drawRectangle(520,410,545,435)

#Santa's sled

sledx1=225
sledx2=270
sledy1=75
sledy2=80
sledx3=230
sledx4=235
sledy3=75
sledy4=68
sledx5=260
sledx6=265
arcx1=270
setColor(100,50,30)
fillRectangle(sledx1,sledy1,sledx2,sledy2)
setColor("black")
drawRectangle(sledx1,sledy1,sledx2,sledy2)
setColor(100,50,30)
fillRectangle(sledx3,sledy3,sledx4,sledy4)
setColor("black")
drawRectangle(sledx3,sledy3,sledx4,sledy4)
setColor(100,50,30)
fillRectangle(sledx5,75,sledx6,68)
setColor("black")
drawRectangle(sledx5,75,sledx6,68)
setColor(100,50,30)
fillArc(arcx1,70,10,10,90,180)
setColor("black")
drawArc(270,70,10,10,90,180)
setColor(100,50,30)
fillCircle(236,50,15)
setColor("black")
drawCircle(236,50,15)
setColor(100,50,30)
fillPolygon([236,35,231,30,241,30,])
setColor("black")
drawPolygon([236,35,231,30,241,30,])
setColor(40,40,70)
fillArc(270,70,3,3,90,180)
setColor("black")
drawArc(270,70,3,3,90,180)
setColor(100,0,0)
fillRectangle(230,68,265,55)
setColor("black")
drawRectangle(230,68,265,55)
setColor(100,0,0)
fillArc(230,55,13,13,180,310)
setColor("black")
drawArc(230,55,13,13,180,310)
setColor(100,0,0)
fillArc(265,55,13,13,90,180)
setColor("black")
drawArc(265,55,13,13,90,180)
setColor("white")
fillStar(265,30,3,12)
setColor("black")
drawStar(265,30,3,12)
setColor(100,0,0)
fillOval(265,55,5,10)
setColor("black")
drawArc(265,55,5,10,270,60)
setColor(238,207,161)
fillCircle(265,43,5)
setColor("black")
drawCircle(265,43,5)
setColor(238,207,161)
fillCircle(278,50,1)
setColor("black")
drawCircle(278,50,1)
setColor(100,0,0)
fillPolygon([265,33,260,40,270,40])
setColor("black")
drawPolygon([265,33,260,40,270,40])
setColor(100,0,0)
fillPolygon([269,51,273,51,277,49,277,52,273,54,269,54])
setColor("black")
drawPolygon([269,51,273,51,277,49,277,52,273,54,269,54])
drawLine(230,55,280,55)
drawLine(230,55,220,45)
drawLine(273,70,280,70)

#Santa's reindeer

firstLx1=315
firstLy1=57
firstLx2=318
firstLy2=65
secondLx1=335
secondLy1=57
secondLx2=338
secondLy2=65
recx1=278
recy1=50
recx2=310
recy2=50
ovalx=325
ovaly=50
circlex=340
circley=42
eyex=341
eyey=41
x1=339
x2=337
x3=335
x4=336
x5=338
x6=339
x7=340
for k in range(5):
   setColor(85,57,44)
   drawLine(recx1,recy1,recx2,recy2)
   setColor(97,69,56)
   fillOval(ovalx,ovaly,15,7)
   setColor("black")
   drawOval(ovalx,ovaly,15,7)
   setColor(97,69,56)
   fillRectangle(firstLx1,firstLy1,firstLx2,firstLy2)
   setColor("black")
   drawRectangle(firstLx1,firstLy1,firstLx2,firstLy2)
   setColor(97,69,56)
   fillRectangle(secondLx1,secondLy1,secondLx2,secondLy2)
   setColor("black")
   drawRectangle(secondLx1,secondLy1,secondLx2,secondLy2)
   setColor(97,69,56)
   fillCircle(circlex,circley,5)
   setColor("black")
   drawCircle(circlex,circley,5)
   fillCircle(eyex,eyey,1)
   setColor(227,218,201)
   fillPolygon([x1,38,x2,35,x3,32,x4,31,x5,34,x6,32,x7,32])
   firstLx1+=60
   firstLx2+=60
   secondLx1+=60
   secondLx2+=60
   recx1+=60
   recx2+=60
   ovalx+=60
   circlex+=60
   eyex+=60
   x1+=60
   x2+=60
   x3+=60
   x4+=60
   x5+=60
   x6+=60
   x7+=60
setColor("red")
fillCircle(586,42,1)

#Santa's hand

setColor(238,207,161)
fillCircle(278,50,1)
setColor("black")
drawCircle(278,50,1)

#Roof

setColor(132,136,132)
fillCircle(690,246,6)
setColor("black")
drawCircle(690,246,6)
setColor(132,136,132)
fillCircle(665,275,10)
setColor("black")
drawCircle(665,275,10)
setColor(132,136,132)
fillCircle(677,270,8)
setColor("black")
drawCircle(677,270,8)
setColor(132,136,132)
fillCircle(668,264,5)
setColor("black")
drawCircle(668,264,5)
setColor(132,136,132)
fillCircle(685,252,8)
setColor("black")
drawCircle(685,252,8)
setColor(132,136,132)
fillCircle(677,259,8)
setColor("black")
drawCircle(677,259,8)
setColor(132,136,132)
fillCircle(674,246,3)
setColor("black")
drawCircle(674,246,3)
setColor(50,50,50)
fillPolygon([450,350,595,285,740,350])
setColor("black")
x1=460
y1=345
x2=470
y2=350
for j in range(6):
   for k in range(27):
      drawRectangle(x1,y1,x2,y2)
      x1+=10
      x2+=10
   x1-=275
   y1-=5
   x2-=275
   y2-=5
   for k in range(27):
      drawRectangle(x1,y1,x2,y2)
      x1+=10
      x2+=10   
   y1-=5
   y2-=5
   x1-=275
   x2-=275
drawRectangle(590,285,600,290)
setColor(25,25,25)
fillPolygon([0,300,112,200,200,264,325,200,395,295,486,190,555,263,605,220,682,310,815,175,950,245,1030,170,1215,300,1300,232,1300,375,735,375,735,350,740,350,595,285,450,350,455,350,455,375,0,375])
setColor("black")
drawPolygon([0,300,112,200,200,264,325,200,395,295,486,190,555,263,605,220,682,310,815,175,950,245,1030,170,1215,290,1300,232,1300,375,0,375])
r=120
g=45
b=45
setColor(r,g,b)
fillRectangle(655,335,685,275)
setColor("black")
drawRectangle(655,335,685,275)
x1=655
y1=275
x2=665
y2=280
r=120
g=45
b=45
for j in range(6):
   for k in range(3):
      r= randint(100,121)
      g= randint(30,40)
      b= randint(30,45)
      setColor(r,g,b)
      fillRectangle(x1,y1,x2,y2)
      setColor("black")
      drawRectangle(x1,y1,x2,y2)
      x1+=10
      x2+=10
   x1-=25
   y1+=5
   x2-=25
   y2+=5
   for k in range(2):
      r= randint(100,121)
      g= randint(30,40)
      b= randint(30,45)
      setColor(r,g,b)
      fillRectangle(x1,y1,x2,y2)
      setColor("black")
      drawRectangle(x1,y1,x2,y2)
      x1+=10
      x2+=10   
   y1+=5
   y2+=5
   x1-=25
   x2-=25

#Christmas tree

setColor(57,38,23)
fillRectangle(985,520,1025,300)
setColor("black")
drawRectangle(985,520,1025,300)
x1=1005
y1=480
x2=915
y2=490
setColor("black")
drawLine(x1,y1,x2,y2)
while x2<1000:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(50,60)
   b=0
   setColor(r,g,b)
   y=2
   x2+=.5
   y1-=y
   y2-=y
   drawLine(x1,y1,x2,y2)
   width(1)
   setColor("black")
   drawPixel(x2,y2)
x2=(x1-x2)+x1
y3=y1-10
while y1<478:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(40,50)
   b=0
   setColor(r,g,b)
   y=2
   x2+=.5
   y1+=y
   y2+=y
   drawLine(x1,y1,x2,y2)
   width(1)
   setColor("black")
   drawPixel(x2,y2)
width(1)
setColor("black")
drawLine(x1,480,x2,y2)
setColor("gold")
fillStar(x1,y3,15,9)
setColor("black")
drawStar(x1,y3,15,9)
setColor(255,194,0)
x1=920
y1=485
for k in range(17):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1+=5
   y1-=randint(3,5)
setColor(190,150,0)
for k in range(13):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1+=5
   y1-=randint(3,5)
setColor(145,145,145)
x=1090
y=485
for k in range(17):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x-=5
   y-=randint(3,5)
setColor(190,190,190)
for k in range(13):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x-=5
   y-=randint(3,5)
setColor(255,194,0)
x+=5
y+=4
for k in range(12):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x+=5
   y-=randint(3,5)
setColor(190,150,0)
for k in range(8):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x+=5
   y-=randint(3,5)
setColor(145,145,145)
x1-=5
y1+=4
for k in range(12):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1-=5
   y1-=randint(3,5)
setColor(190,190,190)
for k in range(8):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1-=5
   y1-=randint(3,5)
setColor(255,194,0)
x1+=5
y1+=4
for k in range(7):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1+=5
   y1-=randint(3,5)
setColor(190,150,0)
for k in range(7):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1+=5
   y1-=randint(3,5)
setColor(145,145,145)
x-=5
y+=4
for k in range(7):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x-=5
   y-=randint(3,5)
setColor(190,190,190)
for k in range(7):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x-=5
   y-=randint(3,5)
setColor(255,194,0)
x+=5
y+=4
for k in range(6):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x+=5
   y-=randint(3,5)
setColor(190,150,0)
for k in range(5):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x,y,r,s)
   x+=5
   y-=randint(3,5)
setColor(145,145,145)
x1-=5
y1+=4
for k in range(6):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1-=5
   y1-=randint(3,5)
setColor(190,190,190)
for k in range(5):
   r=randint(4,6)
   s=randint(10,12)
   drawBurst(x1,y1,r,s)
   x1-=5
   y1-=randint(3,5)
setColor(0,110,0)
fillCircle(940,465,9)
setColor("black")
drawCircle(940,465,9)
setColor(0,110,0)
fillCircle(980,450,9)
setColor("black")
drawCircle(980,450,9)
setColor(0,110,0)
fillCircle(955,435,9)
setColor("black")
drawCircle(955,435,9)
setColor(110,0,0)
fillCircle(980,410,9)
setColor("black")
drawCircle(980,410,9)
setColor(110,0,0)
fillCircle(960,390,9)
setColor("black")
drawCircle(960,390,9)
setColor(0,110,0)
fillCircle(970,360,9)
setColor("black")
drawCircle(970,360,9)
setColor(110,0,0)
fillCircle(985,330,9)
setColor("black")
drawCircle(985,330,9)
setColor(110,0,0)
fillCircle(975,300,9)
setColor("black")
drawCircle(975,300,9)
setColor(0,110,0)
fillCircle(985,270,9)
setColor("black")
drawCircle(985,270,9)
setColor(110,0,0)
fillCircle(995,240,9)
setColor("black")
drawCircle(995,240,9)
setColor(110,0,0)
fillCircle(995,240,9)
setColor("black")
drawCircle(995,240,9)
setColor(0,110,0)
fillCircle(995,210,9)
setColor("black")
drawCircle(995,210,9)
setColor(110,0,0)
fillCircle(1000,170,9)
setColor("black")
drawCircle(1000,170,9)
setColor(80,0,0)
fillCircle(1020,460,9)
setColor("black")
drawCircle(1020,460,9)
setColor(80,0,0)
fillCircle(1060,440,9)
setColor("black")
drawCircle(1060,440,9)
setColor(0,80,0)
fillCircle(1030,430,9)
setColor("black")
drawCircle(1030,430,9)
setColor(0,70,0)
fillCircle(1065,410,9)
setColor("black")
drawCircle(1065,410,9)
setColor(80,0,0)
fillCircle(1045,390,9)
setColor("black")
drawCircle(1045,390,9)
setColor(0,70,0)
fillCircle(1015,380,9)
setColor("black")
drawCircle(1015,380,9)
setColor(80,0,0)
fillCircle(1030,350,9)
setColor("black")
drawCircle(1030,350,9)
setColor(80,0,0)
fillCircle(1040,320,9)
setColor("black")
drawCircle(1040,320,9)
setColor(0,70,0)
fillCircle(1020,290,9)
setColor("black")
drawCircle(1020,290,9)
setColor(80,0,0)
fillCircle(1030,260,9)
setColor("black")
drawCircle(1030,260,9)
setColor(0,70,0)
fillCircle(1020,230,9)
setColor("black")
drawCircle(1020,230,9)
setColor(80,0,0)
fillCircle(1010,195,9)
setColor("black")
drawCircle(1010,195,9)

#People and dogs

setColor("black")
fillCircle(865,495,8)
fillOval(865,518,8,15)
fillRectangle(864,540,860,530)
fillRectangle(866,540,870,530)
x=860
y=490
for k in range(6):
   fillCircle(x,y,2)
   x-=1
   y+=2
x=870
y=490
for k in range(6):
   fillCircle(x,y,2)
   x+=1
   y+=2
x=900
y=460
for k in range(8):
   fillCircle(x,y,3)
   x-=1
   y+=2
x=910
y=460
for k in range(8):
   fillCircle(x,y,3)
   x+=1
   y+=2
fillCircle(905,467,10)
fillOval(905,504,12,26)
fillRectangle(896,520,903,540)
fillRectangle(907,520,914,540)
fillCircle(945,425,15)
fillOval(945,475,13,35)
fillPolygon([935,500,930,540,935,540,945,510,955,540,960,540,955,500])
width(5)
drawArc(945,475,18,30,235,115)
width(1)
fillCircle(985,400,15)
fillOval(985,455,15,38)
fillPolygon([975,480,970,540,975,540,985,490,995,540,1000,540,995,480])
width(5)
drawArc(985,455,21,30,235,115)
width(1)
fillCircle(1025,400,15)
fillOval(1025,455,15,38)
fillPolygon([1015,480,1010,540,1015,540,1025,490,1035,540,1040,540,1035,480])
width(5)
drawArc(1025,455,21,30,235,115)
width(1)
fillCircle(1065,425,15)
fillOval(1065,475,13,35)
fillPolygon([1055,500,1050,540,1055,540,1065,510,1075,540,1080,540,1075,500])
width(5)
drawArc(1065,475,18,30,235,115)
width(1)
fillCircle(1105,401,15)
fillOval(1105,455,15,38)
fillPolygon([1095,480,1090,540,1095,540,1105,490,1115,540,1120,540,1115,480])
width(5)
drawArc(1105,455,20,30,235,115)
width(1)
fillCircle(1145,435,15)
fillOval(1145,475,12,28)
fillPolygon([1135,498,1130,540,1135,540,1145,510,1155,540,1160,540,1155,498])
width(5)
drawArc(1145,478,17,27,235,115)
width(1)

#Trees

setColor(57,38,23)
fillRectangle(90,520,110,320)
setColor("black")
drawRectangle(90,520,110,320)
x1=100
y1=480
x2=30
y2=490
drawLine(x1,y1,x2,y2)
while x2<95:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(20,30)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1-=y
   y2-=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
x2+=10
while y1<478:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(30,40)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1+=y
   y2+=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
drawLine(x1,480,x2,y2)
setColor(57,38,23)
fillRectangle(280,440,300,240)
setColor("black")
drawRectangle(280,440,300,240)
x1=290
y1=400
x2=220
y2=410
drawLine(x1,y1,x2,y2)
while x2<285:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(30,40)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1-=y
   y2-=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
x2+=10
while y1<398:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(40,50)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1+=y
   y2+=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
drawLine(x1,400,x2,y2)
setColor(57,38,23)
fillRectangle(210,620,230,420)
setColor("black")
drawRectangle(210,620,230,420)
x1=220
y1=580
x2=150
y2=590
drawLine(x1,y1,x2,y2)
while x2<215:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(25,35)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1-=y
   y2-=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
x2+=10
while y1<578:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(35,45)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1+=y
   y2+=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
drawLine(x1,580,x2,y2)
setColor(57,38,23)
fillRectangle(325,640,335,540)
setColor("black")
drawRectangle(325,640,335,540)
x1=330
y1=600
x2=290
y2=610
drawLine(x1,y1,x2,y2)
while x2<325:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(30,40)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1-=y
   y2-=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
x2+=10
while y1<598:
   w=randint(2,4)
   width(w)
   r=0
   g=randint(40,50)
   b=0
   setColor(r,g,b)
   y=2
   x2+=randint(0,1)
   y1+=y
   y2+=y
   drawLine(x1,y1,x2,y2)
   setColor("black")
   width(1)
   drawPixel(x2,y2)
drawLine(x1,600,x2,y2)

#Clouds

width(1)
setColor(70,70,70)
fillRectangle(900,50,1050,90)
fillCircle(900,65,25)
fillCircle(930,45,15)
fillCircle(950,40,12)
fillCircle(980,45,25)
fillCircle(1015,40,18)
fillCircle(1040,50,20)
fillCircle(1070,65,25)
fillCircle(1050,85,13)
fillCircle(1028,93,10)
fillCircle(1000,87,20)
fillCircle(970,85,15)
fillCircle(950,90,10)
fillCircle(930,85,18)
fillCircle(910,88,10)
setColor("black")
drawArc(900,65,25,25,180,45)
drawArc(930,45,15,15,270,40)
drawArc(950,40,12,12,270,90)
drawArc(980,45,25,25,300,70)
drawArc(1015,40,18,18,300,50)
drawArc(1040,50,20,20,310,60)
drawArc(1070,65,25,25,310,190)
drawArc(1050,85,13,13,80,250)
drawArc(1028,93,10,10,90,260)
drawArc(1000,87,20,20,120,260)
drawArc(970,85,15,15,130,220)
drawArc(950,90,10,10,100,220)
drawArc(930,85,18,18,110,220)
drawArc(910,88,10,10,130,280)

#Snow

setColor(200,200,200)
for k in range(50):
   w=randint(1,2)
   width(w)
   r=randint(8,12)
   s=randint(6,8)
   x=randint(0,1300)
   y=randint(200,700)
   drawBurst(x,y,r,s)

#Blinking lights

def selectColor1():
   x=randint(1,2)
   if x==1:
      setColor("yellow")
   else:
      setColor("white")
def selectColor3():
   x=randint(1,2)
   if x==1:
      setColor("DeepPink")
   else:
      setColor("BlueViolet")
def selectColor2():
   x=randint(1,2)
   if x==1:
      setColor("green")
   else:
      setColor("blue")
def selectColor4():
   x=randint(1,2)
   if x==1:
      setColor("red")
   else:
      setColor("orange")
def selectColor5():
   x=randint(1,3)
   if x==1:
      setColor("green")
   elif x==2:
      setColor("red")
   else:
      setColor("blue")
def selectColor6():
   x=randint(1,3)
   if x==1:
      setColor("DeepPink")
   elif x==2:
      setColor("BlueViolet")
   else:
      setColor("orange")
for k in range(30):
   x=450
   y=348
   for k in range(10):
      selectColor1()
      fillOval(x,y,1,2)
      x+=5
      y-=2
      selectColor5()
      fillOval(x,y,1,2)
      x+=5
      y-=2
      selectColor6()
      fillOval(x,y,1,2)
      x+=5
      y-=2
   x-=5
   y+=2
   for k in range(3):
      selectColor1()
      fillOval(x,y,1,2)
      x+=5
      y+=2
      selectColor2()
      fillOval(x,y,1,2)
      x+=5
      y+=2
      selectColor3()
      fillOval(x,y,1,2)
      x+=5
      y+=2
      selectColor4()
      fillOval(x,y,1,2)
      x+=5
      y+=2
   x+=33
   y+=13
   for k in range(3):
      selectColor1()
      fillOval(x,y,1,2)
      x+=5
      y+=2
      selectColor5()
      fillOval(x,y,1,2)
      x+=5
      y+=2
      selectColor6()
      fillOval(x,y,1,2)
      x+=5
      y+=2
   y=348
   x=450
   for k in range(12):
      selectColor1()
      fillOval(x,y,1,2)
      x+=6
      selectColor2()
      fillOval(x,y,1,2)
      x+=6
      selectColor3()
      fillOval(x,y,1,2)
      x+=6
      selectColor4()
      fillOval(x,y,1,2)
      x+=6
   delay(10)

endGrfx()