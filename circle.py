from math import pi,sqrt

class Circle:
    def __init__(self,radius=None,diameter=None):
        if radius is None and diameter is None:
            raise ValueError('at least one element between radius and diameter must be defined')
        elif diameter is not None and radius is not None:
            if type(radius) is not str and type(diameter)is not str:
                if str(radius).startswith('-') or str(diameter).startswith('-'):
                    raise ValueError('parameters must be positive')
                if(diameter!=radius*2):
                    raise ValueError('Radius value: {radius} and diameter value: {diameter} are incompatible')
            else:
                raise TypeError('Radius value and diameter value must be a number')
                
        if radius is not None:
            self.radius=radius
            self.diameter=radius*2
            self.area=pi*radius**2
            self.name=(f'CircleWithRadiusOf{round(self.radius,3)}')
            
        else:
            self.diameter=diameter
            self.radius=diameter/2
            self.area=pi*(diameter/2)**2
            self.name=(f'CircleWithRadiusOf{round(self.diameter/2,3)}')
            
        
        
    def __repr__(self):
        return (f'{self.name}')

    def __add__(self, otherCircle):
        return Circle(sqrt((self.area + otherCircle.area)/pi))
    
    def __eq__(self, otherCircle):
        return self.area==otherCircle.area
    
    def __gt__(self, otherCircle):
        return self.radius > otherCircle.radius
    
    def __ge__(self, otherCircle):
        return self.radius >= otherCircle.radius

    def __lt__(self, otherCircle):
        return self.radius < otherCircle.radius
    
    def __le__(self, otherCircle):
        return self.radius <= otherCircle.radius
            
    def print_circle(circle):
        print(f'Radius: {round(circle.radius,3)}\t| Diameter: {round(circle.diameter,3)}\t| Area: {round(circle.area,3)}\t')