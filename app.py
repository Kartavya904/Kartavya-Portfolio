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
