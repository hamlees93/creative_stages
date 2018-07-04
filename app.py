from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from flask_bootstrap import Bootstrap 
from forms import ContactForm
from flask_mail import Message, Mail 

mail = Mail()
app = Flask(__name__)

#Add when website is ready to launch
#app.config['RECAPTCHA_PUBLIC_KEY'] = ''
#app.config['RECAPTCHA_PRIVATE_KEY'] = ''

#Find out the details of info@creatingstages.com.au
app.config['SECRET_KEY'] = '********************'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'bluemountainsblend@gmail.com'
app.config['MAIL_PASSWORD'] = '********'
mail.init_app(app)

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  form = ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields required.')
      return render_template('index.html', form=form)
    else:
      msg = Message(form.name.data, sender='bluemountainsblend@gmail.com', recipients=['info@creatingstages.com.au'])
      msg.body = """
      From : %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('success.html', form=form)
  elif request.method == 'GET':
    return render_template('index.html', form=form)

@app.route('/book')
def book():
  return render_template('book.html')

@app.route('/success')
def success():
  return render_template('success.html')
