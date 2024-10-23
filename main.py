from AC_NagelSchreckenberg import Automata, Graph_cellular
import sys

#if len(sys.argv) < 6:
 #   print("Please provide five arguments. Vecinos, Lenght of Vector, Num de Iteraciones y Regla")
  #  sys.exit()
# self, vector, numautos, iteraciones, tupla_distraccion, v_max):
# Getting arguments
"""
vector = int(sys.argv[1])
numautos = int(sys.argv[2])
iteraciones = int(sys.argv[3])
tupla_distraccion = int(sys.argv[4])
v_max = int(sys.argv[5])
"""
vector = int(input("int value for lenght of Vector "))
numautos = int(input("int value for # of cars "))
iteraciones = int(input("int value for number of iterations "))
tupla_distraccion = tuple(input("Tuple for distraction ej. (0.2,0.8) "))
v_max = int(input("int value max velocity "))

print(f"Vector: {vector}")
print(f"Num autos: {numautos}")
print(f"Iteraciones: {iteraciones}")
print(f"tupla_distraccion: {tupla_distraccion}")
print(f"V max: {v_max}")

aC = Automata(vector, numautos, iteraciones, tupla_distraccion, v_max)
data = aC.create_CA()
#print(data)
Graph_cellular(data).graph(vector,numautos)