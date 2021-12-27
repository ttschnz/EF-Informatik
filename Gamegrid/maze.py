import gamegrid, random, time
from threading import Timer

class Player(gamegrid.Actor):
    def __init__(self, gameMaze):
        gamegrid.Actor.__init__(self, "sprites/animal.gif")
        self.maze = gameMaze
        
    def isLegalMove(self, x,y):
        if gamegrid.isInGrid(gamegrid.Location(x,y)) and self.maze.maze[y][x] == False:
            return True
        self.maze.timeLeft-=10
        self.maze.updateStatus()
        return False
    
    def checkHasWon(self):
        if self.maze.targetPos["x"]==self.getX() and self.maze.targetPos["y"]==self.getY():
            self.maze.score+=1
            self.maze.timeLeft+=random.randint(1, 5)
            self.maze.updateStatus()
            self.maze.generateNewTarget()
    
    def setPosInGrid(self, x,y):
        if self.isLegalMove(x,y):
            self.setX(x)
            self.setY(y)    

    def handleMove(self,e):
        keyCode = e.getKeyCode()
        if keyCode in [37, 65]: # left
          self.setPosInGrid(self.getX()-1, self.getY())
        elif keyCode in [38,87 ]: # up
          self.setPosInGrid(self.getX(), self.getY()-1)
        elif keyCode in [39, 68]: # right
          self.setPosInGrid(self.getX()+1, self.getY())
        elif keyCode in [40, 83]: # down
          self.setPosInGrid(self.getX(), self.getY()+1)
        else:
            print(keyCode)
        self.checkHasWon()
        self.maze.grid.refresh()
        return
    
    def act(self):
        return

class TargetField(gamegrid.Actor):
    def __init__(self,x,y):
        gamegrid.Actor.__init__(self, "sprites/snaketail.gif")

class Wall(gamegrid.Actor):
    def __init__(self,x,y):
        gamegrid.Actor.__init__(self, "sprites/squaretarget.gif")
    
class Maze:
    def __init__(self,**kwargs):
        self.height = kwargs["height"] if "height" in kwargs else 10
        self.width = kwargs["width"] if "width" in kwargs else 10
        self.startPos={}
        self.startPos["x"] = kwargs["startPosX"] if "startPosX" in kwargs else 1
        self.startPos["y"]= kwargs["startPosY"] if "startPosY" in kwargs else 1
        self.player = Player(self)
        self.grid = gamegrid.makeGameGrid(self.width,self.height,90,None, "", False, keyPressed = self.player.handleMove)
        self.grid.setTitle("Maze")
        self.grid.addActor(self.player, gamegrid.Location(self.startPos["y"], self.startPos["y"]))
        self.grid.show()
        self.grid.addStatusBar(20)
        self.createMaze()
        self.score=0
        self.timeLeft = 30
        self.targetField=False
        self.isGameOver=False
        self.generateNewTarget()
        self.startInterval()
        
    def gameOver(self):
        self.isGameOver=True
        self.grid.removeActor(self.player)
        self.grid.removeActor(self.targetField)
        for i in self.maze:
            for j in i:
                if j:
                    self.grid.removeActor(j)
        self.grid.setStatusText("Game Over! Score: {0}".format(self.score))

    def updateStatus(self):
        self.grid.setStatusText("Score: {0}, Time: {1}".format(self.score, self.timeLeft))
        if(self.timeLeft<0):
            self.gameOver()

    def startInterval(self):
        self.timeLeft-=1
        self.updateStatus()
        Timer(1, self.startInterval).start()
        
    def generateNewTarget(self):
        if(self.targetField):
            self.grid.removeActor(self.targetField)
            self.targetField = False
        self.targetPos = self.getRandomLocation()
        
    def getRandomLocation(self):
        x,y=0,0
        while not self.maze[y][x] == False:
            x, y = random.randint(0, self.width-1), random.randint(0,self.height-1)
        self.targetField = TargetField(x,y)
        self.grid.addActor(self.targetField, gamegrid.Location(x,y))
        return {"x":x, "y":y}
    
    def createMaze(self):
        mazeSource = [
                        [1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,1,0,0,0,1],
                        [1,1,1,1,0,1,0,1,0,1],
                        [1,0,0,0,0,0,0,1,0,1],
                        [1,0,1,1,0,1,1,1,1,1],
                        [1,0,1,0,0,0,0,0,0,1],
                        [1,0,1,1,1,1,1,1,0,1],
                        [1,0,1,0,0,0,1,0,0,1],
                        [1,0,0,0,1,0,1,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1]
                    ]
        self.maze = []
        for y in range(self.height):
            mazeRow = []
            for x in range(self.width):
                if mazeSource[y][x]:
                    wall = Wall(x,y)
                    self.grid.addActor(wall, gamegrid.Location(x,y))
                    mazeRow.append(wall)
                else:
                    mazeRow.append(False)
            self.maze.append(mazeRow)
        

maze= Maze(height = 10, width = 10)