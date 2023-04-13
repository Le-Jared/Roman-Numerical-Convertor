from flask import Flask, render_template, request
import re

app = Flask(__name__)

def roman_to_arabic(roman):
    if not roman or not re.fullmatch(r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman):
        raise ValueError('Invalid Roman numeral')

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    arabic = 0
    prev_value = 0
    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        prev_value = value

    return arabic

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        roman_numeral = request.form['roman_numeral']
        try:
            result = roman_to_arabic(roman_numeral)
        except KeyError:
            result = "Invalid Roman numeral"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
