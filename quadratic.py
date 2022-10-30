# the purpose of this program is to solve quadratic equations using the quadratic formula

import math
def main():
    #get a, b, and c from user
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    #calculate discriminant
    discriminant = b**2 - 4*a*c
    #calculate x1 and x2
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    #print x1 and x2
    print('x1 =',x1)
    print('x2 =',x2)

if __name__ == '__main__':
    main()