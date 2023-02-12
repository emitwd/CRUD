from flask import Flask
from flask import render_template

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/productos')
def productos():
    return render_template('productos/productos.html');

@app.route('/cuenta')
def cuenta():
    return render_template('cuenta/cuenta.html');


app.run(debug=True)