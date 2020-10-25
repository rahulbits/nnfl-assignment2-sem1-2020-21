import torch
import torch.nn as nn

from ConvS2S import ConvEncoder
from Attention import MultiHeadAttention, PositionFeedforward

class Encoder(nn.Module): # 1 Mark
    def __init__(self, conv_layers, hidden_dim, feed_forward_dim=2048):
        super(Encoder, self).__init__()
        # Your code here


    def forward(self, input):
        """
        Forward Pass of the Encoder Class
        :param input: Input Tensor for the forward pass. 
        """
        # Your code here

