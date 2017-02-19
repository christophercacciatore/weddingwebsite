from flask import *
from flask import render_template, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')




@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)