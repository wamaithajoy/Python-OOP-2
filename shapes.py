class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area_of_circle(self):
        pie=3.14
        total_radius=self.radius*self.radius
        area=pie*total_radius
        return area    

    def circumfrence(self):
        pie=2*3.14
        radius=self.radius 
        circum=pie*radius   
        return circum

class Square:
    def __init__(self,side):
        self.side=side 

    def area_of_square(self):
        area=self.side*self.side
        return area  

    def perimeter(self):
        perimeter=4*self.side
        return perimeter 
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area_of_rectangle(self):
        area=self.width*self.length
        return area 

    def perimeter(self):
        total_sides=self.width+self.length
        perimeter=2*total_sides
        return perimeter    

class Sphere:
    def __init__(self,radius):
        self.radius=radius

    def area_of_sphere(self):
        pie=3.14
        total_radius=self.radius*self.radius
        area=4*pie*total_radius
        return area 

    def volume_of_sphere(self):
        v=4/3
        pie=3.14
        total_radius=self.radius*self.radius*self.radius
        volume=v*pie*total_radius
        return volume