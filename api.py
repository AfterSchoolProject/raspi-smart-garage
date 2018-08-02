from garage import Garage
from flask import Flask
from yaml import load

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome!"

@app.route("/activate")
def activate():
    if garage.activate():
        return('Activated', 200)
    else:
        return('Failed', 503)

if __name__ == "__main__":
    from sys import argv

    with open("config.yml", "r") as file:
        try:
            configs = load(file)
            env = configs[argv[1]]

            with Garage(input_pin=env['input_pin'], output_pin=env['output_pin']) as garage:
                app.run(host="0.0.0.0")
        
        except IndexError:
            print("Need to specify an environment")
