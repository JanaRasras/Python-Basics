
'''
'''
def circle_area(r):
    if r < 0 :
        raise ValueError('The radius cant  be negative')
    return pi*(r**2)
    