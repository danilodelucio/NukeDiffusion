import sys

try:
    import torch

    print("")
    print(f"- Python Version: {sys.version[:6]}")
    print(f"- Torch version: {torch.__version__}")
    available_cuda = torch.cuda.is_available()
    device_count = torch.cuda.device_count()
    device_name = torch.cuda.get_device_name()

    print("")
    if available_cuda:
        print("- CUDA is available!")
        print(f"    - Device name: {device_name}")
    else:
        print("- CUDA is not available!")

except Exception as error:
    print("")
    print(f"- {error}!")