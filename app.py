from flask import Flask
from routes import *

app = Flask(__name__)
app.config['MYSQL_DATABASE_URI'] = 'mysql://root:password@localhost/ciqDB'

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
