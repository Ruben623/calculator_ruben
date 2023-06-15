from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('glavnaya.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    return render_template('index.html')

@app.route('/information1', methods=['POST'])
def information1():
    return render_template('Finance.html')

@app.route('/information2', methods=['POST'])
def information2():
    return render_template('Marketing.html')

@app.route('/information3', methods=['POST'])
def information3():
    return render_template('Personal.html')

@app.route('/information4', methods=['POST'])
def information4():
    return render_template('webinars.html')

@app.route('/information5', methods=['POST'])
def information5():
    return render_template('Forum.html')

@app.route('/information6', methods=['POST'])
def information6():
    return render_template('start-up.html')

@app.route('/regime', methods=['POST'])
def regime():
    return render_template('tax_regimes.html')

@app.route('/tax_calculate', methods=['POST'])
def calculate1():
    income = float(request.form['income'])
    employees = int(request.form['employees'])
    labor_expenses = float(request.form['labor_expenses'])
    other_expenses = float(request.form['other_expenses'])

    osno_tax = calculate_osno_tax(income, labor_expenses, other_expenses)
    usn_income_tax = calculate_usn_income_tax(income)
    usn_expenses_tax = calculate_usn_expenses_tax(income, labor_expenses, other_expenses)
    patent_tax = calculate_patent_tax(income)

    min_tax = min(osno_tax, usn_income_tax, usn_expenses_tax, patent_tax)

    recommendation = get_tax_recommendation(osno_tax, usn_income_tax, usn_expenses_tax, patent_tax)

    return render_template('result.html', recommendation=recommendation, min_tax=osno_tax)

def calculate_osno_tax(income, labor_expenses, other_expenses):
    tax_rate = 0.2  # Процентная ставка налога для ОСНО
    total_expenses = labor_expenses + other_expenses
    taxable_income = income - total_expenses
    tax = taxable_income * tax_rate
    return tax

def calculate_usn_income_tax(income):
    tax_rate = 0.1  # Процентная ставка налога для УСН "доходы"
    tax = income * tax_rate
    return tax

def calculate_usn_expenses_tax(income, labor_expenses, other_expenses):
    tax_rate = 0.15  # Процентная ставка налога для УСН "доходы-расходы"
    total_expenses = labor_expenses + other_expenses
    taxable_income = income - total_expenses
    tax = taxable_income * tax_rate
    return tax

def calculate_patent_tax(income):
    tax_rate = 0.05  # Процентная ставка налога для патента
    tax = income * tax_rate
    return tax

def get_tax_recommendation(osno_tax, usn_income_tax, usn_expenses_tax, patent_tax):
    min_tax = min(osno_tax, usn_income_tax, usn_expenses_tax, patent_tax)

    if min_tax == osno_tax:
        recommendation = "ОСНО"
    elif min_tax == usn_income_tax:
        recommendation = "УСН 'доходы'"
    elif min_tax == usn_expenses_tax:
        recommendation = "УСН 'доходы-расходы'"
    else:
        recommendation = "Патент"

    return recommendation


if __name__ == '__main__':
    app.run()
