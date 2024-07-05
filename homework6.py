my_dict = {'pudge': 'strength', 'viper': 'universal', 'juggernaut':'agility','silencer':'intelligence'}
print(my_dict.get('pudge'))
print(my_dict.get('bounty hunter'))
my_dict.update({'phantom assassin':'agility',
                'axe':'strength'})
print(my_dict)
a = my_dict.pop('silencer')
print(a)
print(my_dict)



my_set = {15, 12, 9, 15, 6, 12, 15, 9, "axe",True, 13.6, (12,6),'axe'}
print(my_set)
my_set.update({8, 7})
print(my_set)
print(my_set.discard(15))
print(my_set)