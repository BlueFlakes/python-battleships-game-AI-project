import os

from flask import Flask, render_template, redirect, request

from models.computer import Computer
from models.game import Game
from models.player import Player

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


@app.route('/single', methods=["POST"])
def single():
    player_name = request.form["player_name"]
    computer_level = request.form["computer_level"]
    player = Player(player_name)
    computer = Computer(computer_level)

    game = Game(player, computer)
    Game.current_game = game
    Game.current_game.set_first_player()
    return render_template("Ocean.html", game=Game.current_game)

@app.route("/update_single", methods=["POST"])
def update_single():
    if Game.current_game.player_in_round != Game.current_game.player1:
        other_player = Game.current_game.player1
    else:
        other_player = Game.current_game.player2
    counter = 0
    for row in Game.current_game.player_in_round.ocean.enemy_board:
        counter += 1
        counter1 = 0
        for cell in row:
            counter1 += 1
            position = "{}{}".format(counter, counter1)
            if position == request.form["j"] and not cell.is_hit:
                cell.hit()
    Game.current_game.player_switch()
    return render_template("Ocean.html", game=Game.current_game)


@app.route('/multi', methods=["POST"])
def multi():
    player1_name = request.form["player1_name"]
    player2_name = request.form["player2_name"]
    player1 = Player(player1_name)
    player2 = Player(player2_name)

    game = Game(player1, player2)
    Game.current_game = game
    Game.current_game.set_first_player()
    return render_template("Ocean.html", game=Game.current_game)


@app.route('/update_ocean', methods=["POST"])
def update():
    counter_id = 0
    for row in Game.current_game.player_in_round.ocean.enemy_board:
        for cell in row:
            counter_id += 1
            if cell.id == counter_id:
                if not cell.is_hit:
                    cell.hit()
                else:
                    return render_template("Ocean.html", game=Game.current_game, message="It is hit already!")
    Game.current_game.player_switch()
    return render_template("Ocean.html", game=Game.current_game)


@app.route('/simulation', methods=["POST"])
def simulation():
    computer1_level = request.form["computer1_level"]
    computer2_level = request.form["computer2_level"]
    computer1 = Computer(computer1_level)
    computer2 = Computer(computer2_level)
    computer2.name = "Computer 2"
    computer1.set_ships()
    computer2.set_ships()
    Game.current_game = Game(computer1, computer2)
    Game.current_game.set_first_player()
    if Game.current_game.is_over:
        return render_template("Ocean.html", game=Game.current_game, winner=Game.current_game.player_in_round.name)
    return render_template("Ocean.html", game=Game.current_game)


@app.route('/refresh_simulation', methods=["POST"])
def refresh_simulation():
    if Game.current_game.player_in_round == Game.current_game.player1:
        enemy_ocean = Game.current_game.player2.ocean
    else:
        enemy_ocean = Game.current_game.player1.ocean
    Game.current_game.player_in_round.shot(enemy_ocean)
    Game.current_game.player_switch()
    return render_template("Ocean.html", game=Game.current_game)


@app.errorhandler(404)
def not_found(e):
    if request.path.endswith("/") and request.path[:-1] in all_endpoints:
        return redirect(request.path[:-1]), 302
    return render_template("404.html"), 404


# running the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
