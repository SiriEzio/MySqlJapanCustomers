from flask import Flask
app = Flask(__name__)

@app.route('/gay')
def index():
   return '<html><body><h1>Hello gay</h1></body></html>'

if __name__ == '__main__':
   app.run(debug = True)