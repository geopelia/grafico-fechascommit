import matplotlib.pyplot as plt
dict_ejm = {0: 96, 1: 62, 2: 11, 3: 5, 5: 1,6:0}
valores_x = list(dict_ejm)
valores_y = list(dict_ejm.values())
print(valores_x)
print(valores_y)
plt.bar(valores_x, valores_y)
plt.ylabel('Cant commits')
plt.xlabel('Horas')
plt.title('Commits en determinadas horas en un repositorio')
plt.show()
