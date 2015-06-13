guest_list=[]
guest='0'
print('Enter the guest name one by one \n After entering allnames enter end')
while guest.upper()!='END':
    guest=input().upper()
    guest_list.append(guest)
del guest_list[-1]
guest_list.sort()
for steps in range(len(guest_list)):
    print(guest_list[steps])
print(guest_list.index('GOKUL'))