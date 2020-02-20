import turtle
import random

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
    
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print("La ganadora es la de color {}".format(tortuga.color()[0]))
                    break # así una vez hay ganador ya no es necesario seguir la carrera, el bucle
     
if __name__ == "__main__":
    circuito = Circuito(640, 480)
    circuito.competir()