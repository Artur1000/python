state=0



class Image:
    def __init__ (self, file):
        self.img =loadImage(file)
        self.x = random( 0,700)
        self.y = random( 0,700)
        self.dx = random( 100,200)
        self.dy = random( 100,200)
    def draw_(self):
        image(self.img , self.x , self.y , self.dx , self.dy)

x = 0
y = 0
lst = []
houses = []
def setup():
    size(700,700)
    textSize(70)
    lst.append( loadImage("selol.jpg") )
    lst.append( loadImage("selo2.jpg") )
    lst.append( loadImage("selo3.jpg") )
    lst.append( loadImage("dom.png") )
    lst.append( loadImage("selo4.png") )
    lst.append( loadImage("dom1.jpg") )
    lst.append( loadImage("dom2.jpg") )   
    lst.append( loadImage("selo4.jpg") )  
def draw():
    global state
    
    if  state == 0:
        background(255)
 
   
        fill("#19FC2A")
        rect(250,360,320,120)
        fill("#4808FF")
        textSize(22)
        text('to start the game press ENTER',250,410)
   
    elif state == 1:
        
        background("#4AFF15")
        if x > 10:
            image(lst[0] , 0,0,700,700)
        if x > 20:
            image(lst[1] , 0,0,700,700)
        if x > 40:
            image(lst[2] , 0,0,700,700)
        if x > 60 :
            image(lst[4] , 0,0,700,700)
        image(lst[3] , 600,50,70,40)  
        if x > 103 :
            image(lst[5] , 0,0,700,700)
        if x > 200 :
            image(lst[6] , 0,0,700,700)
        if x > 300 :
            image(lst[7] , 0,0,700,700)
        
        
        for house in houses:
            house.draw_()
        textSize(70)
        text(x,11,60)
   
    
    
def keyPressed():

    global x,houses,state
    
    if key == ENTER:
        if state == 0:
            state = 1
        elif state ==1:
            state =0
            
    if key==' ':
        x+=1
        if len(houses) > 5:
            x +=1   
        if len(houses) > 10:
            x +=2  
        
    
    if key=='q':
       x += 100
    if key=='p':
       x += 50 
    if key == "1":
        if x > 100:
            if len(houses) < 15:
                houses.append(Image("dom2.png"))
    if key == "2":
        if x > 150:
            if len(houses) < 15:
                houses.append(Image("dom3.png"))
    if key == "3":
        if x > 200:
               if len(houses) < 15:
                houses.append(Image("dom4.png"))
