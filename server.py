from flask import Flask
import random

random_num = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media0.giphy.com/media/rdiZkcRqXWiTFzTYFS/giphy.webp'>")


@app.route("/<int:guess>")
def check(guess):
    if guess == random_num:
        return ("<h1 style='color: yellow'>You ARE RIGHT</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif guess > random_num:
        return ("<h1 style='color: red'>UR GUESS IS TOO HIGH</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif guess < random_num:
        return ("<h1 style='color: blue'>UR GUESS IS TOO LOW</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")


if __name__ == '__main__':
    app.run(debug=True)