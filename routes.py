from flask import Flask, render_template, request
from flask_mail import Mail, Message
from form import ContactForm


app = Flask(__name__)
app.secret_key = 'YourSuperSecreteKey'

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'secretary@codcompsci.club'
app.config['MAIL_PASSWORD'] = 'cde34rfvbg'

mail = Mail(app)

@app.route('/index', methods=('GET', 'POST'))
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            return 'Please fill in all fields <p><a href="/index">Try Again!!!</a></p>'
        else:
            msg = Message("Message from your visitor" + form.name.data,
                          sender='YourUser@NameHere',
                          recipients=['yourRecieve@mail.com', 'someOther@mail.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data)
            mail.send(msg)
            return "Successfully  sent message!"
    elif request.method == 'GET':
        return render_template('/index.html', form=form)

if __name__ == '__main__':
    app.run()