FROM arm32v7/python:3.6.6-stretch

WORKDIR /webapp

RUN pip3 install rpi.gpio
RUN pip3 install pipenv

COPY Pipfile* /webapp/

RUN pipenv install --system

COPY . /webapp

EXPOSE 5000

ENTRYPOINT ["python3", "api.py", "18"]
