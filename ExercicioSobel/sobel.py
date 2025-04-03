from PIL import Image, ImageFilter, ImageChops

# Carregar a imagem
imagem_colorida = Image.open("tigre.png")
imagem_colorida.save("colorida.png")

# Converter para escala de cinza
imagem_cinza = imagem_colorida.convert("L")
imagem_cinza.save("escala_cinza.png")

# Aplicar filtros na imagem colorida
sobel_x = imagem_colorida.filter(ImageFilter.Kernel((3,3), [-1,0,1,-2,0,2,-1,0,1], 1))
sobel_y = imagem_colorida.filter(ImageFilter.Kernel((3,3), [-1,-2,-1,0,0,0,1,2,1], 1))
sobel = ImageChops.add(sobel_x, sobel_y)
sobel.save("colorida_sobel.png")

laplace = imagem_colorida.filter(ImageFilter.Kernel((3,3), [0,1,0,1,-4,1,0,1,0], 1))
laplace.save("colorida_laplace.png")

prewitt_x = imagem_colorida.filter(ImageFilter.Kernel((3,3), [-1,0,1,-1,0,1,-1,0,1], 1))
prewitt_y = imagem_colorida.filter(ImageFilter.Kernel((3,3), [-1,-1,-1,0,0,0,1,1,1], 1))
prewitt = ImageChops.add(prewitt_x, prewitt_y)
prewitt.save("colorida_prewitt.png")

# Aplicar filtros na imagem em escala de cinza
sobel_x = imagem_cinza.filter(ImageFilter.Kernel((3,3), [-1,0,1,-2,0,2,-1,0,1], 1))
sobel_y = imagem_cinza.filter(ImageFilter.Kernel((3,3), [-1,-2,-1,0,0,0,1,2,1], 1))
sobel = ImageChops.add(sobel_x, sobel_y)
sobel.save("cinza_sobel.png")

laplace = imagem_cinza.filter(ImageFilter.Kernel((3,3), [0,1,0,1,-4,1,0,1,0], 1))
laplace.save("cinza_laplace.png")

prewitt_x = imagem_cinza.filter(ImageFilter.Kernel((3,3), [-1,0,1,-1,0,1,-1,0,1], 1))
prewitt_y = imagem_cinza.filter(ImageFilter.Kernel((3,3), [-1,-1,-1,0,0,0,1,1,1], 1))
prewitt = ImageChops.add(prewitt_x, prewitt_y)
prewitt.save("cinza_prewitt.png")
