from flask import Flask, render_template, url_for, redirect, request
from calculate import Probability

app = Flask(__name__)

cards = ['A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
         'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
         'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
         'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']

suits = ['♥', '♠', '♦', '♣']
diction = {}
diction['card1'] = 'A♥'
diction['card2'] = 'A♠'
diction['tablecard1'] = '?'
diction['tablecard2'] = '?'
diction['tablecard3'] = '?'
diction['tablecard4'] = '?'
diction['tablecard5'] = '?'
diction['color11'] = 'red'
diction['color12'] = 'black'
diction['probability'] = 0

prob = Probability()


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html', cards=cards, suits=suits, diction=diction)


# card in hend
@app.route('/card1/<value>', methods=['GET', 'POST'])
def card1(value):
    diction['card1'] = value
    if value[-1] in ['♥', '♦']:
        diction['color11'] = 'red'
    else:
        diction['color11'] = 'black'
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))


@app.route('/card2/<value>', methods=['GET', 'POST'])
def card2(value):
    diction['card2'] = value
    if value[-1] in ['♥', '♦']:
        diction['color12'] = 'red'
    else:
        diction['color12'] = 'black'
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))


# talbecards
@app.route('/tablecard1/<value>', methods=['GET', 'POST'])
def tablecard1(value):
    diction['tablecard1'] = value
    if value[-1] in ['♥', '♦']:
        diction['color1'] = 'red'
    else:
        diction['color1'] = 'black'
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))


@app.route('/tablecard2/<value>', methods=['GET', 'POST'])
def tablecard2(value):
    diction['tablecard2'] = value
    if value[-1] in ['♥', '♦']:
        diction['color2'] = 'red'
    else:
        diction['color2'] = 'black'
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))


@app.route('/tablecard3/<value>', methods=['GET', 'POST'])
def tablecard3(value):
    diction['tablecard3'] = value
    if value[-1] in ['♥', '♦']:
        diction['color3'] = 'red'
    else:
        diction['color3'] = 'black'
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))


@app.route('/tablecard4/<value>', methods=['GET', 'POST'])
def tablecard4(value):
    diction['tablecard4'] = value
    if value[-1] in ['♥', '♦']:
        diction['color4'] = 'red'
    else:
        diction['color4'] = 'black'
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))


@app.route('/tablecard5/<value>', methods=['GET', 'POST'])
def tablecard5(value):
    diction['tablecard5'] = value
    if value[-1] in ['♥', '♦']:
        diction['color5'] = 'red'
    else:
        diction['color5'] = 'black'
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))


# culculate probability
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    dealler = cards[:]
    diction['players'] = int(request.form.get('players'))
    diction['card1'] = request.form.get('card1')
    diction['card2'] = request.form.get('card2')
    for i in range(1, 6):
        diction['tablecard' + str(i)] = request.form.get('tablecard' + str(i))
    print(diction)
    diction['pairs'] = prob.pairs(diction)['prob_all']
    diction['two_pairs'] = prob.two_pairs(diction)['prob_all']
    diction['sets'] = prob.sets(diction)['prob_all']
    diction['street'] = prob.street(diction)['prob_all']
    diction['flash'] = prob.flash(diction)['prob_all']
    return redirect(url_for('main', cards=cards, suits=suits, diction=diction))
