from flask import Flask, render_template, request
from curses.ascii import isupper,isdigit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sign_up')
def sign_up():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    first_name = request.args.get('name')
    last_name = request.args.get('surname')
    return render_template('thankyou.html', first_name=first_name, last_name=last_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/username_check')
def username_check():
    return render_template('username_check.html')

@app.route('/username_check_report')
def username_check_report():
    first_name = request.args.get('uname')
    lower_found = 0
    upper_found = 0
    number_found_at_last = 0
    for upper_char in first_name:
        if upper_char.isupper():
            upper_found += 1
            break
    for lower_char in first_name:
        if lower_char.islower():
            lower_found = lower_found+1
            break
    if first_name[-1].isdigit():
        number_found_at_last = number_found_at_last+1
    
    return render_template('username_check_report.html',lower_found=lower_found, upper_found=upper_found, number_found_at_last=number_found_at_last)
        

if __name__ == '__main__':
    app.run(debug=True, port=5005)