from flask import Flask,request, session, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__);
app.config['SQLALCHEMY_DATABASE_URI']  =  'sqlite:///database/productos.db'
DB = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/productos')
def productos():
    return render_template('productos/productos.html');

@app.route('/cuenta')
def cuenta():
    return render_template('cuenta/cuenta.html');

if __name__ == '__main__':
    app.run(debug=True) 