spielfeld = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = [1, 2, 3]
players = ["X", "O"]


def show_field(spielfeld):
    print(spielfeld[0][0], "|", spielfeld[0][1], "|", spielfeld[0][2])
    print("––|–––|––")
    print(spielfeld[1][0], "|", spielfeld[1][1], "|", spielfeld[1][2])
    print("––|–––|––")
    print(spielfeld[2][0], "|", spielfeld[2][1], "|", spielfeld[2][2])


def check_if_over(spielfeld):
    for p in players:
        for i in rows:
            if spielfeld[i][0] == p and spielfeld[i][1] == p and spielfeld[i][2] == p:
                return True
            elif spielfeld[0][i] == p and spielfeld[1][i] == p and spielfeld[2][i] == p:
                return True
            elif spielfeld[0][0] == p and spielfeld[1][1] == p and spielfeld[2][2] == p:
                return True
            elif spielfeld[2][0] == p and spielfeld[1][1] == p and spielfeld[0][2] == p:
                return True
            else:
                return False


show_field(spielfeld)
