from boggle import Boggle
from flask import Flask, render_template, session

app = Flask(__name__)
boggle_game = Boggle()

app.config['SECRET_KEY'] = "secret key"

@app.route("/")
def display_board():
    session["board"] = Boggle.make_board(Boggle)
    return render_template("board.html", board = Boggle.make_board(Boggle))

    