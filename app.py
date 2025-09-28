from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cycle')
def cycle():
    return render_template('cycle.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)

