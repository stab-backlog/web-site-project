from flask import Flask, request, url_for, render_template
from classes import FromSystemToSystem, ToHtml
from xml.sax.saxutils import escape

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/numeral_system', methods=['POST', 'GET'])
def numeral_system():
    if request.method == 'GET':
        return render_template('numeral_system.html')

    elif request.method == 'POST':
        ton = request.form['ton']
        tons = request.form['tons']
        tdns = request.form['tdns']

        answer = FromSystemToSystem()

        num = answer.get_number(ton, tons, tdns)

        to_html = ToHtml()

        return to_html.transfer(num[0], num[1])


@app.route('/change', methods=['POST', 'GET'])
def change():
    if request.method == 'GET':
        return render_template('change.html')

    elif request.method == 'POST':
        f_text = escape(request.form['f_text'])
        s_text = escape(request.form['s_text'])
        switch = request.form['switch']

        to_html = ToHtml()

        if switch == 'tog':
            return to_html.text_tog(f_text, s_text)
        elif switch == 'sep':
            return to_html.text_sep(f_text, s_text)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
