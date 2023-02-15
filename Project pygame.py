from pygame import *
init()

win=display.set_mode((1000,1000))

display.set_caption('Vidit')

x=10
y=10
w=20
h=20
v=10
ij=False
jc=10

while True:
      
      time.delay(100)
      draw.rect(win,(255,0,0),(x,y,20,20))
      display.update()

      k=key.get_pressed()

      if k[K_LEFT] and x>v:
            x-=v
      if k[K_RIGHT] and x<1000-w-v:
            x+=v
      if ij==False:
            if k[K_UP] and y>v:
                  y-=v
            if k[K_DOWN] and y<100-h-v:
                  y+=v
            if k[K_SPACE]:
                  ij=True
      else:
            if jc>=-10:
                  s=1
                  if jc<0:
                        s=-1
                  y-=((jc**2)/2)*s
            else:
                  ij=False
                  jc=10
                  

      win.fill((0,0,0))

            
      
      
            
            
