nombres = ['Juan', 'Mario', 'Pablo', 'Paula', 'Miriam']

# agregar un unico elemento por el final
nombres.append('Joaquin')
print('append', nombres)

# agregar varios elementos a la vez en una lista por el final
nombres.extend(['Miguel Angel', 'Reniel'])
print('extend', nombres)

# agregar un metodo en cualquier posicion
nombres.insert(3, 'Luis')
print('insert', nombres)

# borrar un elemento de la lista 
# metodo pringle pop()
ultimo_elemento = nombres.pop()
print(nombres)
print(ultimo_elemento)

elemento_tres = nombres.pop(3)
print(elemento_tres)

# eleminar elementos de la lista por contenido
nombres.remove('Mario')
print(nombres)