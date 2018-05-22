from garage import Garage
from tasks import add

if __name__ == "__main__":
    from sys import argv

    try:
        garage = None
        channel = int(argv[1])

        garage = Garage(channel)
        garage.setup()

        while true:
            message = poll.delay()

            if message == "open":
                garage.open()
    except IndexError:
        print("Need to specify a channel")
        if garage is not None:
            garage.cleanup()
