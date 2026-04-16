from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form10', methods=['GET', 'POST'])
def form10():
    if request.method == 'POST':
        file = request.files.get('rasm')
        if file and file.filename:
            return f"<h2>Fayl muvaffaqiyatli yuklandi!</h2><p>Fayl nomi: {file.filename}</p><br><a href='/'>Orqaga</a>"
        return "Fayl tanlanmadi!<br><a href='/'>Orqaga</a>"
    return render_template('form10.html')

if __name__ == '__main__':
    app.run(debug=True)
