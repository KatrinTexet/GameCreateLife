from flask import Flask, render_template, request, redirect
from game_of_life import GameOfLife


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/life", methods=["POST"])
def create_life():
    width = int(request.form["width"])
    height = int(request.form["height"])
    if 1 < width < 100 and 1 < height < 100:
        GameOfLife(width, height)
    return redirect("/live")


@app.route("/live", methods=["GET"])
def live():
    current_game = GameOfLife()
    current_game.form_new_generation()
    current_game.counter += 1
    return render_template("live.html", current_game=current_game)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
