
from flask import Flask

app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'
app.secret_key = "spininmanurematch"

import views