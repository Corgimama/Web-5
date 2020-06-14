from flask import render_template

print("Hello world")
from flask import Flask
app = Flask(__name__)

#decorator for default output
@app.route("/")
def hello():
  return "<html><head></head><body>Hello World!</body></html>"

#new function
@app.route("/data_to")
def data_to():
    some_pars={'user':'Me', 'color':'red'}
    some_str='Hello friends'
    some_value = 10
    return render_template('simple.html', some_str=some_str, some_value = some_value, some_pars=some_pars)
    
if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000)
