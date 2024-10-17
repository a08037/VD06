from flask import render_template, request, redirect, url_for
from app import app

# Инициализация списка для хранения анкет
users = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Извлечение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Проверка, что все данные введены
        if name and city and hobby and age:
            # Добавление данных пользователя в список
            users.append({
                'name': name,
                'city': city,
                'hobby': hobby,
                'age': age
            })
            # Перенаправление на главную страницу
            return redirect(url_for('index'))

    # Передача списка users в шаблон
    return render_template('form.html', users=users)
