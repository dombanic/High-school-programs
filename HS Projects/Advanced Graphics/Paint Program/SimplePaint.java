// SimplePaint.java
// The Paint Brush Program
// Made in Collaboration with Karson Aronsson


import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class SimplePaint 
{
   public static void main(String args[])
   {
      Painter paint = new Painter();
      paint.addWindowListener(new WindowAdapter()
      {public void windowClosing(WindowEvent e)
      {System.exit(0);}});
      paint.setSize(1900,950);
      paint.setVisible(true);
   }
}


class Painter extends Frame implements MouseListener, MouseMotionListener, MouseWheelListener
{
   private Rectangle red, orange, yellow, green, blue, purple, pink, black, custom;
   private Rectangle pencil, brush, custom1, sprayCan, clear, erase, vLine, hLine, circleSquare, line, rectangle, oval, circle, star, polygon, increase, decrease, filler;
   private Rectangle rUp, rDown, gUp, gDown, bUp, bDown;
   private Rectangle vlUp, vlDown, hlUp, hlDown;
   int numColor, numTool, xClick, yClick;
   int vLength = 41;
   int hLength = 41;
   int vNum = 5;
   int hNum = 5;
   int r1=125;
   int gr1=125;
   int b1=125;
   int r=125;
   int gr=125;
   int b=125;
   boolean clearScreen = false;
   boolean circleBrush = false;
   Random rand = new Random();
   boolean up = true;
   int penx, peny, startx, starty;
   private Graphics gBuffer;
   private Image virtualMem;
   private boolean ready, setFill, color1;
   int radius;
   int sides = 5;
      
   //Colors
   Color purpleColor = new Color(150,0,150);

   public Painter()
   {
      super("SimplePaint");
      addMouseListener(this);
      addMouseMotionListener(this);
      addMouseWheelListener(this);      

      setSize(1900+22,950+60);
      setVisible(true);
      virtualMem = createImage(1900,950);
   	gBuffer = virtualMem.getGraphics();
      
      red = new Rectangle(11,40,75,75);
      orange = new Rectangle(86,40,75,75);
      yellow = new Rectangle(11,40+75,75,75);
      green = new Rectangle(86,40+75,75,75);
      blue = new Rectangle(11,40+150,75,75);
      purple = new Rectangle(86,40+150,75,75);
      pink = new Rectangle(11,40+225,75,75);
      black = new Rectangle(86,40+225,75,75);
      pencil = new Rectangle(11,40+300,75,75);
      brush = new Rectangle(86,40+300,75,75);
      erase = new Rectangle(11,40+375,75,75);
      sprayCan = new Rectangle(86,40+375,75,75);
      clear = new Rectangle(11,40+450,150,75);
      custom1 = new Rectangle(11,40+525,75,75);
      custom = new Rectangle(86,40+525,75,75);
      circleSquare = new Rectangle(11,40+750,75,75);
      line = new Rectangle(86,40+750,75,75);
      rectangle = new Rectangle(161,40,75,75);
      oval = new Rectangle(161,40+75,75,75);
      circle = new Rectangle(161,40+150,75,75);
      star = new Rectangle(161,40+225,75,75);
      polygon = new Rectangle(161,40+300,75,75);
      increase = new Rectangle(161,40+375,75,75);
      decrease = new Rectangle(161,40+450,75,75);
      filler = new Rectangle(161,40+525,75,75);
      
      vLine = new Rectangle(11,40+675,50,75);
      hLine = new Rectangle(86,40+675,50,75);
      vlUp = new Rectangle(11+50,40+700,25,25);
      vlDown = new Rectangle(11+50,40+725,25,25);
      hlUp = new Rectangle(86+50,40+700,25,25);
      hlDown = new Rectangle(86+50,40+725,25,25);

      rUp = new Rectangle(36,40+625,25,25);
      rDown = new Rectangle(36,40+650,25,25);
      gUp = new Rectangle(86,40+625,25,25);
      gDown = new Rectangle(86,40+650,25,25);
      bUp = new Rectangle(136,40+625,25,25);
      bDown = new Rectangle(136,40+650,25,25);
      
      numColor = 8;
      numTool = 1;
      ready = true;
   }

   public void paint(Graphics g)
   {
      Graphics2D g2D = (Graphics2D) g;
      g2D.translate(11,40);
      if (ready)
      {
         drawMenu(gBuffer);
         colorPicker(g, gBuffer);
         
         if (xClick>=240)
         {
            tools(gBuffer);  
            virtualTools(g, gBuffer);
         }
      }
      g.drawImage(virtualMem,0,0,this);
      if (xClick>=240 && up == false)
      {
         rubberBands(g);
      }
   }

   public void mousePressed(MouseEvent e)
   {
      int x = e.getX();
      int y = e.getY();
      startx = x-11;
      starty = y-40;
      penx = x-11;
      peny = y-40;
      if(red.contains(x,y))
      {
         numColor = 1;
      }
      else if(orange.contains(x,y))
      {
         numColor = 2;
      }
      else if(yellow.contains(x,y))
      {
         numColor = 3;
      }
      else if(green.contains(x,y))
      {
         numColor = 4;
      }
      else if(blue.contains(x,y))
      {
         numColor = 5;
      }
      else if(purple.contains(x,y))
      {
         numColor = 6;
      }
      else if(pink.contains(x,y))
      {
         numColor = 7;
      }
      else if(black.contains(x,y))
      {
         numColor = 8;
      }
      else if(erase.contains(x,y))
      {
         numColor = 9;
      }
      else if(custom.contains(x,y))
      {
         numColor = 10;
         color1 = false;
      }
      else if(clear.contains(x,y))
      {
         if (e.getClickCount() == 2)
         {
            clearScreen = true;
         }
      }
      else if(pencil.contains(x,y))
      {
         numTool = 1;
      }
      else if(brush.contains(x,y))
      {
         numTool = 2;
      }
      else if(custom1.contains(x,y))
      {
         numColor = 11;
         color1 = true;
         
      }
      else if(sprayCan.contains(x,y))
      {
         numTool = 4;
      }
      else if(circleSquare.contains(x,y))
      {
         circleBrush = !circleBrush;
      }
      else if(vLine.contains(x,y))
      {
         numTool = 5;
      }
      else if(hLine.contains(x,y))
      {
         numTool = 6;
      }
      else if(line.contains(x,y))
      {
         numTool = 7;
      }
      else if(rectangle.contains(x,y))
      {
         numTool = 8;
      }
      else if(oval.contains(x,y))
      {
         numTool = 9;
      }
      else if(circle.contains(x,y))
      {
         numTool = 10;
      }
      else if(star.contains(x,y))
      {
         numTool = 11;
      }
      else if(polygon.contains(x,y))
      {
         numTool = 12;
      }
      else if(increase.contains(x,y))
      {
         sides++;
      }
      else if(decrease.contains(x,y))
      {
         if (sides > 3)
         {
            sides--;
         }
      }
      else if(filler.contains(x,y))
      {
         setFill = !setFill;
      }
      else if(vlUp.contains(x,y))
      {
         vNum++;
      }
      else if(vlDown.contains(x,y))
      {
         vNum--;
      }
      else if(hlUp.contains(x,y))
      {
         hNum++;
      }
      else if(hlDown.contains(x,y))
      {
         hNum--;
      }
      else if(rUp.contains(x,y))
      {
         if (color1 == true)
         {
            if (r1 <= 250)
            {r1+=5;}
         }
         else
         {
            if (r <= 250)
            {r+=5;}
         }
      }
      else if(rDown.contains(x,y))
      {
         if (color1 == true)
         {
            if (r1 >=5)
            {r1-=5;}
         }
         else
         {
            if (r >=5)
            {r-=5;}
         }
      }
      else if(gUp.contains(x,y))
      {
         if (color1 == true)
         {
            if (gr1 <= 250)
            {gr1+=5;}
         }
         else
         {
            if (gr <= 250)
            {gr+=5;}
         }
      }
      else if(gDown.contains(x,y))
      {
         if (color1 == true)
         {
            if (gr1 >=5)
            {gr1-=5;}
         }
         else
         {
            if (gr >=5)
            {gr-=5;}
         }
      }
      else if(bUp.contains(x,y))
      {
         if (color1 == true)
         {
            if (b1 <= 250)
            {b1+=5;}
         }
         else
         {
            if (b <= 250)
            {b+=5;}
         }
      }
      else if(bDown.contains(x,y))
      {
         if (color1 == true)
         {
            if (b1 >=5)
            {b1-=5;}
         }
         else
         {
            if (b >=5)
            {b-=5;}
         }
      }
      xClick = x-11;
      yClick = y-40;
      repaint();
      }
      
   public void mouseDragged(MouseEvent e)
   {
      int x = e.getX();
      int y = e.getY();
      xClick = x-11;
      yClick = y-40;
      repaint();
   }
   
   public void mouseWheelMoved(MouseWheelEvent e)
   {
      int scroll = e.getWheelRotation()*-10;
      
   	if(numTool == 5)
      {
         if(scroll == 10)
         {
            vLength += scroll;
         }
         else
         {
            if (vLength > 11)
            {
               vLength += scroll;
            }
         }
      }
      else if(numTool == 6)
      {
         if(scroll == 10)
         {
            hLength += scroll;
         }
         else
         {
            if (hLength > 11)
            {
               hLength += scroll;
            }
         }
      }
   }
   
   public void mouseMoved(MouseEvent e) {}
   public void mouseEntered(MouseEvent e) { }
   public void mouseExited(MouseEvent e) { }
   public void mouseClicked(MouseEvent e) { }
   public void mouseReleased(MouseEvent e) 
   {
      up = true;
      double twoPI = 2 * Math.PI;
      int xCoord[] = new int[sides*2];
      int yCoord[] = new int[sides*2];
      
      if (xClick>=240)
      {
         switch (numTool)
         {
            case 7:
               gBuffer.drawLine(startx,starty,xClick,yClick);
               break;
            case 8:
               if (setFill == true)
               {
                  gBuffer.fillRect(startx,starty,xClick-startx,yClick-starty);
               }
               else
               {
                  gBuffer.drawRect(startx,starty,xClick-startx,yClick-starty);
               }
               break;
            case 9:
               if (setFill == true)
               {
                  gBuffer.fillOval(startx,starty,xClick-startx,yClick-starty);
               }
               else
               {
                  gBuffer.drawOval(startx,starty,xClick-startx,yClick-starty);
               }
               break;
            case 10:
               if (setFill == true)
               {
                  gBuffer.fillOval(startx-radius,starty-radius,2*radius,2*radius);
               }
               else
               {
                  gBuffer.drawOval(startx-radius,starty-radius,2*radius,2*radius);
               }
               break;
            case 11:
               for (int k = 0; k < sides; k++)
               {
                  xCoord[k] = (int) Math.round(Math.cos(twoPI * k/sides) * radius) + startx;
                  yCoord[k] = (int) Math.round(Math.sin(twoPI * k/sides) * radius) + starty;
               }
               gBuffer.drawPolygon(xCoord,yCoord,sides);
               if (setFill == true)
                     {
                        gBuffer.fillPolygon(xCoord,yCoord,sides);
                     }
               break;
            case 12:
               int starSides = 2 * sides;
                     for (int k = 0; k < starSides; k++)
                  	{
                  	   if (k % 2 == 0)
                        {
                           xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * radius) + startx;
                  	      yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * radius) + starty;
                        }
                        else
                        {
                           xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * radius)/2 + startx;
                  	      yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * radius)/2 + starty;
                        }
                  	}
                  	gBuffer.drawPolygon(xCoord,yCoord,starSides);
                     if (setFill == true)
                     {
                        gBuffer.fillPolygon(xCoord,yCoord,starSides);
                     }
               break;
            
         }
      }
      repaint();
   }
   public void update(Graphics g)
   {
      paint(g);
   }
   
   public void drawMenu(Graphics g)
   {
      Color customColor = new Color(r,gr,b);
      Color customcolor1 = new Color(r1,gr1,b1);
      if (clearScreen == true)
         {
            gBuffer.setColor(Color.white);
            gBuffer.fillRect(-50,-50,2000,1050); //clears the screen
            clearScreen = false;
         }
         
         gBuffer.setColor(Color.lightGray); //tools border
         gBuffer.fillRect(-50,-50,300,1050);
         gBuffer.setColor(Color.darkGray);
         gBuffer.drawRect(-50,-50,300,1050);
         
         
      	gBuffer.setColor(Color.red); //1
      	gBuffer.fillRect(0,0,75,75);
         gBuffer.setColor(Color.orange); //2
      	gBuffer.fillRect(75,0,75,75);
         gBuffer.setColor(Color.yellow); //3
      	gBuffer.fillRect(0,75,75,75);
         gBuffer.setColor(Color.green); //4
      	gBuffer.fillRect(75,75,75,75);
         gBuffer.setColor(Color.blue); //5
      	gBuffer.fillRect(0,150,75,75);
         gBuffer.setColor(purpleColor); //6
      	gBuffer.fillRect(75,150,75,75);
      	gBuffer.setColor(Color.pink); //7
       	gBuffer.fillRect(0,225,75,75);
         gBuffer.setColor(Color.black); //8
      	gBuffer.fillRect(75,225,75,75);
         gBuffer.setColor(Color.white); //creates white tool icon backdrops
         gBuffer.fillRect(0,300,150,300);
         gBuffer.fillRect(0,675,150,150);
         gBuffer.setColor(Color.black);
         gBuffer.drawRect(75,750,75,75);
         gBuffer.setColor(customColor); //custom colors
         gBuffer.fillRect(75,525,75,75);
         gBuffer.setColor(customcolor1); 
         gBuffer.fillRect(0,525,75,75);
         gBuffer.setColor(Color.lightGray); //rbg picker
         gBuffer.fillRect(0,600,150,75);
         gBuffer.setColor(Color.gray); //rbg value picker
         gBuffer.fillRect(25,625,25,50);
         gBuffer.fillRect(75,625,25,50);
         gBuffer.fillRect(125,625,25,50);
         
         gBuffer.setColor(Color.red); //rgb value displays
         gBuffer.fillRect(0,600,50,25);
         gBuffer.setColor(Color.green);
         gBuffer.fillRect(50,600,50,25);
         gBuffer.setColor(Color.blue);
         gBuffer.fillRect(100,600,50,25);
         
         gBuffer.setColor(Color.black);
         if (color1 == true)
         {
            gBuffer.drawString(Integer.toString(r1),15,617); //display r1 value
            gBuffer.drawString(Integer.toString(gr1),65,617); //display gr1 value
            gBuffer.drawString(Integer.toString(b1),115,617); //display b1 value
         }
         else
         {
            gBuffer.drawString(Integer.toString(r),15,617); //display r value
            gBuffer.drawString(Integer.toString(gr),65,617); //display gr value
            gBuffer.drawString(Integer.toString(b),115,617); //display b value
         }
         
         gBuffer.setFont(new Font("Arial",Font.BOLD,20));
         gBuffer.drawString("^",32,649);
         gBuffer.drawString("^",82,649);
         gBuffer.drawString("^",132,649);
         gBuffer.setFont(new Font("Arial",Font.BOLD,-20));
         gBuffer.drawString("^",43,655);
         gBuffer.drawString("^",93,655);
         gBuffer.drawString("^",143,655);
         gBuffer.drawRect(0,600,150,75); //draws borders of rgb picker
         gBuffer.drawRect(0,600,50,25);
         gBuffer.drawRect(50,600,50,25);
         gBuffer.drawRect(100,600,50,25);
         gBuffer.drawRect(25,625,25,25);
         gBuffer.drawRect(25,650,25,25);
         gBuffer.drawRect(75,625,25,25);
         gBuffer.drawRect(75,650,25,25);
         gBuffer.drawRect(125,625,25,25);
         gBuffer.drawRect(125,650,25,25);
         
         for (int y=0;y<6;y++) //creates borders of top twelve boxes
         {
            for (int x=0;x<2;x++)
            {
               gBuffer.drawRect(x*75,y*75,75,75);
            }
         }
         
         gBuffer.setColor(Color.white); //create boxes for 3rd column
         gBuffer.fillRect(150,0,75,825);
         gBuffer.setColor(Color.black);
         for (int y = 0;y<11;y++)
         {
            gBuffer.drawRect(150,y*75,75,75);
         }
         
         gBuffer.drawRect(160,10,55,55); //3rd column tool icons
         gBuffer.drawOval(160,95,55,35);
         gBuffer.drawOval(160,160,55,55);
         gBuffer.fillRect(160,405,55,15);
         gBuffer.fillRect(180,385,15,55);
         gBuffer.fillRect(160,480,55,15);
         
         if (setFill == true)
         {
            gBuffer.fillRect(160,535,55,55);
         }
         else
         {
            gBuffer.drawRect(160,535,55,55);
         }
         
         double twoPI = 2 * Math.PI;
         int xCoord[] = new int[sides*2];
         int yCoord[] = new int[sides*2];
         
         for (int k = 0; k < sides; k++)
         {
            xCoord[k] = (int) Math.round(Math.cos(twoPI * k/sides) * 30) + 185;
            yCoord[k] = (int) Math.round(Math.sin(twoPI * k/sides) * 30) + 265;
         }   
         g.drawPolygon(xCoord,yCoord,sides);
         
         int starSides = 2 * sides;
         for (int k = 0; k < starSides; k++)
         {
            if (k % 2 == 0)
            {
               xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * 30) + 185;
               yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * 30) + 335;
            }
            else
            {
               xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * 30)/2 + 185;
               yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * 30)/2 + 335;
            }
         }
         g.drawPolygon(xCoord,yCoord,starSides);
         gBuffer.drawRect(50,700,25,25); //arrow buttons for dotted lines
         gBuffer.drawRect(50,725,25,25);
         gBuffer.drawRect(125,700,25,25);
         gBuffer.drawRect(125,725,25,25);
         gBuffer.drawRect(25,675,50,25);
         gBuffer.drawRect(100,675,50,25);
         gBuffer.setFont(new Font("qwerty",Font.BOLD,15)); //sets back to default font
         gBuffer.drawString(Integer.toString(vNum),37,692);
         gBuffer.drawString(Integer.toString(hNum),115,692);
         gBuffer.setFont(new Font("Arial",Font.BOLD,20));
         gBuffer.drawString("^",57,724);
         gBuffer.drawString("^",132,724);
         gBuffer.setFont(new Font("Arial",Font.BOLD,-20));
         gBuffer.drawString("^",68,730);
         gBuffer.drawString("^",143,730);
         
         
         gBuffer.setColor(Color.black);
         gBuffer.drawRect(108,390,10,10);
         colorPicker(g,gBuffer);
         gBuffer.fillRect(100,410,25,20);
         gBuffer.drawLine(118,395,140,395);
         gBuffer.drawLine(118,395,140,390);
         gBuffer.drawLine(118,395,140,400);         
         
         gBuffer.setColor(Color.black);
         gBuffer.drawRect(100,400,25,40);
         gBuffer.fillRect(37-1,338-1,3,3);
         gBuffer.fillRect(112-25,338-25,50,50);
         
         for (int q = 1;q<=5;q++) // vertical/horizontal dotted line icons
         {
            gBuffer.fillRect(25-1,695-1+q*10,3,3);
            gBuffer.fillRect(70-1+q*10,725-1,3,3);
         }
         
         if (circleBrush == false)                      //circleSquare icon
               {
                  gBuffer.fillRect(12,762,50,50);
               }
               else
               {
                  gBuffer.fillOval(12,762,50,50);
               }
                  
         gBuffer.drawLine(85,760,140,815);
         
         gBuffer.setColor(Color.black);
         gBuffer.drawRect(0,450,150,75); //clear
         gBuffer.drawRect(0,525,75,75);
         gBuffer.drawRect(75,525,75,75); //erase
         gBuffer.drawRect(0,675,75,75);
         gBuffer.drawRect(75,675,75,75);
         gBuffer.drawRect(0,750,75,75); //circleSquare
         
         gBuffer.setFont(new Font("Arial",Font.BOLD,15));
         gBuffer.setColor(Color.black);
         gBuffer.drawString("Custom 2",80,568);
         gBuffer.drawString("Custom 1",5,568);
         gBuffer.drawString("Erase",20,418);
         gBuffer.drawString("Clear (Double Click)",5,493);
         
      g.drawImage (virtualMem,0,0,this);
   }
   
   public void colorPicker(Graphics g, Graphics gBuffer)
   {
      Color customColor = new Color(r,gr,b);
      Color customcolor1 = new Color(r1,gr1,b1);
      switch (numColor)
         {
            case 1: gBuffer.setColor(Color.red);
                    g.setColor(Color.red);
                    break;
            case 2: gBuffer.setColor(Color.orange);
                    g.setColor(Color.orange);
                    break;
            case 3: gBuffer.setColor(Color.yellow);
                    g.setColor(Color.yellow);
                    break;
            case 4: gBuffer.setColor(Color.green);
                    g.setColor(Color.green);
                    break;
            case 5: gBuffer.setColor(Color.blue);
                    g.setColor(Color.blue);
                    break;
            case 6: gBuffer.setColor(purpleColor);
                    g.setColor(purpleColor);
                    break;
            case 7: gBuffer.setColor(Color.pink);
                    g.setColor(Color.pink);
                    break;
            case 8: gBuffer.setColor(Color.black);
                    g.setColor(Color.black);
                    break;
            case 9: gBuffer.setColor(Color.white);
                    g.setColor(Color.white);
                    break;
            case 10: gBuffer.setColor(customColor);
                    g.setColor(customColor);
                    break;
            case 11: gBuffer.setColor(customcolor1);
                    g.setColor(customcolor1);
                    break;
         }
   }
   
   public void tools(Graphics g)
   {
      switch (numTool)
            {
               case 1:{}
               
                  gBuffer.drawLine(xClick,yClick,penx,peny);
                  penx = xClick;
                  peny = yClick;
                  
                  break;
               case 2:
                  if (circleBrush == false)
                  {
                     gBuffer.fillRect(xClick-sides*5/2,yClick-sides*5/2,sides*5,sides*5);
                  }
                  else
                  {
                     gBuffer.fillOval(xClick-sides*5/2,yClick-sides*5/2,sides*5,sides*5);
                  }
                  break;
               case 4:
                  if (circleBrush == false)
                  {
                     for (int d = 0; d < 150; d++)
                     {
                        int x = rand.nextInt(61) - 30;
                        int y = rand.nextInt(61) - 30;
                        gBuffer.fillRect(xClick+x,yClick+y,1,1);
                     }
                  }
                  else
                  {
                     int dots = 0;
                     while (dots < 150)
                     {
                        int x = rand.nextInt(61) - 30;
                        int y = rand.nextInt(61) - 30;
                        if (30 >= Math.sqrt(Math.pow(x,2)+Math.pow(y,2)))
                        {
                           gBuffer.fillRect(xClick+x,yClick+y,1,1);
                           dots++;
                        }
                     }
                  }
                  
                  break;
               case 5:
                  if (0 == vNum % 2)
                  {
                     int vSegment = vLength/2/vNum;
                     for (int v = 0; v < vNum/2; v++)
                     {
                        gBuffer.fillRect(xClick-1,yClick-1+vSegment*v+vSegment/2,3,3);
                        gBuffer.fillRect(xClick-1,yClick-1-vSegment*v-vSegment/2,3,3);
                     }
                  }
                  else
                  {
                     int vSegment = vLength/vNum;
                     for (int v = 0; v <= vNum/2; v++)
                     {
                        gBuffer.fillRect(xClick-1,yClick-1+vSegment*v,3,3);
                        gBuffer.fillRect(xClick-1,yClick-1-vSegment*v,3,3);
                     }
                  }
                  break;
              case 6:
                  if (0 == hNum % 2)
                  {
                     int hSegment = hLength/2/hNum;
                     for (int h = 0; h < hNum/2; h++)
                     {
                        gBuffer.fillRect(xClick-1+hSegment*h+hSegment/2,yClick-1,3,3);
                        gBuffer.fillRect(xClick-1-hSegment*h-hSegment/2,yClick-1,3,3);
                     }
                  }
                  else
                  {
                     int hSegment = hLength/hNum;
                     for (int h = 0; h <= hNum/2; h++)
                     {
                        gBuffer.fillRect(xClick-1+hSegment*h,yClick-1,3,3);
                        gBuffer.fillRect(xClick-1-hSegment*h,yClick-1,3,3);
                     }
                  }
                  break;
               }
                  
      g.drawImage (virtualMem,0,0,this);
   }
   
   public void virtualTools(Graphics g, Graphics gBuffer)
   {
      int xLength = xClick-startx;
      int yLength = yClick-starty;
      radius = (int)Math.sqrt(Math.pow(xLength,2)+Math.pow(yLength,2));
      
      double twoPI = 2 * Math.PI;
      int xCoord[] = new int[sides*2];
      int yCoord[] = new int[sides*2];
   
      switch (numTool)
      {
                  
         case 7:
                  up = false;
                  break;
         case 8: 
                  up = false;
                  break;
         case 9: 
                  up = false;
                  break;
         case 10: 
                  up = false;
                  break;
         case 11: 
                  for (int k = 0; k < sides; k++)
               	{
               	   xCoord[k] = (int) Math.round(Math.cos(twoPI * k/sides) * radius) + startx;
               	   yCoord[k] = (int) Math.round(Math.sin(twoPI * k/sides) * radius) + starty;
               	}
               	g.drawPolygon(xCoord,yCoord,sides);
                  if (setFill == true)
                  {
                     g.fillPolygon(xCoord,yCoord,sides);
                  }
                  up = false;
                  break;
         case 12: 
                  int starSides = 2 * sides;
                  for (int k = 0; k < starSides; k++)
               	{
               	   if (k % 2 == 0)
                     {
                        xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * radius) + startx;
               	      yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * radius) + starty;
                     }
                     else
                     {
                        xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * radius)/2 + startx;
               	      yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * radius)/2 + starty;
                     }
               	}
               	g.drawPolygon(xCoord,yCoord,starSides);
                  if (setFill == true)
                  {
                     g.fillPolygon(xCoord,yCoord,starSides);
                  }
                  up = false;
                  break;          
      }
   }
   
   public void rubberBands(Graphics g)
   {
      double twoPI = 2 * Math.PI;
      int xCoord[] = new int[sides*2];
      int yCoord[] = new int[sides*2];
        
      if (numTool == 7)
      {
         g.drawLine(xClick,yClick,startx,starty);
      }
      else if (numTool == 8)
      {
         g.drawRect(startx,starty,xClick-startx,yClick-starty);
      }
      else if (numTool == 9)
      {
         g.drawOval(startx,starty,xClick-startx,yClick-starty);
      }
      else if (numTool == 10)
      {
         g.drawOval(startx-radius,starty-radius,2*radius,2*radius);
      }
      else if (numTool == 11)
      {
         for (int k = 0; k < sides; k++)
         {
            xCoord[k] = (int) Math.round(Math.cos(twoPI * k/sides) * radius) + startx;
            yCoord[k] = (int) Math.round(Math.sin(twoPI * k/sides) * radius) + starty;
         }
         g.drawPolygon(xCoord,yCoord,sides);
         if (setFill == true)
                  {
                     g.fillPolygon(xCoord,yCoord,sides);
                  }
      }
      else if (numTool == 12)
      {
         int starSides = 2 * sides;
                  for (int k = 0; k < starSides; k++)
               	{
               	   if (k % 2 == 0)
                     {
                        xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * radius) + startx;
               	      yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * radius) + starty;
                     }
                     else
                     {
                        xCoord[k] = (int) Math.round(Math.cos(twoPI * k/starSides) * radius)/2 + startx;
               	      yCoord[k] = (int) Math.round(Math.sin(twoPI * k/starSides) * radius)/2 + starty;
                     }
               	}
               	g.drawPolygon(xCoord,yCoord,starSides);
                  if (setFill == true)
                  {
                     g.fillPolygon(xCoord,yCoord,starSides);
                  }
      }
   }
}
