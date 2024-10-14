import numpy as np
import matplotlib.pyplot as plt
import random

class Auto:
    """This class
    :param value: rule"""

    def __init__(self, num, posicion, velocidad, distraccion):
        self.name = f'A{num}'
        self.posicion = posicion
        self.velocidad = velocidad
        self.distraccion = distraccion
        self.vecinos = list()
        self.num_auto = num

    def decimal_to_binary(self, decimal, bit):
        
        binary_str = format(int(decimal), '0{0}b'.format(bit))
        return binary_str

    def pattern(self):
        #print(f'vecninos {self.vecinos}')
        len_pattern = 2**(self.vecinos + 1)
        for i in range(len_pattern):
            pattern_t = self.decimal_to_binary(i, 3)
            self.list_pattern.append(np.array(list(pattern_t), dtype = int))
    
    def rule_called(self):
        self.list_rule = list(self.decimal_to_binary(self.rule_num, 8))

    def __repr__(self):
      return f'{self.list_pattern}'
        

class Automata:

    """Cellular Automata.py
    Class Automata
    :param value: rule
    """
    def __init__(self, vector, numautos, iteraciones, inital_state, tupla_distraccion, v_max):
        self.name = f'Linear_CA_transito'
        self.vector = vector
        self.numautos = numautos
        #self.list_autos = [*range(1, self.numautos, 1)]
        self.list_autos = list()
        self.pos_autos = list()
        self.iteraciones = iteraciones
        self.estados = 2
        self.matrix_CA = np.array([])
        self.inital_state = inital_state
        self.tupla_distraccion = tupla_distraccion
        self.v_max = v_max

    def move_auto(self, auto):
        # ---- aceleracion ----------
        v_actual = auto.velocidad
        if auto.velocidad <  self.v_max:
            v_actual = min(auto.velocidad + 1, self.v_max)
        
        # ---- distancia segura -----
        # Calcular distancia del auto
        if self.pos_auto[auto.num + 1] > self.pos_auto[auto.num]:
            distancia_auto = self.pos_auto[auto.num + 1] - self.pos_auto[auto.num]
        else:
            distancia_auto = self.vector - self.pos_auto[auto.num] + self.pos_auto[auto.num + 1]
        
        if v_actual >= distancia_auto:
            v_actual = min(v_actual, distancia_auto)

        #----- aletoriedad -------
        if random.random() >= auto.distraccion:
            if (v_actual > 0):
                v_actual = max(v_actual - 1, 0)
        
        auto.velocidad = v_actual

        return v_actual

    def create_CA(self):
        # Create matrix for CA with a single cell at the middle
        self.matrix_CA = np.zeros([self.iteraciones + 1, self.vector])

        # give position to cars
        self.pos_autos = random.sample(range(self.vector), self.numautos)
        self.pos_autos.sort()

        # give velocity to cars and distraction
        for auto in range(self.numautos):
            v = random.randint(0, self.v_max)
            new_auto = Auto(auto, self.pos_auto[auto], v, random.random())
            self.list_autos.append(new_auto)

        # actualizar autos        
        for it in range(self.iteraciones):
            for car in range(self.list_autos):
                car.velocidad = self.move_auto(car)
                if car.posicion + car.velocidad > self.vector:
                    car.posicion = self.vector - car.velocidad
                else: 
                    car.posicion = car.posicion + car.velocidad
                
                color_celda = 1 - (car.velocidad / self.v_max)

                # Change cell
                self.matrix_CA[it+1][car.posicion] = color_celda

        return self.matrix_CA
    
    def __repr__(self):
      return f'{self.matrix_CA}'


    

class Graph_cellular:
    """Cellular Automata.py"""

    def __init__(self, data):
        self.data = data

    def graph(self, regla, initial_state):
        plt.imshow(self.data, cmap='gray', interpolation='none')
        plt.title(f"Cellular Automata {regla}")
        plt.savefig('CA_{0}_{1}.png'.format(initial_state, regla))

        # Add a color bar for reference (optional)
        plt.colorbar()

        # Display the plot
        plt.show()
        