
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
#Создание таблицы
class Card(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    #Описание
    #Текст
    text = db.Column(db.Text, nullable=False)

    #Вывод объекта и id
    def __repr__(self):
        return f'<Card {self.id}>'
    
#Задание №1. Создать таблицу User
class User(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100),  nullable=False)
    password = db.Column(db.Text,  nullable=False)
    
#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')
#Динамичные скиллы
@app.route('/', methods=['GET','POST'])
def process_form():
    cards = Card.query.order_by(Card.id).all() 
    if request.method == 'POST': 
        login = request.form['email']
        password = request.form['text']
        #Задание №3. Реализовать запись пользователей
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()

    button_discord = request.form.get('button_discord')
    button_python = request.form.get('button_python')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python
                           ,button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db,login=login,password=password,cards=cards)

    


if __name__ == "__main__":
    app.run(debug=True)