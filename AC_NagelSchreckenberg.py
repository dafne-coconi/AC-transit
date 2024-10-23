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
      return f'{self.name}'
        

class Automata:

    """Cellular Automata.py
    Class Automata
    :param value: rule
    """
    def __init__(self, vector, numautos, iteraciones, tupla_distraccion, v_max):
        self.name = f'Linear_CA_transito'
        self.vector = vector
        self.numautos = numautos
        #self.list_autos = [*range(1, self.numautos, 1)]
        self.list_autos = list()
        self.pos_autos = list()
        self.iteraciones = iteraciones
        self.estados = 2
        self.matrix_CA = np.array([])
        self.tupla_distraccion = tupla_distraccion
        self.v_max = v_max

    def move_auto(self, auto):
        # ---- aceleracion ----------
        v_actual = auto.velocidad
        if auto.velocidad <  self.v_max:
            v_actual = min(auto.velocidad + 1, self.v_max)
        
        # ---- distancia segura -----
        # Calcular distancia del auto
        next_auto = auto.num_auto + 1 if auto.num_auto + 1 < self.numautos else 0
        #print(f'next auto {next_auto}')
        
        if self.pos_autos[next_auto] > self.pos_autos[auto.num_auto]:
            distancia_auto = self.pos_autos[next_auto] - self.pos_autos[auto.num_auto]
        else:
            distancia_auto = self.vector - self.pos_autos[auto.num_auto] + self.pos_autos[next_auto]
        
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
        self.matrix_CA = np.ones([self.iteraciones + 1, self.vector])

        # give position to cars
        self.pos_autos = random.sample(range(self.vector), self.numautos)
        self.pos_autos.sort()

        # give velocity to cars and distraction
        for auto in range(self.numautos):
            v = random.randint(0, self.v_max)
            new_auto = Auto(auto, self.pos_autos[auto], v, random.random())
            val_min = v if v > 0 else 0.7
            self.matrix_CA[0][self.pos_autos[auto]] = 1 - (val_min / self.v_max)
            self.list_autos.append(new_auto)
            print(f'auto {auto} velocidad {v} pos {self.pos_autos[auto]}')

        # actualizar autos        
        for it in range(self.iteraciones):
            for car in self.list_autos:
                car.velocidad = self.move_auto(car)
                if car.posicion + car.velocidad > self.vector - 1:
                    car.posicion = car.posicion - self.vector + car.velocidad 
                else: 
                    car.posicion = car.posicion + car.velocidad
                
                self.pos_autos[car.num_auto] = car.posicion
                val_min = car.velocidad if car.velocidad > 0 else 0.7
                color_celda = 1 - (val_min / self.v_max)

                # Change cell
                self.matrix_CA[it+1][car.posicion] = color_celda
                print(f'auto {car} velocidad {car.velocidad} pos {car.posicion}')

        return self.matrix_CA
    
    def __repr__(self):
      return f'{self.matrix_CA}'


    

class Graph_cellular:
    """Cellular Automata.py"""

    def __init__(self, data):
        self.data = data

    def graph(self, vector, nautos):
        plt.imshow(self.data, cmap='gray', interpolation='none')
        plt.title(f"Cellular Automata {vector} Num Autos {nautos}")
        plt.savefig('images/CA_{0}.png'.format(vector))

        # Add a color bar for reference (optional)
        plt.colorbar()

        # Display the plot
        plt.show()
        