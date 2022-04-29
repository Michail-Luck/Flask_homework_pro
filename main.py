from flask import Flask, render_template, request
import csv
import random

app = Flask(__name__)


@app.route("/form/", methods=['POST','GET'])
def players_add():
    context = {"Имя": [], "Фамилия": [], "Номер": []}
    with open('main_base.csv', 'r') as csvfile:
        text = csv.reader(csvfile, delimiter=';')
        for row in text:
            context["Имя"].append(row[0])
            context["Фамилия"].append(row[1])
    if request.method == 'GET':
        return render_template('form.html', context_name_1=context["Имя"],
                               context_name_2=context["Фамилия"],
                               num=len(context["Имя"]), form=True)
    elif request.method == 'POST':
        input_name_1 = request.form['input_name_1']
        input_name_2 = request.form['input_name_2']
        with open('main_base.csv', 'a+') as f:
            f.write(f'{input_name_1};{input_name_2};\n')
        return render_template('form.html', context_name_1=context["Имя"],
                           context_name_2=context["Фамилия"],
                           num=len(context["Имя"]), form=False)
@app.route("/")
def index():

    return render_template('index.html')


@app.route("/game/", methods=['POST','GET'])
def game():
    if request.method == 'GET':
        context = {"Имя": [], "Фамилия": [], "Баллы": []}
        with open('main_base.csv', 'r') as csvfile:
            text = csv.reader(csvfile, delimiter=';')
            for row in text:
                context["Имя"].append(row[0])
                context["Фамилия"].append(row[1])
                context["Баллы"].append(0)
            return render_template('game.html', context_name_1=context["Имя"],
                               context_name_2=context["Фамилия"], point=context["Баллы"],
                               num=len(context["Имя"]),victory=False)
    elif request.method == 'POST':
        context = {"Имя": [], "Фамилия": [], "Баллы": []}
        with open('main_base.csv', 'r') as csvfile:
            text = csv.reader(csvfile, delimiter=';')
            for row in text:
                context["Имя"].append(row[0])
                context["Фамилия"].append(row[1])
                context["Баллы"].append(random.randint(0,100))
            victory = context["Баллы"].index(max(context["Баллы"]))
            return render_template('game.html', context_name_1=context["Имя"],
                                   context_name_2=context["Фамилия"], point=context["Баллы"],
            num = len(context["Имя"]),victory=victory)

def create_players():
    names_1 = ['Иван', 'Антон', 'Махмут', 'Джон', 'Алексей', 'Николай', 'Олег', 'Павел']
    names_2 = ['Иванов', 'Петров', 'Сидоров', 'Большов', 'Меньшов', 'Краснов', 'Кузнецов', 'Молодцов']
    n = random.randint(1,10)
    with open('main_base.csv', 'w') as f:
        for i in  range(n):
            n_1 = random.randint(0, len(names_1)-1)
            n_2 = random.randint(0, len(names_2)-1)
            f.write(f'{names_1[n_1]};{names_2[n_2]};\n')



if __name__ == "__main__":
    create_players()
    app.run(debug=True, port=5001)







