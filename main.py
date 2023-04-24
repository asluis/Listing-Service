from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/api/v1/')
def main():
    return {'response': '''This is University Pal's Listing microservice for everything related to a listing.'''}


if __name__ == '__main__':
    app.run(host='localhost', port=5050)
