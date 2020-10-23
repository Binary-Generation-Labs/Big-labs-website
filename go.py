from flask import Flask
from flask import render_template
from flask import request

app = Flask(__email__)

@app.route('/',methods=['POST','GET'])
def process_form():
    if request.method == 'POST':
       form_input = request.form['email']
       return render_template('index.html',email=form_input)
    else:
       return render_template('index.html')

if __email__ == '__main__':
   app.run(debug=True)
