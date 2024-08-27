from flask import Flask, render_template
app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/client')
def client():
    return render_template('client.html')

@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__=='__main__':
    app.run(debug=True)
