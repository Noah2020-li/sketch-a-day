

def setup():
    size(400, 400)
    colorMode(HSB)

def draw():
    background(200)
    #rect(0, 0, width, height)
    r = 100  # radius
    x1, y1 = 100, 200
    x2, y2 = 300, 200
    for i in range(64):
        stroke(i * 4, 200, 200)
        a1 = i * TWO_PI / 64 + frameCount/10.
        sx1 = x1 + cos(a1) * r * cos(frameCount/20.)
        sy1 = y1 + sin(a1) * r * cos(frameCount/20.)
        a2 = i * TWO_PI / 64
        sx2 = x2 + cos(a2) * r * sin(frameCount/20.)
        sy2 = y2 + sin(a2) * r * sin(frameCount/20.)
        line(sx1, sy1, sx2, sy2)