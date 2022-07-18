import json

from flask import Flask, jsonify
from utils import movie_by_title, movies_by_years

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/movie/<title>')
def get_by_title(title):
    return movie_by_title(title)


@app.route('/movie/<int:year1>/to/<year2>')
def get_movies_by_years(year1: int, year2: int):
    return jsonify(movies_by_years(year1, year2))


if __name__ == "__main__":
    app.run(debug=True)
