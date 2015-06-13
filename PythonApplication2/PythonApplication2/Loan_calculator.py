print('welcome to loan calculator')
l=float(input('Input the loan amount '))
i=float(input('Input the interest percentage '))
n=float(input('Input the number of payments '))
i=i/100
print(i)
#calculating the monthly payment using the formula
m=l*(i*(1+i)*n)/((1+i)*n-1)
print('Monthly payment for your given input is {0:f}'.format(m))