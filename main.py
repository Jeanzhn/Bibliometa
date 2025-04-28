<<<<<<< HEAD
from flask import Flask
import uuid

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

from views import *
=======
import json
from flask import Flask

app = Flask(__name__)

from views.views import *
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c

if __name__ == '__main__':
    app.run()
