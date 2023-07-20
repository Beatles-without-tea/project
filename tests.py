from german_whist import Play, is_card_legal, Card

def test_0_player_game():
    players = 0
    new_game = Play(players=players)
    new_game.deal()
    new_game.player2_hand
    for _ in range(13):
        new_game.play_first_half_round(_)
        assert len(new_game.player1_hand) == 13
        assert len(new_game.player2_hand) == 13
    for j in range(13):
        assert len(new_game.player1_hand) == 13 - j
        assert len(new_game.player2_hand) == 13 - j
        new_game.play_second_half_round(_)
    new_game.is_game_over()
    assert new_game.game_over == True
    assert new_game.player1_score + new_game.player2_score == 13

#check that players hands are correct
# check if rule checker for cards works    


def test_payouts_case_1():
    new_game = Play(players=0)
    new_game.trump_card = Card('Spades','2')
    new_game.card1 = Card('Diamonds','K')
    new_game.card2 = Card('Spades','1')
    new_game.pay_player_1()
    assert new_game.player1_wins == False

def test_payouts_case_2():
    new_game = Play(players=0)
    new_game.trump_card = Card('Spades','2')
    new_game.card1 = Card('Diamonds','K')
    new_game.card2 = Card('Diamonds','K')
    new_game.pay_player_2()
    assert new_game.player1_wins == False

def test_payouts_case_3():
    new_game = Play(players=0)
    new_game.trump_card = Card('Spades','2')
    new_game.card1 = Card('Spades','1')
    new_game.card2 = Card('Diamonds','K')
    new_game.pay_player_2()
    assert new_game.player1_wins == True

# Test the constructor of the Play class
def test_Play_initialization():
    new_game = Play(players=2)
    assert new_game.players == 2
    assert len(new_game.player1_hand) == 0
    assert len(new_game.player2_hand) == 0

# Test dealing of the cards
def test_dealing():
    new_game = Play(players=2)
    new_game.deal()
    assert len(new_game.player1_hand) == 13
    assert len(new_game.player2_hand) == 13


# Test if is_card_legal function is working as expected
def test_is_card_legal():
    card1 = Card('Spades', 'K')
    card2 = Card('Hearts', 'A')
    # Assuming the first card played is Spades, Hearts should not be legal if there is any Spade card in the hand
    hand = [card1, card2]
    assert is_card_legal(card2, card1, hand) == None
# check cards (equality and rankings)
