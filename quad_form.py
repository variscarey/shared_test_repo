def quad_form(a,b,c):

    from math import sqrt
    ''' expects inputs a,b,c, coefficients of ax^2+bx+c, returns tuple of roots. '''
    discrim=b**2-4*a*c
    root1=(-b+sqrt(discrim))/(2*a)
    root2=(-b-sqrt(discrim))/(2*a)
    return root1,root2
    
