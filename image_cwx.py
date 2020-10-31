from PIL import Image
pil_im = Image.open('empire.jpg')

pil_im = Image.open('empire.jpg').convert('L')

