from flask import Flask, render_template, request, render_template_string, redirect
import hashlib

app = Flask(__name__)

redirect_urls = {}
base_url = 'http://localhost:5000/'

def generate_short_url_path(url, char_limit=6):
    return hashlib.shake_256(url.encode('utf-8')).hexdigest(char_limit//2)

@app.route('/', methods=['POST', 'GET'])
def get_url():
    if request.method == 'POST':
        input_url = request.form['url']
        short_url_path = ''
        short_url_path = generate_short_url_path(input_url)
        redirect_urls[short_url_path] = input_url
        return render_template('home.html', new_url=base_url+short_url_path, old_url=input_url)
    else:
        return render_template('home.html')

@app.route('/<path>')
def index(path):
    if path not in redirect_urls:
        return render_template_string('PageNotFound {{ errorCode }}', errorCode='404'), 404
    return redirect(redirect_urls[path])