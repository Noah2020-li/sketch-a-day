
"""
sketch 75 180316 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Based on Recursive Tree by Daniel Shiffman.    
"""

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, porta_serial in enumerate(Arduino.list()):
    println(str(num)+":"+porta_serial)
NUM_PORTA = 0  # Find your port and change!    

add_library('gifAnimation')
from gif_exporter import gif_export

# from slider import Slider
# A = Slider(0, HALF_PI, QUARTER_PI)
# B = Slider(0, 10, 10)
# C = Slider(-2, 2, 0)
# D = Slider(2, 15, 10)

def setup():
    global arduino
    size(600, 600)
    # A.position(20, height - 60)
    # B.position(20, height - 30)
    # C.position(width - 180, height - 60)
    # D.position(width - 180, height - 30)
    arduino = Arduino(this, Arduino.list()[NUM_PORTA], 57600)

def draw():
    global c, d
    background(0)
    frameRate(30)
    stroke(255)
    strokeWeight(2)

    # a = A.value()  # Angle
    # b = B.value()  # branch size randomization
    # c = C.value()  # angle randomization
    # d = D.value()  # recursion depth
    a = map(arduino.analogRead(1), 0, 1023, 0, HALF_PI)
    b = map(arduino.analogRead(2), 0, 1023, 0, 10)
    c = map(arduino.analogRead(3), 0, 1023, -2, 2)
    d = map(arduino.analogRead(4), 0, 1023, 2, 15)
    
    randomSeed(1)
    translate(width / 2, height / 2)
    branch(d, a, width/30)

    # uncomment next line to export GIF
    #if not frameCount % 10: gif_export(GifMaker, frames=3000)

def branch(gen, theta, branch_size):
    # Each branch will be 2/3rds the size of the previous one

    
    # All recursive functions must have an exit condition!!!!
    if gen > 1 and branch_size > 1:
        h = branch_size * (1 + random(b) / 4)
        branch_size *= 1 - random(b) / 10
        # Save the current state of transformation (i.e. where are we now)
        pushMatrix()
        rotate(theta + c * random(1))  # Rotate by theta
        line(0, 0, 0, -h)  # Draw the branch
        translate(0, -h)  # Move to the end of the branch
        # Ok, now call myself to draw two branches!!
        branch(gen - 1, theta, branch_size)
        # Whenever we get back here, we "pop" in order to restore the previous
        # matrix state
        popMatrix()
        # Repeat the same thing, only branch off to the "left" this time!
        with pushMatrix():
            rotate(-theta + c * random(1))
            line(0, 0, 0, -h)
            translate(0, -h)
            branch(gen - 1, theta, branch_size)