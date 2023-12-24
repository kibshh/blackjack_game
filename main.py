import random


def deal(hand):
    card_on_top = random.choice(cards)
    hand.append(card_on_top)


def display_hands():
    print(f"\nYour hand: {player_hand}  SCORE: {player_score}")
    print(f"Computer's first card: {computer_hand[0]}")


def calculate(hand):
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def check_for_end_of_game():
    if player_score >= 21 or computer_score >= 21:
        return True
    else:
        return False


def ask_player_for_another_card():
    answer = ''
    while answer not in ['y', 'n']:
        answer = input("\n'y' for another card\n'n' to pass\nTYPE HERE: ").lower()
    if answer == 'y':
        return True
    else:
        return False


def display_both():
    print(f"\nYour final hand: {player_hand}  SCORE: {player_score}")
    print(f"Computer's final hand: {computer_hand}   SCORE: {computer_score}")


def display_final():
    display_both()
    if (player_score == 21 and computer_score == 21) or (player_score > 21 and computer_score > 21):
        print("It's a draw! 2 * BLACKJACK")
    elif player_score == 21:
        print("YOU WIN! $$$  BLACKJACK  $$$")
    elif computer_score == 21:
        print("You lost by computer's Blackjack...")
    elif player_score > 21:
        print("You went over, you lost...")
    elif computer_score > 21:
        print("YOU WIN! Computer went over.")
    else:
        if player_score > computer_score:
            print("You both declined to draw. YOU WIN! Your score is higher.")
        elif computer_score > player_score:
            print("You both declined to draw. You lost.. computer's score is higher.")
        else:
            print("You both declined to draw. Your scores are the same, it's a draw.")


def reset():
    global is_game_over, another_card, player_score, computer_score
    player_hand.clear()
    computer_hand.clear()
    is_game_over = False
    another_card = True
    player_score = 0
    computer_score = 0


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []
is_game_over = False
another_card = True
player_score = 0
computer_score = 0
another_game = 'y'

while another_game == 'y':
    reset()
    print("\nWelcome to the game of BLACKJACK")
    #initial deal
    deal(hand=player_hand)
    deal(hand=computer_hand)

    while not is_game_over:
        if another_card:
            deal(hand=player_hand)
        player_score = calculate(player_hand)
        if computer_score < 16:
            deal(hand=computer_hand)
        computer_score = calculate(computer_hand)
        is_game_over = check_for_end_of_game()
        if not another_card and computer_score >= 16:
            is_game_over = True
        if is_game_over:
            display_final()
            another_game = ''
            while another_game not in ['y', 'n']:
                another_game = input("\nDo you want to play another game?\n'y' for yes\n'n' for no\nTYPE HERE: ").lower()
        else:
            display_hands()
            another_card = ask_player_for_another_card()


print("Thank you for playing our game!")