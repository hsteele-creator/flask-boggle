from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify

app = Flask(__name__)
boggle_game = Boggle()

app.config['SECRET_KEY'] = "secret key"

@app.route("/")
def display_board():
    """displays the boggle board and saves it in session"""
    session["board"] = Boggle.make_board(Boggle)
    session["score"] = 0
    return render_template("board.html", board = Boggle.make_board(Boggle), score=session["score"])

@app.route("/check-guess")
def check_guess():
    """checks if the user guess is valid"""
    guess = request.args["guess"] 
    board = session["board"]
    result = Boggle().check_valid_word(board, guess)
    return jsonify({"result": result})
    # return str(Boggle().find(session["board"], guess))

