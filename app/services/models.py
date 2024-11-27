import torch.nn as nn

class LargeModel(nn.Module):
    def __init__(self):
        super(LargeModel, self).__init__()
        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=512, nhead=8),
            num_layers=6,
        )

    def forward(self, x):
        return self.encoder(x)

class TransformerModel(nn.Module):
    def __init__(self):
        super(TransformerModel, self).__init__()
        self.fc = nn.Linear(512, 128)  # Adjust as needed

    def forward(self, x):
        return self.fc(x)
