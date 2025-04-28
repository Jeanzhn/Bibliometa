from flask import Flask
import uuid

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

from views import *

if __name__ == '__main__':
    app.run()
