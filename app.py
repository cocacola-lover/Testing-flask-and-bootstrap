from flask import Flask, render_template;

app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/promotion_image')
def promo() :
    return render_template('promo.html')

@app.route('/astronaut_selection')
def selection() :
    return render_template('selection.html')

if __name__ == '__main__':
    app.run(debug=True)
