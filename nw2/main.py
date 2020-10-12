# i = [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
# o = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
from window.mainwindow import *

if __name__ == '__main__':
    window = MainWindow()
    window.start()
    #
    # rows = columns = 5
    # neuron = Neuron(rows*columns, 1, None, None)
    # print(neuron.w_list)
