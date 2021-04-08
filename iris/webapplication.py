# Answer to a question on Flask mailing list
# http://librelist.com/browser//flask/2012/6/30/using-ajax-with-flask/
# NOTE: *REALLY* don't do the thing with putting the HTML in a global
#       variable like I have, I just wanted to keep everything in one
#       file for the sake of completeness of answer.
#       It's generally a very bad way to do things :)
#
from flask import (Flask, request, jsonify, render_template)
import pandas as pd        

import math
import ast
import numpy as np
import tensorflow


model=tensorflow.keras.models.load_model('model.tf')
model.compile()
app = Flask(__name__)



@app.route('/', methods=['post', 'get'])
def index():    
    
    mes = ''
    if request.method == 'POST':
        sepal = request.form.get('sepal')  # access the data inside 
        petal = request.form.get('petal')
        lis=ast.literal_eval(sepal)+ast.literal_eval(petal)
        mes = np.array(lis,ndmin=2)
        mes=model.predict(mes)
        
        
    return render_template('index.html', message=str(mes))
    
        

        
@app.route('/iris', methods = ['POST'])
def iris():
    return

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return render_template('view.html', message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)