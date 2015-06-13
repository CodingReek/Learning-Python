#setting flag to easily modify the program later
#free_toaster=False
#deposit=float(input('how much do you like to deposit: '))
#if deposit >100:
#    free_toaster=True
#if free_toaster:
#    print('You got a free toaster')
#else:
#    print('you got a free coupon ')
#print('have a nice day')
#calcualtionn for the shipping charges for the shopper
freeshipping=False
shippingcost=10
total_purchase=int(input('Enter the amount of total purchase :'))
if total_purchase >= 50:
    freeshipping=True
if freeshipping:
    print('You have a free shipping')
    print('Your total cost of the purchase is {0:d}$'.format(total_purchase))
else:
    total_purchase=total_purchase+shippingcost
    print('shipping cost is {0:d}$'.format(shippingcost))
    print('Your total cost for the purchase is {0:d}$'.format(total_purchase))
print('Thank you for shopping')