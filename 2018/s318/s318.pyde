# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s318"  # 20181112
OUTPUT = ".gif"
GRID_SIZE = 12

from line_geometry import Line
from line_geometry import par_hatch
# add_library('gifAnimation')
# from gif_exporter import gif_export

rule = lambda x, y: random(40) < 20

def setup():
    size(700, 700, P3D)
    ortho()
    init_grid(GRID_SIZE)
    background(200)
    hint(DISABLE_DEPTH_TEST)
    
def draw():
    translate(width/2, 0)
    rotateY(frameCount/7.)
    translate(-width/2, 0)
    # noStroke()
    # fill(200, 10)
    # rect(0, 0, width, height)
    background(200)
    i = 0
    while i/5. < TWO_PI:
        t = cos(i/5.)/3    
        stroke(0, 32)
        for c in Cell.cells:
            c.plot(t*5)
        i += 1
        
    f = frameCount/7.  
    # if 0 < f < TWO_PI:
    #      pass
    #      gif_export(GifMaker, SKETCH_NAME)
    # else:
    #      gif_export(GifMaker, SKETCH_NAME, finish=True)
    #      noLoop()
    #      pass

def init_grid(grid_size):
    Cell.border = 125.
    Cell.spacing = (width - Cell.border *2) / grid_size
    Cell.cells = []
    randomSeed(100)
    for x in range(0, grid_size, 2):
        for y in range(0, grid_size, 2):
                new_cell = Cell(x, y)
                Cell.cells.append(new_cell)
                Cell.grid[x, y] = new_cell
                
    randomSeed(frameCount+2) 
    for x in range(-1, grid_size+1, 2):
        for y in range(-1, grid_size+1, 2):
                Node.grid0[x, y] = Node(x, y)   # extrarir do dict
                Node.grid1[x, y] = Node(x, y)   # extrarir do dict


    for c in Cell.cells:
        c.update_vers()
   
class Node():
    grid0 = dict()
    grid1 = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing + y * Cell.spacing 
        self.pz = 0
        if rule(x, y):
           mx, my = width/2, height/2
           self.px += (self.px - mx) * 0.15 
           self.py += (self.py - my) * 0.15
           self.pz = (self.px - mx) * 0.1 + (self.py - my) * 0.10 #* random(-2, 2)
        self.x = self.px
        self.y = self.py
        self.z = self.pz

class Cell():
    cells = []
    grid = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing  + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing  + y * Cell.spacing 
        self.pz = 0
        self.vers = []
        self.num_hatches = int(random(5, 12))
        self.type_hatches = random(10)      
      
    def plot(self, t):    
        L0, V0 = self.lines, self.vers
        L1, V1 = self.lines_f, self.vers_f

        strokeWeight(1)
        for l0, l1 in zip(L0, L1):
            l = l0.lerp(l1, t)
            l.plot()
        beginShape()
        noFill()
        strokeWeight(2)
        for p0, p1 in zip(V0, V1):
            vertex(lerp(p0.x, p1.x, t),
                   lerp(p0.y, p1.y, t),
                   lerp(p0.z, p1.z, t) )
        endShape(CLOSE)
        
    def update_vers(self):
        self.v0 = Node.grid0.get((self.ix-1, self.iy-1))
        self.v1 = Node.grid0.get((self.ix-1, self.iy+1))
        self.v3 = Node.grid0.get((self.ix+1, self.iy-1))
        self.v2 = Node.grid0.get((self.ix+1, self.iy+1))
        self.vers = [self.v0, self.v1, self.v2, self.v3]
        self.v0f = Node.grid1.get((self.ix-1, self.iy-1))
        self.v1f = Node.grid1.get((self.ix-1, self.iy+1))
        self.v3f = Node.grid1.get((self.ix+1, self.iy-1))
        self.v2f = Node.grid1.get((self.ix+1, self.iy+1))
        self.vers_f = [self.v0f, self.v1f, self.v2f, self.v3f]
        self.hatch()
        
    def hatch(self):
        self.lines = []
        self.lines_f = []
        n = self.num_hatches
        r = self.type_hatches
        if r > 2:                        
            self.lines.extend(par_hatch(self.vers, n, 0))
            self.lines_f.extend(par_hatch(self.vers_f, n, 0))
        if r < 8:
            self.lines.extend(par_hatch(self.vers, n, 1))
            self.lines_f.extend(par_hatch(self.vers_f, n, 1))
        
def keyPressed():
    if key == "n" or key == CODED:
        init_grid(GRID_SIZE)
        #saveFrame("###.png")
    if key == "s": saveFrame("###.png")

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
