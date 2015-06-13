canada=False
country = input('Enter your country name').upper()
order_total=float(input('Enter the total cost of the of the order:')
if country=='CANADA':
    canada=True
if canada
    province=input('Enter your province')
    if province.upper()=='ALBERTA':
        order_total=order_total+order_total*0.05
    elif province.upper() in ['ONTARIO','NEW BRUNSWICK','NOVA SCOTIA']:
        order_total=order_total+order_total*0.13
    else:
        order_total=order_total+order_total*(0.06+0.05)
print('Your order total is {0:f} /n Thank you for shopping'.format(order_total))