import torch
import torch.nn as nn
from torch.nn.modules.module import _addindent
from torch.autograd import Variable
import numpy as np
from dface.core.models import PNet,RNet,ONet,LossFn

def torch_summarize(model, show_weights=True, show_parameters=True):
    """Summarizes torch model by showing trainable parameters and weights."""
    tmpstr = model.__class__.__name__ + ' (\n'
    for key, module in model._modules.items():
        # if it contains layers let call it recursively to get params and weights
        if type(module) in [
            torch.nn.modules.container.Container,
            torch.nn.modules.container.Sequential
        ]:
            modstr = torch_summarize(module)
        else:
            modstr = module.__repr__()
        modstr = _addindent(modstr, 2)

        params = sum([np.prod(p.size()) for p in module.parameters()])
        weights = tuple([tuple(p.size()) for p in module.parameters()])

        tmpstr += '  (' + key + '): ' + modstr 
        if show_weights:
            tmpstr += ', weights={}'.format(weights)
        if show_parameters:
            tmpstr +=  ', parameters={}'.format(params)
        tmpstr += '\n'   

    tmpstr = tmpstr + ')'
    return tmpstr

class Model(nn.Module):

    def __init__(self):
        super(Model,self).__init__()

        self.conv0 = nn.Conv2d(1, 16, kernel_size=3, padding=5)
        self.conv1 = nn.Conv2d(16, 32, kernel_size=3)

    def forward(self, x):
        h = self.conv0(x)
        h = self.conv1(h)
        return h

model = RNet(is_train=False, use_cuda=True)

print(torch_summarize(model))

# Summarize Model
from pytorch_modelsummary import ModelSummary

ms = ModelSummary(model, input_size=(1, 3, 12, 12))

