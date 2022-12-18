z=100
x=500
c=400
def setup():
    size(600,600)
def draw():
    global z,x,c
    triangle(300,z,200,300,400,300)
    triangle(400,300,300,400,x,c)
    translate(10,200)
    triangle(200,100,z,200,300,200)
    z -=1
    x +=1
    c +=1
