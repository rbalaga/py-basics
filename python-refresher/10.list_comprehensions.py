friends = ['ram','sujani','rajesh','vignesh']

people = [person for person in friends] #  copies all friends list into prople list.

# for person in friends:
#     people.append(person)

print(people)  # gives all the peoples list.  ['ram', 'sujani', 'rajesh', 'vignesh']

starts_r = [person for person in friends if person.startswith('r')]

print(starts_r)  # ['ram', 'rajesh']

# for person in friends:
#     if person.startswith('r'):
#         starts_r.append(person)