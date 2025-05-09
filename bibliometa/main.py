from flask import Flask
import uuid

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())
app.debug = True

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
