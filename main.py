from flask import Flask, request, url_for
import requests
import pandas as pd
from faker import Faker
fake = Faker()

app = Flask(__name__)


@app.route("/requirements/")
def requirements():
    with open('requirements.txt', 'r') as f:
        t = f.readlines()
        t = "<br>".join(t)
    return t


def randomize(count):
    st = ''
    for i in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name}.{last_name}@{fake.domain_name()}"
        comb = f"{first_name} {last_name} -- {email}<br>"
        st = st + str(comb)
    return st


@app.route('/generate-users/')
def generate_users():
    count = request.args.get('count')
    return randomize(int(count))


@app.route("/mean/")
def mean():
    data = pd.read_csv("hw.csv")
    a = sum(data[' "Height(Inches)"']) / max(data['Index']) * 2.54
    b = sum(data[' "Weight(Pounds)"']) / max(data['Index']) * 0.453592
    return f'''
    <p>Average height = {a} cm<br>
    Average weight = {b} kg</p>
    '''


@app.route("/space/")
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts = r.json()["number"]
    return f'<p> Current number of astronauts in space are {astronauts}'


@app.route('/')
def main():
    return f'''
    <a href = \'{url_for('requirements')}\'>Requirements</a><br>
    <a href = \'{url_for('generate_users', count='100')}\'>Generate users</a><br>
    <a href = \'{url_for('mean')}\'>Mean</a><br>
    <a href = \'{url_for('space')}\'>Space</a><br>
    '''


if __name__ == "__main__":
    app.run()
