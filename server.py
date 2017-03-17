from flask import Flask, render_template, request, redirect, url_for
from typografyzing_module import Typograph

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def handle_form_request():
    origin_text = request.form['text']
    if origin_text is not None:
        typograph = Typograph(origin_text)
        typographed_text = typograph.typographed_text
        redirect(url_for('index'))
    return render_template('form.html', origin_text=origin_text, typographed_text=typographed_text)


if __name__ == '__main__':
    app.run(debug=True)
