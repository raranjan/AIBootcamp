import torch
from torch import nn, autograd
import torch.nn.functional as F
from logzero import logger

input_size = 3
batch_size = 5
output_size = 1
hidden_size = 8

# Seed will ensure that we get same random data generated everytime
torch.manual_seed(123)
input = torch.rand(5, 3) # Create tensor of size 5 x 3 (5 rows with 3 colums each)
logger.info(input.shape)

class HelloNN(nn.Module):
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
    net = HelloNN(input_size, hidden_size, output_size)
    logger.info("Created Neural Net --> {}".format(net))