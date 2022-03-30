from circle import Circle

if __name__ == '__main__':
    
    circle1=Circle(3)           
    circle1.print_circle()

    circle2=Circle(4)
    circle2.print_circle()

    circle3= circle1+circle2
    circle3.print_circle()

    circle4=Circle(3)
    print(circle1==circle4)
    print(circle1==circle3)

    circles = [                                 
            Circle(7),
            Circle(5),
            Circle(10)
        ]

    print(circles)                              
    circles.sort(key=lambda x: x.radius)        
    print(circles) 