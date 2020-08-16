def main(): 

    import turtle 

    ttl = turtle.Turtle() 
    
    screen = turtle.Screen()
    screen.setup(800,800,0,0)
    screen.title ("Class demo of Turtle Graphics")
    screen.bgcolor ("yellow")

    ttl.penup() 
    ttl.goto(-250,0) 
    ttl.pendown() 
    ttl.circle(50) 

    ttl.fillcolor("blue") 
    ttl.penup() 
    ttl.goto(-100,0) 
    ttl.pendown() 
    ttl.begin_fill()
    ttl.circle(50) 
    ttl.end_fill() 
    
    ttl.fillcolor("red") 
    ttl.penup() 
    ttl.goto(50,0) 
    ttl.pendown() 
    ttl.begin_fill() 
    ttl.circle(50,90) 
    ttl.left(90) 
    ttl.forward(50) 
    ttl.left(90) 
    ttl.forward(50) 
    ttl.left(90) 
    ttl.end_fill() 
    
    ttl.fillcolor("green") 
	ttl.penup() 
	ttl.goto(200,0) 
	ttl.pendown() 
    ttl.begin_fill() 
    ttl.circle(50,steps=5)
    ttl.end_fill() 
	
	ttl.penup()
	ttl.goto(300,0)
	ttl.pendown()
	ttl.right(10)
	ttl.

    turtle.done() 

main() 