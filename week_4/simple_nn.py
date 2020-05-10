import torch
from torch import nn, autograd
import torch.nn.functional as F
from logzero import logger

input_size = 3
batch_size = 5
output_size = 1
hidden_size = 8

class SimpleNN(nn.Module):
    def __init__(self, inputs, hidden, output):
        super().__init__()
        # Creating the basic skeleton structure of neural network
        self.fc1 = nn.Linear() # First Layer
        self.fc2 = nn.Linear() # Second Layer

    def forward(self, x):
        pass

    def __getitem__(self, item):
        pass

if __name__ == '__main__':
    net = SimpleNN(input_size, hidden_size, output_size)