list = []
list_size = 3
suma = 0
for i in range(list_size):
    element = input("add element to list: ")
    list.append(element)
for i in range(list_size):
 if list[i].isdigit():
     suma += int(list[i])
print(suma)