has_ticket = True
knife_length = 20

if has_ticket:
    print("Ticket checking passed!")
    if knife_length < 20:
        print("Plase onboard the train!")
    else:
        print("Please do NOT carry a long knife!!")
else:
    print("You don't have ticket, please buy one first!")