from flask import render_template

print("Hello world")
from flask import Flask
app = Flask(__name__)

#decorator for default output
@app.route("/")
def hello():
  return "<html><head></head><body>Home</body></html>"

#new function
@app.route("/data_to")
def data_to():
    some_pars={'user':'Me', 'color':'red'}
    some_str='Hello friends'
    some_value = 10
    return render_template('simple.html', some_str=some_str, some_value = some_value, some_pars=some_pars)
    

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

SECRET_KEY = 'secret'
app.config['SECRET_KEY'] = SECRET_KEY
#use keys from google
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfRyKQZAAAAAAH-jfQ1J5xvJJT0INIuIB4qJwZI'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfRyKQZAAAAANuc77UiF9zdxEAPY0cbUGGIQgft'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}
#work with standarts
from flask import Flask
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

#form for file downloading
class NetForm(FlaskForm):
    #checking field for string entering 
    openid= StringField('openid', validators=[DataRequired()])
    #checking field for file entering 
    openid= StringField('Load image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
        
recaptcha = RecaptchaField()
submit = SubmitField('send')

#function of transaction processing from 127.0.0.1:5000/net
from werkzeug.utils import secure_filename
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import net as neuronet
@app.route("/net", methods=['GET','POST'])
def net():
    #create form object
    form = NewForm()
    filename = None
    neurodic = {}
    #if 'submit' was pressed
    if form.validate_on_submit():
        #read image from static cataloge
        filename = os.path.join('./static', secure_filename(form.upload.data.filename))
        fcount, fimage = neuronet.read_image_files(10, './static')
        decode = neuronet.getresult(fimage)
        for elem in decode:
            neurodic[elem[0][1]] = elem[0][2]
        #file saving
        form.upload.data.save(filename)
    return render_template('net.html', form=form, image_name=filename, neurodic=neurodic)

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000)
  
from flask import request
from flask import Response
import base64
from PIL import Image
from io import BytesIO
import json

@app.route("/apinet", methods=['GET', 'POST'])
def apinet():
    if request.mimetype == 'application/json':
        data = request.get_json()
        filebytes = data['imagebin'].encode('utf-8')
        cfile = base64.b64decode(filebytes)
        img = Image.open(BytesIO(cfile))
        decode = neuronet.getresult([img])
        neurodic = {}
        for elem in decode:
            neurodic[elem[0][1]] = str(elem[0][2])
            print(elem)
    ret = json.dumps(neurodic)
    resp = Response(response=ret, status=200, mimetype = "application/json")
    return resp
