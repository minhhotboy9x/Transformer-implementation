import torch

out = torch.ones(2, 3, 4)
print(out[:, -1].shape)

decoder_input = torch.empty(1,1).fill_(1).type_as(out)
print(decoder_input.shape)