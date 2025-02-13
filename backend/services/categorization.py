import torch
from torch_geometric.nn import GATConv # Import GAT layer from PyTorch Geometric

# Dummy GAT model definition.
class DummyGAT(torch.nn.Module):
    def __init__(self, in_channels: int, out_channels: int) -> None:
        super().__init__()
        self.gat = GATConv(in_channels, out_channels)
        
    def forward(self, x, edge_index):
        return self.gat(x, edge_index)