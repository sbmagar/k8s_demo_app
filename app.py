from flask import Flask
import random

 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sqrt')
def square_root():
    num = random.randint(1, 1000)
    return (f"The square root of {num} is {num ** 0.5}.")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    
