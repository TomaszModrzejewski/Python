import turtle 

colors = ["red", "cyan", "green", "yellow", "White", "orange"]

kashyap = turtle.Turtle()
turtle.Screen().bgcolor('black')
kashyap.speed(0)

for i in range(200):
    kashyap.color(colors[i%6])
    kashyap.width(i/100 + 1)
    kashyap.forward(i)
    kashyap.left(59)
kashyap.forward(20)
turtle.done()
