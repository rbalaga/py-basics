know_it = True

if(know_it):
    print('Welcome to next section.')
    print('hello')
else: print('Then learn it')


age = {''}   # True
age = {} # False
age = () #False
age = ('',) #true
age = [] #false
age = [''] #true

if age:
    print('matured')
else:
    print('minor')


num = 100

# both if 's executes
if (num >= 100):
    print('first if')
if (num == 100):
    print('second if')

# either of one will execute.
if (num >= 100):
    print('first if')
elif(num == 100):
    print('second if')
else:
    print('last block')

friends = ('ram', 'harish', 'sundeep')

if(len(friends) > 0):
    print(f'you have {len(friends)} friends')
else:
    print('You dont have friends')


if (not len(friends)==0):
    print(f'you have {len(friends)} friends')
else:
    print('you dont have friends')