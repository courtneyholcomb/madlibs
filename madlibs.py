"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment1 = AWESOMENESS.pop(choice(range(len(AWESOMENESS))))
    compliment2 = AWESOMENESS.pop(choice(range(len(AWESOMENESS))))
    compliment3 = AWESOMENESS.pop(choice(range(len(AWESOMENESS))))

    return render_template("compliment.html",
                           person=player,
                           compliment1=compliment1,
                           compliment2=compliment2,
                           compliment3=compliment3)


@app.route('/game')
def show_madlib_form():
    """Display madlib form."""
    # stylesheet = request.args.get("/static/madlibs.css")

    response = request.args.get("game-response")

    person = request.args.get("person")

    if response == "no":
        return render_template("goodbye.html",person=person)

    elif response == "yes": 
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Display filled-in madlib."""
    rando_madlib = choice(["madlib.html", "madlib1.html", "madlib2.html"])


    adjective = request.args.get("adjective")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    adjective4 = request.args.get("adjective4")
    noun = request.args.get("noun")
    noun2 = request.args.get("noun2")
    noun3 = request.args.get("noun3")
    pverb = request.args.get("pverb")
    pverb2 = request.args.get("pverb2")
    adverb = request.args.get("adverb")
    adverb2 = request.args.get("adverb2")
    verb = request.args.get("verb")

    return render_template(rando_madlib, noun=noun, noun2=noun2, noun3=noun3,
        adjective=adjective, adjective2=adjective2, adjective3=adjective3,
        adjective4=adjective4, pverb=pverb, pverb2=pverb2, adverb=adverb, 
        adverb2=adverb2, verb=verb)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)