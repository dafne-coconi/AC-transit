import numpy as np
import matplotlib.pyplot as plt
import random

class Auto:
    """This class
    :param value: rule"""

    def __init__(self, num, posicion, velocidad, distraccion):
        self.name = f'A{num}'
        self.posicion = posicion
        self.velocidad = list()
        self.distraccion = list()
        self.vecinos = list()

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

    def create_CA(self):
        # Create matrix for CA with a single cell at the middle
        self.matrix_CA = np.zeros([self.iteraciones + 1, self.vector])

        # give position to cars
        self.pos_autos = random.sample(range(self.vector), self.numautos)
        self.pos_autos.sort()

        # give velocity to cars
        for auto in range(self.numautos):
            self.list_autos.append(Auto(auto, self.pos_auto[auto], random.randint(0, self.v_max)))


        if self.inital_state == 1:
            middle_first_v = self.vector//2
            self.matrix_CA[0][middle_first_v] = 1
        else:
            self.matrix_CA[0] = np.random.randint(0, 2, self.vector)
        
        rule = Rules(self.regla, self.vecinos)
        rule.rule_called()
        rule.pattern()

        #print(f'first CA {self.matrix_CA}')
        
        for it in range(self.iteraciones):
            for cell in range(self.vector):

                initial_cell = cell - self.vecinos + 1
                central_cell = initial_cell + (self.vecinos)//2
                #print(f'central {central_cell}')
                if cell < 2:
                    binary = np.concatenate((self.matrix_CA[it][initial_cell:], self.matrix_CA[it][:cell+1]))
                else:
                    binary = self.matrix_CA[it][initial_cell:initial_cell+self.vecinos]

                bin_to_dec = int(''.join(map(lambda binary: str(int(binary)), binary)), 2)
                #print(f'binary {binary}, dec {bin_to_dec}')

                current_pattern = rule.list_rule[-bin_to_dec-1]

                # Change central cell
                self.matrix_CA[it+1][central_cell] = current_pattern
                #print(f'matrix \n{self.matrix_CA}')

        #print(f'IS {self.inital_state}')
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
        