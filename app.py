from boggle import Boggle
from flask import Flask, render_template

app = Flask(__name__)
boggle_game = Boggle()

@app.route("/")
def display_board():
    return render_template("board.html", board = Boggle.make_board(Boggle))