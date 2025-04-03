from flask import Flask, request, redirect, url_for, send_file, render_template
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        
        if file1 and file2:
            path1 = os.path.join(app.config['UPLOAD_FOLDER'], '1.txt')
            path2 = os.path.join(app.config['UPLOAD_FOLDER'], '2.txt')
            file1.save(path1)
            file2.save(path2)
            
            # Lancer le script de comparaison
            subprocess.run(['python', 'comparaison.py', path1, path2])
            # Lancer le script de génération Excel (supposant que le résultat est 'result_diff.txt')
            subprocess.run(['python', 'generation_excel.py', os.path.join(app.config['UPLOAD_FOLDER'], 'result_diff.txt'),
                            os.path.join(app.config['UPLOAD_FOLDER'], 'sortie.xlsx')])
            
            return redirect(url_for('download_file'))
    return render_template('upload.html')  # Votre template HTML pour le formulaire

@app.route('/download')
def download_file():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'sortie.xlsx')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
