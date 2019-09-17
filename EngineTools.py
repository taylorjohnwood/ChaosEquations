import pygame as pg

DEFAULT_FPS = 60

class Engine(object):
    
    def __init__(self, size=(0,0)):
        
        # Initialise the display
        if not pg.display.get_init():
            pg.display.init()
        
        self.size = size

        # Create the display surface
        self.display = pg.display.set_mode(size)

        # Internal Clock that tracks time
        self.clock = pg.time.Clock()


        # List that stores children frames that this engine handles
        self.children = []

    def sendEventToChildren(self,event):
        # Pass events to children frames
        for child in self.children:
            child.newEvent(event)
    
    def addChild(self, child):
        child.engine = self
        self.children.append(child)

    def renderChildren(self):

        # Loop through children
        for child in self.children:

            # Only render active children
            if child.active:
                child.runUpdaters()
                self.display.blit(child,(0,0))


    def mainloop(self):
        while True:

            # Loop through events
            for event in pg.event.get():

                # Pass events to children
                self.sendEventToChildren(event)

                # If event is quit close the application
                if event.type == pg.QUIT:
                    quit()

            # Render all the children
            self.renderChildren()

            # Update the display
            pg.display.update()

            # Tick to next frame
            self.clock.tick(DEFAULT_FPS)

class Frame(pg.surface.Surface):
    def __init__(self,size=(0,0)):
        super().__init__(size)
        self.size = size
        self.rect = self.get_rect()
        self.updaters = []
        self.active = True
    
    def newEvent(self, event):
        None

    def runUpdaters(self):
        for updater in self.updaters:
            updater()

class Entity(pg.surface.Surface):
    def __init__(self):
        None


if __name__ == "__main__":

    E = Engine((300,50))
    F = Frame((200,200))
    E.addChild(F)
    # Start the engine mainloop
    E.mainloop()
