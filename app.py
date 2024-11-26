from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql


pymysql.install_as_MySQLdb()

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/Biblio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  


db = SQLAlchemy(app)


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))


@app.route('/')
def index():

    livros = Livro.query.all()  
    return render_template('index.html', livros=livros)  

if __name__ == '__main__':
    app.run(debug=True)
