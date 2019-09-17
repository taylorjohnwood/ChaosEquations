from EngineTools import *
TIME_DIVISOR = 100

POINT_COLOURS =[
    (100,0,0),
    (0,100,0),
    (0,0,100)

]
GameEngine = Engine((500,500))

class Window(Frame):
    def __init__(self,size=(0,0)):
        super().__init__(size)
        self.initGUI()

        self.engine = None
        self.numPoints = 30
        self.points = pg.sprite.Group()
        

    def createPoints(self):
        for i in range(self.numPoints):
            
            self.points.add(pg.sprite.Sprite())

    def initGUI(self):
        self.fill((50,100,200))
    
    def updatePoints(self,equation):
        self.points[0]
        

window = Window((500,500))
window.createPoints()
GameEngine.addChild(window)
GameEngine.mainloop()
    
    
    
