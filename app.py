from flask import Flask, render_template, request
from stock_price import get_stock_price

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    data = None
    if request.method == 'POST':
        stock_symbol = request.form.get('symbol')
        data = get_stock_price(stock_symbol)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)