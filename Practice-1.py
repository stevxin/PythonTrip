import random

#生成用户信息字典
info={str(''.join(chr(random.randint(97,122)) for _ in range(3))):['{:<2}:186{:8}'.format(v,"".join(chr(random.randint(48,57)) for j in range(8)))] for v in range(50) }

for i in range(len(info)):
    enter=input('Please enter your choice:\n[delete,update,find,list,exit]\n')
    print()
    if enter == 'delete':
        userid=input('Please enter user name: ')
        dele=info.pop(userid,'No exists')
        print(dele)
    elif enter == 'update':
        print('Enter your user information,example:"username:age:phone"')
        userup=input('username:age:phonenumber :')
        userinfo=userup.split(':')

        if info.get(userinfo[0]):
            info[userinfo[0]]=[':'.join(userinfo[1:])]
        else:
            print('No exists')
        continue
    elif enter == 'list':
        print('user information:\nUsername:Age:PhoneNumber\n{}'.format(info) )
        continue
    elif enter == 'find':
        userfind=input('Please enter user name: ')
        ufind=info.get(userfind,'No exists')
        print(ufind)
    elif enter == 'exit':
        print('Quit to session.')
        break
    else:
        print('Error,Please enter your choice:\n[delete,update,find,list,exit]\n')