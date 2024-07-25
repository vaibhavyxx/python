print('Calculator')
exit = input('When you are done, enter STOP: ')

while(exit != 'STOP' or exit != 'stop'):
#without int before input you will get strings as value
#in python, {} aare replaced by indentation
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    action = input('Do you want to add, subtract, multiply or divide it? ')
    if(action == 'add'):    
        c = x+y
        print(c)
    elif(action == 'subtract'): print(x-y)
    elif(action == 'divide'): print(x/y)
    elif (action == 'multiply'): print(x*y)
    elif(action == 'STOP'): break
    else: print('Invalid option')
