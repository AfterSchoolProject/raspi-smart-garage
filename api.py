from garage import Garage
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome!"

@app.route("/open")
def open():
    garage.open()

    return "Open"

@app.route("/close")
def close():
    garage.close()

    return "Close"

if __name__ == "__main__":
    from sys import argv

    try:
        garage = None
        channel = int(argv[1])

        garage = Garage(channel)
        garage.setup()

        app.run()
    except IndexError:
        print("Need to specify a channel")
    finally:
        if garage is not None:
            garage.cleanup()
