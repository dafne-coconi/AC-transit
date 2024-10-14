from AC-NagelSchreckenberg import Automata, Graph_cellular
import sys

if len(sys.argv) < 6:
    print("Please provide five arguments. Vecinos, Lenght of Vector, Num de Iteraciones y Regla")
    sys.exit()

# Getting arguments
vecinos = int(sys.argv[1])
vector = int(sys.argv[2])
iteraciones = int(sys.argv[3])
regla = int(sys.argv[4])
inital_state = int(sys.argv[5])

print(f"First argument: {vecinos}")
print(f"Second argument: {vector}")

aC = Automata(vecinos, vector, iteraciones, regla, inital_state)
data = aC.create_CA()
#print(data)
Graph_cellular(data).graph(regla, inital_state)