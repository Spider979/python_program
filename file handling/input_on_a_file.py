open("input.txt","a")
while 1!=0:
    with open("input.txt","a") as file:
        aa=input("enter name ")
        file.write(f'{aa}\n')
    
    bb=int(input('1.add more name \n2.exit'))
    if bb==1:
        pass
    elif bb==2:
        break
    else:
        print('invalid input')

print('|| FILE CONTENT  ||')
with open("input.txt","r") as file:
    print(file.read())