# FixedPositionalEncoding implementation in NeMo
# Find more in NeMo/nemo/collections/nlp/modules/common/transformer/transformer_modules.py
import math
import numpy as np
import torch
import matplotlib.pyplot as plt

hidden_size=512        
max_sequence_length=768
pos_enc = torch.zeros(max_sequence_length, hidden_size)
position = torch.arange(0.0, max_sequence_length).unsqueeze(1)
coef = -math.log(10000.0) / hidden_size
div_term = torch.exp(coef * torch.arange(0.0, hidden_size, 2))
pos_enc[:, 0::2] = torch.sin(position * div_term)
pos_enc[:, 1::2] = torch.cos(position * div_term)
pos_enc.div_(math.sqrt(hidden_size))
T=pos_enc.cpu().detach().numpy()



plt.figure(figsize=(50,20))
plt.plot(T)
plt.show()