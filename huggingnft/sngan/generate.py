import torch
from PIL import Image
from torchvision.utils import save_image
from train import Generator


model = Generator.from_pretrained("huggingnft/dooggies")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

with torch.no_grad():
    z = torch.randn(64, 100, 1, 1, device=device)
    pixel_values = model(z)

save_image(pixel_values, "generated.png", normalize=True)
img = Image.open(f"generated.png").convert('RGBA')
img.putalpha(255)
img.save("generated.png")