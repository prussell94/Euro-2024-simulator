
import torch
import torch.nn as nn
import torchbnn as bnn
import torch.nn.functional as F

class BayesianNN(nn.Module):
    def __init__(self):
        super(BayesianNN, self).__init__()
        self.fc1 = torchbnn.BayesLinear(in_features=87, out_features=64, prior_mu=0.0, prior_sigma=0.1)
        self.fc2 = torchbnn.BayesLinear(in_features=64, out_features=32, prior_mu=0.0, prior_sigma=0.1)
        self.fc3 = torchbnn.BayesLinear(in_features=32, out_features=16, prior_mu=0.0, prior_sigma=0.1)
        self.fc4 = torchbnn.BayesLinear(in_features=16, out_features=1, prior_mu=0.0, prior_sigma=0.1)

    def forward(self, x):
        x = F.leaky_relu(self.fc1(x), negative_slope=0.01)
        x = F.leaky_relu(self.fc2(x), negative_slope=0.01)
        x = F.leaky_relu(self.fc3(x), negative_slope=0.01)
        x = self.fc4(x)  # No activation function here for the final layer, as it's typically used for regression
        return x