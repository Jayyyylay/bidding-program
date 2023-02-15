from art import logo
print(logo)

list_mon_bidders = []


def main():
    add_bidders = {}



    again = True
    while again:
        name = input("Type your name: ")
        bid = int(input("Type your bid: $"))

        add_bidders[name] = bid
        play_again = input("Do any one still wants to bid: yes or no: ").lower()
        if play_again == "no":
            for highest in add_bidders:
                mon = add_bidders[highest]
                list_mon_bidders.append(mon)
            highest_bid = list_mon_bidders[0]
            for number in list_mon_bidders:
                if number > highest_bid:
                    highest_bid = number
            print(f"The highest is {highest} with a bid of {highest_bid}")
            again = False


main()
game_again = True
while game_again:

    play_again = input("Do you wanna try again? yes or no: ").lower()
    if play_again == "yes":
        main()
    elif play_again == "no":
        print("Thank you for bidding!")
        game_again = False
    elif play_again != "yes" and play_again != "no":
        print("Please type yes or no only!")
