# i = [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
# o = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]

#from mainwindow import Widget
from mainwindownew import MyWidger

from classes.neuron import Neuron

if __name__ == '__main__':
    window = MyWidger()
    window.start()
    #
    # rows = columns = 5
    # neuron = Neuron(rows*columns, 1, None, None)
    # print(neuron.w_list)
