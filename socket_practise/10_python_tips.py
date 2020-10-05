# https://www.youtube.com/watch?v=C-gEQdGVXbk


class People():
    pass


people = People()

people.abc = 123

dict_to_use = {'name': 'Diminished Seven', 'gender': 'Male'}

# print(people.abc)
# print(people.name)

for key, value in dict_to_use.items():
    # print(key, value)
    setattr(people, key, value)

# print(people.name)

# for att in dir(people):
#     if not att.startswith('__'):
#         print(att)

# print([att for att in dir(people) if not att.startswith('__')])

print('ab \
      // cd')
