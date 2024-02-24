import torch

def check_cuda_devices():
    if torch.cuda.is_available():
        print("CUDA devices are available.")
        num_devices = torch.cuda.device_count()
        print(f"Number of CUDA devices: {num_devices}")
        for i in range(num_devices):
            print(f"Device {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA is not available on this system.")

if __name__ == "__main__":
    check_cuda_devices()
