import torch

if torch.cuda.is_available():
    device = torch.device("cuda")  # a CUDA device object
    print('GPU is available')
else:
    device = torch.device("cpu")
    print('GPU is not available, using CPU')