import pytest
from circle import Circle

def test_init_circle_with_no_parameters():
    with pytest.raises(ValueError) as init_exception:
        circle = Circle()
        assert init_exception == 'at least one lement between radius and diameter must be defined'
        
def test_init_circle_with_incompatible_parameters():
    with pytest.raises(ValueError) as init_exception:
        circle = Circle(1,4)
        assert init_exception == 'Radius value and diameter value are incompatible'
        
def test_init_circle_with_string_parameters():
    with pytest.raises(TypeError) as init_exception:
        circle = Circle('cane',4)
        assert init_exception == 'Radius value and diameter value must be a number'
        
def test_init_circle_with_negative_parameters():
    with pytest.raises(ValueError) as init_exception:
        circle = Circle(-5,-10)
        assert init_exception == 'parameters must be positive'

def test_generate_diameter_from_radius():
    test_circle1=Circle(radius=3.5)
    assert test_circle1.diameter==7
    
def test_generate_radius_from_diameters():
    test_circle2=Circle(diameter=11)
    assert test_circle2.radius==5.5
    
def test_generate_area():
    test_circle3=Circle(4,8)
    assert round(test_circle3.area,3)==50.265
    
def test_circle_greater_than_other():
    test_circle4=Circle(4)
    test_circle5=Circle(7)
    assert test_circle5>test_circle4
    
def test_circle_lesser_than_other():
    test_circle6=Circle(2)
    test_circle7=Circle(5)
    assert test_circle6<test_circle7
    
def test_circle_equal_than_other():
    test_circle8=Circle(3)
    test_circle9=Circle(3)
    assert test_circle8==test_circle9
    
    
    