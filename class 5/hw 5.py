import turtle

import time

"""
for k in range(60):
    turtle.right(6 * k)
    turtle.forward(100)
    turtle.home()
    turtle.clear()
    time.sleep(1)
turtle.done()
"""
turtle.penup()
for e in range(8):
    turtle.forward(100)
    turtle.stamp()
    turtle.home()
    turtle.right(60 * e)
