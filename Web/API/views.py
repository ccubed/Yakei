from flask import *
from Backend import *

api = Blueprint('api', __name__, template_folder="templates", static_folder="static")