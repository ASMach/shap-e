import torch
import platform

def check_device():
    if platform.system() == 'Darwin':
        print(f"Torch MPS Available: {torch.backends.mps.is_available()}")
        print(f"Torch MPS Built: {torch.backends.mps.is_built()}")
    else:
        print(torch.cuda.is_available())
        print(f"CUDA Devides: {torch.cuda.device_count()}")
        print(f"Current CUDA Index: {torch.cuda.current_device()}")

    device = None

    if platform.system() == 'Darwin':
        device = torch.device("mps")
    else:
        device = torch.device("cuda" if (torch.cude.is_available()) else 'cpu')

    return device