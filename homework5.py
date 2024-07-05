immutable_var = (18, 6, 'm5 f90', 18.6)
print(immutable_var)
print(immutable_var[1])
print(type(immutable_var))
#immutable_var[0]= 30  нельзя изменить, так как переменые типа tuple
mutable_list = ['car','vehicle','automobile']
print(mutable_list)
mutable_list[1] = 'truck'
mutable_list.append('motorbike')
print(mutable_list) #переменные одного типа list
