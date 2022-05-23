# the blackjack game with computer

from random import randrange

score = 0

while score < 21:
    print('Your score is', score)
    answer = input('Do you want next card? ')
    if answer == 'yes':
        card = randrange(2, 12)
        print('Your card is', card)
        score = score + card
    elif answer == 'no':
        break
    else:
        print('I do not understand, answer yes or no')

dealer_score = 0

while dealer_score < score and score <= 21:
    dealer_card = randrange(2, 12)
    print('Dealer card is', dealer_card) 
    dealer_score = dealer_score + dealer_card
    print('Dealer score is', dealer_score)
    if dealer_score >= score:
        break

print('...\n...\n...')

if score > dealer_score and score <= 21 or dealer_score > 21:
    print('Your score is', score) 
    print('Dealer score is', dealer_score)
    print('You win')
elif score <= dealer_score:
    print('Your score is', score)
    print('Dealer score is', dealer_score)
    print('You lose')
else:
    print('Your score is', score, 'witch is too much')
    print('You lose')