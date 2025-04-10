from PIL import Image, ImageFilter, ImageChops, ImageOps
import numpy as np
import random

# Abrir imagem e converter pra escala de cinza
img = Image.open("tigre.png").convert("L")
img.save("cinza.png")

# Equalizar imagem
img_eq = ImageOps.equalize(img)
img_eq.save("equalizada.png")

# Adicionar ruído salt and pepper
arr = np.array(img)
for _ in range(500):  # pixels brancos (sal)
    x = random.randint(0, arr.shape[0] - 1)
    y = random.randint(0, arr.shape[1] - 1)
    arr[x, y] = 255
for _ in range(500):  # pixels pretos (pimenta)
    x = random.randint(0, arr.shape[0] - 1)
    y = random.randint(0, arr.shape[1] - 1)
    arr[x, y] = 0
img_ruido = Image.fromarray(arr)
img_ruido.save("ruido.png")

# Equalizar imagem com ruído
img_ruido_eq = ImageOps.equalize(img_ruido)
img_ruido_eq.save("ruido_equalizada.png")

# Filtro de borda Sobel (em cada versão da imagem)
# Original
sx = img.filter(ImageFilter.Kernel((3,3), [-1,0,1,-2,0,2,-1,0,1], 1))
sy = img.filter(ImageFilter.Kernel((3,3), [-1,-2,-1,0,0,0,1,2,1], 1))
sobel = ImageChops.add(sx, sy)
sobel.save("sobel_original.png")

# Equalizada
sx = img_eq.filter(ImageFilter.Kernel((3,3), [-1,0,1,-2,0,2,-1,0,1], 1))
sy = img_eq.filter(ImageFilter.Kernel((3,3), [-1,-2,-1,0,0,0,1,2,1], 1))
sobel_eq = ImageChops.add(sx, sy)
sobel_eq.save("sobel_equalizada.png")

# Com ruído
sx = img_ruido.filter(ImageFilter.Kernel((3,3), [-1,0,1,-2,0,2,-1,0,1], 1))
sy = img_ruido.filter(ImageFilter.Kernel((3,3), [-1,-2,-1,0,0,0,1,2,1], 1))
sobel_ruido = ImageChops.add(sx, sy)
sobel_ruido.save("sobel_ruido.png")

# Ruído + Equalizada
sx = img_ruido_eq.filter(ImageFilter.Kernel((3,3), [-1,0,1,-2,0,2,-1,0,1], 1))
sy = img_ruido_eq.filter(ImageFilter.Kernel((3,3), [-1,-2,-1,0,0,0,1,2,1], 1))
sobel_ruido_eq = ImageChops.add(sx, sy)
sobel_ruido_eq.save("sobel_ruido_equalizada.png")
