from PIL import Image, ImageOps, ImageFilter
import numpy as np
import matplotlib.pyplot as plt


def aplicar_filtro(caminho_imagem, filtro):
    imagem = Image.open(caminho_imagem)

    if filtro == 'negativo':
        # Converte para RGB antes de inverter
        return ImageOps.invert(imagem.convert('RGB'))
    
    elif filtro == 'mediana':
        return imagem.filter(ImageFilter.MedianFilter(size=3))
    
    elif filtro == 'gaussiano':
        return imagem.filter(ImageFilter.GaussianBlur(radius=2))
    
    elif filtro == 'personalizado':
        return imagem.filter(ImageFilter.EDGE_ENHANCE)
    
    elif filtro == 'sobel':
        # Aplica kernel Sobel horizontal
        kernel = ImageFilter.Kernel(
            size=(3, 3),
            kernel=[-1, 0, 1, -2, 0, 2, -1, 0, 1],
            scale=1
        )
        return imagem.convert('L').filter(kernel)
    
    elif filtro == 'threshold':
        # Converte para tons de cinza antes de aplicar threshold
        imagem_gray = imagem.convert('L')
        threshold_value = 128  # valor fixo
        return imagem_gray.point(lambda p: 255 if p > threshold_value else 0)
    
    else:
        # Se o filtro não for reconhecido, retorna a imagem original
        return imagem


def gerar_histograma(caminho_imagem, nome_arquivo, tipo):
    imagem = Image.open(caminho_imagem).convert('L')
    dados = np.array(imagem).flatten()

    plt.figure(figsize=(6, 4))
    plt.hist(dados, bins=256, range=(0, 256), color='gray')
    plt.title(f'Histograma - {tipo}')
    plt.xlabel('Intensidade')
    plt.ylabel('Frequência')

    hist_path = f'static/histograms/hist_{tipo}_{nome_arquivo}.png'
    plt.savefig(hist_path)
    plt.close()

    return f'hist_{tipo}_{nome_arquivo}.png'
