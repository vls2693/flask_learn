from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()






#http://thewebland.net/development/python/flask/mega-tutorial-part-1-hello-world/
#https://code.tutsplus.com/ru/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972