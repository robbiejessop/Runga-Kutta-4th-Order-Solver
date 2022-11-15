# RK4
print('Enter DE to be solved: ')
func = input("f'(x) = ")

def f(x,y):
    return eval(func)

def rk4(x0,y0,xn,n):
    h = (xn-x0)/n
    print('\n--------SOLUTION--------')
    print('-------------------------')
    print("f'(x) =",func)
    print('-------------------------')
    print('x0\ty0\tyn')
    print('-------------------------')
    for i in range(n):
        f1 = f(x0, y0)
        f2 = f(x0+h/2, y0+(h/2)*f1)
        f3 = f(x0+h/2, y0+(h/2)*f2)
        f4 = f(x0+h, y0+h*f3)
        yn = y0 + (h/6)*(f1+2*f2+2*f3+f4)
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        print('-------------------------')
        y0 = yn
        x0 = x0 + h    
    print('\nAt x = %.4f, y = %.4f' %(xn,yn))
    print('\n')

print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
print('Enter calculation point: ')
xn = float(input('xn = '))
print('Enter number of steps:')
step = int(input('Number of steps = '))
rk4(x0,y0,xn,step)
