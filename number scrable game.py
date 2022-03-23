numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1_score = []
player2_score = []

# check winning of player 1


def check_winner1():
    if len(player1_score) >= 3:
        if (player1_score[0] + player1_score[1] + player1_score[2] == 15) or (
                player1_score[0] + player1_score[2] + player1_score[3] == 15) or (
                player1_score[0] + player1_score[1] + player1_score[3] == 15) or (
                player1_score[3] + player1_score[1] + player1_score[2] == 15):
            print("congratulation!player one , you win")
            exit()
# check winning of player 2


def check_winner2():
    if len(player2_score) >= 3:
        if (player2_score[0] + player2_score[1] + player2_score[2] == 15) or (
                player2_score[0] + player2_score[2] + player2_score[3] == 15) or (
                player2_score[0] + player2_score[1] + player2_score[3] == 15) or (
                player2_score[3] + player2_score[1] + player2_score[2] == 15):
            print("congratulation!player two , you win")
            exit()


# loop make each player has the ability to pick 4 numbers.
while len(numbers) != 1:
    for player in [1, 2]:
        # player 1 turn.
        if player == 1:
            print("The valid list = ", numbers)
            inp_num = int(input("PLAY1: "))
            # check if the input is valid or not.
            while inp_num not in numbers:
                inp_num = int(input("The number is not in the list, enter a new number: "))
            # remove number from the list to prevent the player from picking it again
            numbers.remove(inp_num)
            # i use insert to append the inputs of the player from the left side.
            player1_score.insert(0, inp_num)
        check_winner1()
        # player 2 turn.
        if player == 2:
            print("The valid list = ", numbers)
            inp_num = int(input("PLAY2: "))
            # check if the input is valid or not.
            while inp_num not in numbers:
                inp_num = int(input("The number is not in the list, enter a new number: "))
            # remove number from the list to prevent the player from picking it again
            numbers.remove(inp_num)
            player2_score.insert(0, inp_num)
        check_winner2()
# if game end without winner.
print("Game drawn")
