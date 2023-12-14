class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        
   
    def Perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
    
    def Surface(self):
        return self.longueur * self.largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur
    
    
    def Volume(self):
        return self.longueur * self.largeur * self.hauteur
    
monRectangle = Rectangle(8, 2)
monParallelepipede = Parallelepipede(8, 2, 3)
print("Le périmètre de mon rectangle est :", monRectangle.Perimetre())
print("La surface de mon rectangle est :", monRectangle.Surface())
print("Le volume de mon parallélépipède est :", monParallelepipede.Volume())


