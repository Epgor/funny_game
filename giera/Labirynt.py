from random import randint

def Generate(labirynt):

    labirynt = [['◫'] * (20) for i in range(20)]

    for i in range(20):
        labirynt[i][19] = '◼'
        labirynt[i][0] = '◼'
        labirynt[19][i] = '◼'
        labirynt[0][i] = '◼'

    for x in range(1, 19):
        for y in range(1, 19):
            roll = randint(0, 3)
            if (roll == 0):
                if ((labirynt[x - 1][y - 1] != 1) & (labirynt[x + 1][y + 1] != 1) & (labirynt[x - 1][y + 1] != 1) & (
                        labirynt[x + 1][y - 1] != 1)):
                    labirynt[x][y] = '▩'
            if (roll == 1):
                labirynt[x][y] = '◩'
            if (roll == 2):
                labirynt[x][y] = '◨'

        # gracz - ▣
        # 1 - sciana
        # 2 - wrog
    for i in range(len(labirynt)):
        print(labirynt[i])

    return labirynt
