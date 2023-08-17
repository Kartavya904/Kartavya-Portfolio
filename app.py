import json
import os, sys, time, datetime, random, string, re, requests
from flask import Flask, Blueprint, render_template, request, session, redirect, url_for, jsonify, flash, current_app, g
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb

app = Flask(__name__)
Breadcrumbs(app=app)

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

@app.route('/Year-In-Review')
@register_breadcrumb(app, './Year-In-Review', 'Year In Review')
def year_in_review():
    return render_template('Year-In-Review.html')

@app.route('/Pathways')
@register_breadcrumb(app, './Pathways', 'Pathways')
def more():
    return render_template('Pathways.html')

@app.route('/Contact')
@register_breadcrumb(app, './Contact', 'Contact')
def contact():
    return render_template('Contact.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
