# Variables

my_variable="My String Variable"
print(my_variable)

my_int_variable=5
print(my_int_variable)

my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
my_bool_variable=False
print(my_bool_variable)

#Concatenacion de variables en un print

print(my_variable,str(my_int_variable),my_bool_variable)
print("Esta frase es",my_bool_variable)

# Funciones del sistema

print(len(my_variable))

# Variables es una sola linea

name,surname,alias,age,="Alejandro","Gemes","Ale",18
print("Me llamo:",name,surname,"Mi edad es:",age,"Y mi alias es:",alias)
# Escribir por teclado
name=input("Como te llamas")
age=input("Cuantos años tienes")
print("Me llamo:",name,"y tengo:",age)
