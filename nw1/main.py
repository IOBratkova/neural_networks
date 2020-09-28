# i = [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
# o = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]

from mainwindow import Widget

from nw1.classes.neuron import Neuron

if __name__ == '__main__':
    window = Widget()
    window.start()

    rows = columns = 5
    neuron = Neuron(rows*columns, 1, None)
    print(neuron.w_list)
