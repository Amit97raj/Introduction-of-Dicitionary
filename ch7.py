 # Python Basics Chapter 7:
# ========================

# 1. Introduction To Dictionaries

# We use dictionaries because of limitations of lists, lists are not 
# enough to represent real data.

# Example - 
# user = ["Anshul", 22]
# this list contains user name, age 
# you can do this but this is not a good way to do this.

# Dictionaries are the unordered collection of data in key : value 
# pairs.

# We can store any type of data in dictionaries such as numbers, 
# strings, lists, dictionaries etc.

# Ways to create a dictionary -

# first way -

# user = {'name': 'Anshul', 'age': 22}

# print(user)
# print(type(user))

# second way -

# user = dict(name= 'Anshul', age= 22)

# print(user)
# print(type(user))

# Access data from dictionary -

# We use keys to access the data from dictionaries.
 
# Note : There is no indexing because of unordered collection of data.

# print(user['name'])
# print(user['age'])

# user = {
#     'name': 'Anshul', 
#     'age': 22,
#     'fav_actor': 'Sharukh Khan',
#     'fav_cricketer': 'Virat Kohli'
#     }

# print(user)
# print(user['age'])
# print(user['fav_actor'])
# print(user['fav_cricketer'])

# dictionary inside dictionary -

# users = {
#     'user1' : {
#         'name': 'Anshul', 
#         'age': 22,
#         'fav_actor': 'Sharukh Khan',
#         'fav_cricketer': 'Virat Kohli'
#     }, 

#     'user2' : {
#         'name': 'Anurag', 
#         'age': 24,
#         'fav_actor': 'Salman Khan',
#         'fav_cricketer': 'AB De Villiers'
#     } 
# }

# print(users)
# print(users['user1'])
# print(users['user2'])

# print(users['user1']["name"])
# print(users['user2']["name"])

# add data to empty dictionary -

# user = {}

# user['name'] = 'Anshul'
# user['age'] = 22

# print(user)

# # 2. Looping and In Keyword
   
# user = {
#     'name': 'Anshul', 
#     'age': 22,
#     'fav_actor': 'Sharukh Khan',
#     'fav_cricketer': 'Virat Kohli'
#     }

# # print(user)
# # print(user.keys())
# # # print(user.values())
# # print(type(user.keys()))
# # print(type(user.values()))
# # print(user.items())
# # print(type(user.items()))

# # check if key exist in dict -

# first way -

# if 'name' in user:
#     print("Present")
# else:
#     print("Not Present")

# second way -

# if 'name' in user.keys():
#     print("Present")
# else:
#     print("Not Present")

# check if value exist in dict -

# if 'Anshul' in user.values():
#     print("Present")
# else:
#     print("Not Present")

# loops in dict -

# for key in user:
#     print(key)

# for key in user.keys():
#     print(key)

# for value in user.values():
#     print(value)

# for key in user:
#     print(user[key])

# for item in user.items():
#     print(item)

# for key, value in user.items():
#     print(f"{key} : {value}")

# 3. Add and delete Data

# user = {
#     'name': 'Anshul', 
#     'age': 22,
#     'fav_actor': 'Sharukh Khan',
#     'fav_cricketer': 'Virat Kohli'
#     }

# add data -

# user['designation'] = ['Data Scientist', 'Software Developer']
# print(user)

# pop method -
# key = 'age'
# popped_item = user.pop(key)

# print(f"Popped item - {key} : {popped_item}")
# print(f"Type of Popped item : {type(popped_item)}")
# print(user)

# popitem method -

# popped_item = user.popitem()

# print(f"Popped item : {popped_item}")
# print(f"Type of Popped item : {type(popped_item)}")
# print(user)

# 4. Update Dictionary

# user = {
#     'name': 'Anshul', 
#     'age':  22,
#     'fav_actor': 'Sharukh Khan',
#     'fav_cricketer': 'Virat Kohli'
#     }

# more = {
#     'designation': 'Data scientist',
#     'passion': 'Programming',
#     'hobbies': ['music', 'poetries']
# }

# user.update(more)
# print(user)

# 5. fromkeys(), get(), copy(), clear() methods

# get() returns none when their is no any key present in dict

# user = dict.fromkeys(['name', 'age'])
# print(user)

# user = dict.fromkeys(['name', 'age'], 'unknown')
# print(user)

# user = dict.fromkeys(('name', 'age'), 'unknown')
# print(user)

# user = {
#     'name': 'Anshul', 
#     'age': 22,
#     'fav_actor': 'Sharukh Khan',
#     'fav_cricketer': 'Virat Kohli'
#     }

# print(user.get('name'))
# print(user.get('names'))

# if user.get('name'):
#     print("Present")
# else:
#     print("Not Present")

# user_copy = user.copy()
# print(user_copy)

# user.clear()
# print(user)

# 6. More about get() method

# two same keys in dict

# user = {'name': 'Anshul', 'age': 22}
# user = {'name': 'Anshul', 'age': 22, 'age': 24}

# print(user.get('name'))
# print(user.get('names', 'not found'))
# print(user.get('age'))

# 7. Exercise - 1

# define a function that takes a number (n).
# return a dictionary containing cube of numbers from 1 to n.

# 8. Exercise - 1 Solution

# def cube_finder(n):
#     cubes = {}

#     for i in range(1, n+1):
#         cubes[i] = i ** 3
    
#     return cubes

# print(cube_finder(3))

# 9. Word Counter

# def word_counter(s):
#     char_dict = {}
    
#     for ch in s:
#         char_dict[ch] = s.count(ch)

#     return char_dict

# name = input("Enter your name : ")
# print(word_counter(name))

# 10. Exercise - 2

# Take the required data from the user and create a dictionary as 
# below :

# user = {
#     'name': 'Anshul', 
#     'age': 22,
#     'fav_actor': 'Sharukh Khan',
#     'fav_cricketer': 'Virat Kohli'
#     }

# 11. Exercise - 2 Solution

# user = {}

# name, age, actor, cricketer = input("Enter your name, age, favourite actor and favourite cricketer separated by comma : ").split(',')

# user['name'] = name
# user['age'] = age
# user['fav_actor'] = actor
# user['fav_cricketer'] = cricketer

# user = dict(name=name, age=age, actor=actor, cricketer=cricketer)

# user.update(name=name, age=age, actor=actor, cricketer=cricketer)

# print(user)

# for key, value in user.items():
#     print(f"{key} : {value}")
