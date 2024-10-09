import numpy as np
import matplotlib.pyplot as plt

class Rules:
    """This class
    :param value: rule"""

    def __init__(self, rule_num, vecinos):
        self.rule_num = rule_num
        self.list_pattern = list()
        self.list_rule = list()
        self.vecinos = vecinos

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
    def __init__(self, vecinos, vector, iteraciones, regla, inital_state):
        self.name = f'Linear_CA_{regla}'
        #self.vecinos = vecinos
        self.vector = vector
        self.iteraciones = iteraciones
        self.estados = 2
        self.matrix_CA = np.array([])
        self.inital_state = inital_state

    def create_CA(self):
        # Create matrix for CA with a single cell at the middle
        
        self.matrix_CA = np.zeros([self.iteraciones + 1, self.vector])

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
        