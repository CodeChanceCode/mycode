#!/usr/bin/evn python3

elvis_presley = {
    'birthday': 'january-8-1935',
    'place_of_birth': 'tupelo',
    'death': 'august-16-1977',
    'AKA': 'The King',
    }

elvis_presley.update({'occupation': 'singer'})

print(elvis_presley.keys())

choice = input("Please choose one of the keys from the dictionary above: ")

value= elvis_presley.get(choice)

print(value)



