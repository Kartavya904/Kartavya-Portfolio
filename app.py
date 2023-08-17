import json
import os, sys, time, datetime, random, string, re, requests
from flask import Flask, Blueprint, render_template, request, session, redirect, url_for, jsonify, flash, current_app, g
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

app = Flask(__name__)
Breadcrumbs(app=app)
secret_key = os.getenv("SENDGRID_API_KEY")
# print("secret_key: ", secret_key)

# Define routes for each page
@app.route('/')
@app.route('/Home')
@register_breadcrumb(app, './Home', 'Home')
def index():
    return render_template('Home.html')

@app.route('/About_Me')
@register_breadcrumb(app, './About_Me', 'About Me')
def about_me():
    return render_template('About_Me.html')

@app.route('/Projects')
@register_breadcrumb(app, './Projects', 'Projects')
def projects():
    return render_template('Projects.html')

@app.route('/Experiences')
@register_breadcrumb(app, './Experiences', 'Experiences')
def experiences():
    return render_template('Experiences.html')

@app.route('/Honors_Experience')
@app.route('/Honors-Experience')
@register_breadcrumb(app, './Honors-Experience', 'Honors-Experience')
def honors_experience():
    return render_template('Honors-Experience.html')

@app.route('/Gateway')
@register_breadcrumb(app, './Gatway', 'Gateway')
def gateway():
    return render_template('Gateway.html')

@app.route('/Year-In-Review')
@register_breadcrumb(app, './Year-In-Review', 'Year-In-Review')
def year_in_review():
    return render_template('Year-In-Review.html')

@app.route('/Year-In-Review-2022-2023')
@register_breadcrumb(app, './Year-In-Review-2022-2023', 'Year-In-Review-2022-2023')
def year_in_review_2022_2023():
    return render_template('Year-In-Review-2022-2023.html')

@app.route('/Involvements')
@register_breadcrumb(app, './Involvements', 'Involvements')
def involvements():
    return render_template('Involvements.html')

@app.route('/COOP-1000')
@register_breadcrumb(app, './COOP-1000', 'COOP-1000')
def coop_1000():
    return render_template('COOP-1000.html')

@app.route('/Discord_Exp')
@register_breadcrumb(app, './Discord-Exp', 'Discord-Exp')
def discord():
    return render_template('Discord_Exp.html')

@app.route('/Pathways')
@register_breadcrumb(app, './Pathways', 'Pathways')
def pathways():
    return render_template('Pathways.html')

@app.route('/Contact', methods=['GET', 'POST'])
@register_breadcrumb(app, './Contact', 'Contact')
def contact():
    if request.method == 'POST':
        # Process the form data here
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        if (not phone):
            phone = "N/A"
        location = request.form.get('location')
        if (not location):
            location = "N/A"
        Subject = request.form.get('subject')
        message = request.form.get('message')
        
        messageToSend = "Hi Kartavya, This is " + name + ". My email is " + email + ". My phone number is " + phone + ". I am from " + location + ". " + "\nI wanted to say:\n" + message + "."

        # Send email to myself
        message = Mail(
            from_email='singhk6@mail.uc.edu',
            to_emails='singhk6@mail.uc.edu',
            subject=Subject,
            html_content=f'<strong>{messageToSend}</strong>')
        print(message)
        try:
            sg = SendGridAPIClient(secret_key)
            response = sg.send(message)
            print("Email sent successfully")
            return "<script LANGUAGE='JavaScript'> window.alert('Message Successfully Sent!'); window.location.href = 'Contact'</script>)"
        except Exception as e:
            print("Error sending email")
            print(e)
            return "<script LANGUAGE='JavaScript'> window.alert('Message Failed To Send!'); window.location.href = 'Contact'</script>)"


    return render_template('Contact.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
