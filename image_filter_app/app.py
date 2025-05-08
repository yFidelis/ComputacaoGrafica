from flask import Flask, render_template, request, send_file
from PIL import Image
import os
from filtros import aplicar_filtro, gerar_histograma

app = Flask(__name__)

# Pastas para upload, imagens processadas e histogramas
UPLOAD_FOLDER = 'static/uploads/'
PROCESSED_FOLDER = 'static/processed/'
HISTOGRAM_FOLDER = 'static/histograms/'

# Configurando as pastas na aplicação
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER
app.config['HISTOGRAM_FOLDER'] = HISTOGRAM_FOLDER

# Criando as pastas, se não existirem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs(HISTOGRAM_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        filtro = request.form['filtro']

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Aplica o filtro selecionado
            processed_img = aplicar_filtro(filepath, filtro)
            processed_path = os.path.join(app.config['PROCESSED_FOLDER'], file.filename)
            processed_img.save(processed_path)

            # Gera histogramas da original e processada
            hist_original = gerar_histograma(filepath, file.filename, 'original')
            hist_processado = gerar_histograma(processed_path, file.filename, 'processed')

            return render_template('index.html', original=file.filename, processed=file.filename,
                                   hist_original=hist_original, hist_processado=hist_processado)

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    # Permite o download da imagem processada
    path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
