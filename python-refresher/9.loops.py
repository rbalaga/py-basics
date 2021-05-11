friends = ['ram','vignesh','rajesh','harish', 'sundeep','lohit','sudheer'];

for friend in friends:
    if (friend.startswith('s')):
        print(friend)


grades = (90,98,94,54,97,95)
total = 0

for grade in grades:
    total+=grade

average = total / len(grades)
print(f'average {average}')




for friend in range(3,4):    # range(4)   gives first 0,1,2,3
    print(f'friend {friends[friend]}')