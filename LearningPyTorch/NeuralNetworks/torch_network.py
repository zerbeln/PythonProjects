import torch
import numpy as np


class TorchNetwork(torch.nn.Module):
    def __init__(self, n_inp=8, n_hid=10, n_out=2):
        super().__init__()
        self.l1 = torch.nn.Linear(n_inp, n_hid)  # Layer 1 Weights
        self.l1.requires_grad_(False)
        self.l2 = torch.nn.Linear(n_hid, n_out)  # Layer 2 Weights
        self.l2.requires_grad_(False)

        self.n_inputs = n_inp
        self.n_hidden = n_hid
        self.n_outputs = n_out

    def get_weights(self, weights):
        """
        Take network weights from CCEA, convert from numpy array to tensor
        """
        self.l1.weight.data = torch.from_numpy(np.transpose(weights['L1'][0:self.n_inputs, :]))
        self.l1.bias.data = torch.from_numpy(weights['L1'][self.n_inputs, :])

        self.l2.weight.data = torch.from_numpy(np.transpose(weights['L2'][0:self.n_hidden, :]))
        self.l2.bias.data = torch.from_numpy(weights['L2'][self.n_hidden, :])

    def run_network(self, inputs):
        """
        Run the rover neural network and convert inputs from a numpy array to a tensor
        """
        network_inputs = torch.from_numpy(inputs)
        x1 = torch.nn.functional.sigmoid(self.l1(network_inputs))
        outputs = torch.nn.functional.sigmoid(self.l2(x1))

        return outputs
