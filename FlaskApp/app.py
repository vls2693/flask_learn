from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    text2 = request.form['text2']
    text2int = int(text)
    text2int2 = int(text2)
    summ = text2int + text2int2
    processed_text = str(summ)
    return processed_text

if __name__ == "__main__":
    app.run()






#http://thewebland.net/development/python/flask/mega-tutorial-part-1-hello-world/
#https://code.tutsplus.com/ru/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
'''
пример добавления строки в форму
http://www.html.by/threads/13985-Dobavlenie-polej-formy-po-nazhatiju-na-knopku
'''