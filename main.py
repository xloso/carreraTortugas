import turtle

class Circuito():
    corredores = [] #lista vacia
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
                
        self.__screen = turtle.Screen()
        #este interesa que sea privado para que nadie modifique la pantalla
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners()        
    
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup() #levanta el boli y no se ve la raya
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
                        
            self.corredores.append(new_turtle)
 
 
 
 
if __name__ == "__main__":
    circuito = Circuito(640, 480)