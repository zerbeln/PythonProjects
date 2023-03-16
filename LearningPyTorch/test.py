from NeuralNetworks.torch_network import TorchNetwork
from EvolutionaryAlgorithms.ea import EA
from NeuralNetworks.neural_network import NeuralNetwork
import numpy as np


eva = EA()
nn = NeuralNetwork()
tnn = TorchNetwork()

eva.create_new_population()
eva.weight_mutate()
x = np.random.normal(0, 1, 8)  # Random test input

# Hand-coded neural network
nn.get_weights(eva.population['pol0'])
print(nn.run_rover_nn(x))

# Torch neural network
tnn.get_weights(eva.population['pol0'])
print(tnn.run_network(x))


