import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset, random_split
from logzero import logger
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

lr = 0.01
epoch = 50

# determine the supported device
def get_device():
    return torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

class IrisNet(nn.Module):
    def __init__(self, inputs, output, hidden):
        super(IrisNet, self).__init__()
        self.inputs = inputs
        self.hidden = hidden
        self.output = output

        # Creating skeleton of the Neural Network
        self.fc1 = nn.Linear(inputs, hidden)
        self.fc2 = nn.Linear(hidden, output)

    def forward(self, x):
        x = F.relu((self.fc1(x)))
        x = self.fc2(x)

        return x


class IrisDataset(Dataset):
    def __init__(self, data, features, label):
        self.X = data[features].astype(np.float32).values
        self.y = data[label].astype(np.float32).values.reshape(-1, 1)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, item):
        return [self.X[item], self.y[item]]


def data_loader():
    data = pd.read_csv("../data/iris.csv").iloc[:,0:4]
    logger.info("Loaded Iris Data with size: {}".format(len(data)))

    features = ['sepal_length', 'sepal_width', 'petal_length']
    label = ['petal_width']

    train_data, test_data = train_test_split(data, train_size=0.6)
    logger.info("No of train dataset: {} and No of test dataset:{}".format(len(train_data), len(test_data)))

    train_dataset = IrisDataset(train_data, features, label)
    test_dataset = IrisDataset(test_data, features, label)

    return train_dataset, test_dataset


def train(net, train_dataset):
    optimizer = optim.SGD(params=net.parameters(), lr=lr)
    criteria = nn.MSELoss()
    trainloader = DataLoader(train_dataset, batch_size=10, shuffle=True)

    for i in range(epoch):
        running_loss = 0
        for data in trainloader:
            inputs, label = data[0], data[1]
            optimizer.zero_grad()
            output = net(inputs)
            loss = criteria(output, label)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
        logger.info("Epoch: {}, Loss: {}".format(i + 1, running_loss / len(trainloader)))
    logger.info("Training complete")

def test(net, test_dataset):
    running_loss = 0
    criteria = nn.MSELoss()
    testloader = DataLoader(test_dataset, batch_size=1, shuffle=True)

    with torch.no_grad():
        for data in testloader:
            inputs, label = data[0], data[1]
            output = net(inputs)
            loss = criteria(output, label)
            running_loss += loss.item()

        logger.info("Loss on test data: {}".format(running_loss/len(testloader)))

if __name__ == '__main__':
    device = get_device()
    logger.info("Using device: {}".format(device))
    net = IrisNet(3, 1, 10).to(device)
    logger.info("Created neural net:\n{}".format(net))
    train_dataset, test_dataset = data_loader()
    train(net, train_dataset)
    test(net, test_dataset)