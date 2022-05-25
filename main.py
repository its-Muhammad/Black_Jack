import random
import tkinter


def load_cards(card_list):
    suits = ["club", "diamond", "heart", "spade"]
    face_cards = ["jack", "king", "queen"]

    for suit in suits:
        # Loading images of numbered cards and putting them into the list
        for card in range(1, 11):
            name = f"cards\\{card}_{suit}.png"
            image = tkinter.PhotoImage(file=name)
            card_list.append((card, image))
        # Loading images of face cards and putting them into the list
        for card in face_cards:
            name = f"cards\\{card}_{suit}.png"
            image = tkinter.PhotoImage(file=name)
            card_list.append((10, image))


def score_hand(hand):
    score = 0
    ace = False
    for card in hand:
        card_value = card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 11
            ace = False
    return score


def deal_card(frame):
    # Taking the card out of the deck and displaying in the frame
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1]).pack(side="left")

    # Append the card back in the deck
    deck.append(next_card)
    return next_card


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_var.set(player_score)

    if player_score > 21:
        result_text.set("Dealer Wins!")


def deal_dealer():
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_var.set(dealer_score)

    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_var.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Its a Draw!")


def shuffle():
    random.shuffle(deck)


def new_game():
    global dealer_hand
    global player_hand
    global dealer_card_frame
    global player_card_frame

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="ew")

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, rowspan=2)

    result_text.set("")

    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_var.set(score_hand(dealer_hand))
    deal_player()


# Creating Main window
window = tkinter.Tk()
window.title("Black Jack By ME")
window.geometry("640x300-400-200")
window.configure(background="green")
window["padx"] = 8

# Result variable showing "win or draw"
result_text = tkinter.StringVar()
tkinter.Label(window, textvariable=result_text, background="green",
              fg="White", font=("Ariel", 12, "bold")).grid(row=0, column=0, columnspan=3)

# Card frames to put dealer and player cards and scores
card_frame = tkinter.Frame(window, relief="sunken", background="green", borderwidth=1)
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

# Dealer text label - card frame
dealer_label = tkinter.Label(card_frame, text="Dealer", background="green", fg="white")
dealer_label.grid(row=0, column=0)

# Dealer score -  to be put inside card frame
dealer_score_var = tkinter.IntVar()
dealer_score_label = tkinter.Label(card_frame, textvariable=dealer_score_var, background="green", fg="white")
dealer_score_label.grid(row=1, column=0)

# Dealer card frame - card frame
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="ew")

# Player text label - card frame
player_label = tkinter.Label(card_frame, text="Player", background="green", fg="white")
player_label.grid(row=2, column=0)

# Player score -  to be put inside card frame
player_score_var = tkinter.IntVar()
player_score_label = tkinter.Label(card_frame, textvariable=player_score_var, background="green", fg="white")
player_score_label.grid(row=3, column=0)

# Player card frame - card frame
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Button frame - Separate frame to put buttons
button_frame = tkinter.Frame(window)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

# Button to Hit
deal_dealer_button = tkinter.Button(button_frame, text="Deal", command=deal_dealer)
deal_dealer_button.grid(row=0, column=0)

# Button to stand
deal_player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
deal_player_button.grid(row=0, column=1)

# Button to shuffle
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=2)

# Button for new game
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=3)

cards = []
load_cards(cards)

deck = list(cards) + list(cards) + list(cards)
shuffle()

player_hand = []
dealer_hand = []

new_game()

window.mainloop()
