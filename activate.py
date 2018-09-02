from flask import Blueprint
from garage import Garage
from yaml import load

with open("config.yml", "r") as file:
    config = load(file)
    env = config['development']
    garage = Garage(
        input_pin=env['input_pin'],
        output_pin=env['output_pin']
    )

bp = Blueprint('activate', __name__)

@bp.route('/activate', methods=['GET'])
def activate():
    if garage.activate():
        return('Activated', 200)
    else:
        return('Failed', 503)
