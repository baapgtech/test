import torch

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())

for i in range(torch.cuda.device_count()):
    props = torch.cuda.get_device_properties(i)
    print(
        f"GPU {i}: {props.name} | "
        f"VRAM: {props.total_memory / 1024**3:.1f} GB"
    )
