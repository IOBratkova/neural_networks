from l53.newuron_web_mor import NeuronWebMor

neuron_web = NeuronWebMor(2, 1, 2, (-0.5, 0.5))

neuron_web.input_neurons[0].w_list[0] = 0.2
neuron_web.input_neurons[0].w_list[1] = 0.3
neuron_web.input_neurons[1].w_list[0] = -0.3
neuron_web.input_neurons[1].w_list[1] = 0.2

neuron_web.hide_neurons[0][0].w_list[0] = -0.1
neuron_web.hide_neurons[0][0].w_list[1] = 0.2
neuron_web.hide_neurons[0][1].w_list[0] = -0.1
neuron_web.hide_neurons[0][1].w_list[1] = -0.3

neuron_web.hide_neurons[1][0].w_list[0] = 0.4
neuron_web.hide_neurons[1][1].w_list[0] = -0.2

neuron_web.output_neurons[0].w_list[0] = 0.0



patterns = [([0.5, 0.3], [1])]

neuron_web.teaching(patterns, 0.1, 1)
