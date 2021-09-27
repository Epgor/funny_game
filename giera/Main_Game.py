from Hero import Hero
from random import randint
from random import choice
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from Labirynt import Generate
from PIL import Image, ImageTk
from itertools import count


class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


Jon = Hero()
Jon.stats()

Jon.lvl_up()

pos_x = 10
pos_y = 10

Labirynt = [[' '] * (20) for i in range(20)]
Labirynt = Generate(Labirynt)

Labirynt[pos_y][pos_x] = '▣'

def move_south():
    global pos_y
    global pos_x
    roll = randint(1, 100)
    if Jon.is_dead():
        a = 1
    else:
        if (Labirynt[pos_y+1][pos_x] == '◼'):
            lbl.unload()
            lbl.load('victory.gif')
            return "You have finished a level! - comming soon"

        if (Labirynt[pos_y + 1][pos_x] == '▣'):
            Labirynt[pos_y + 1][pos_x] = '◫'
            lbl.unload()
            lbl.load('body.gif')
            Jon.gold += 1000
            Jon.defence += 4
            Jon.attack += 4
            Jon.lvl_up
            Jon.hp -= 10
            return "You found a looted dead body of your ancestor"

        if (Labirynt[pos_y+1][pos_x] == '▩'):
            lbl.unload()
            lbl.load('wall.gif')
            return "Oups! I hit a wall!"

        if (Labirynt[pos_y+1][pos_x] == '◫'):
            Labirynt[pos_y+1][pos_x] = '▣'
            Labirynt[pos_y][pos_x] = '◫'
            pos_y += 1
            lbl.unload()
            lbl.load('giphy.gif')
            return "You moved south!"

        else:
            if (Labirynt[pos_y+1][pos_x] == '◨'):
                Labirynt[pos_y+1][pos_x] = '▣'
                Labirynt[pos_y][pos_x] = '◫'
                pos_y +=1
                temp = Jon.gold
                Jon.travel_event_gold()
                if temp < Jon.gold:
                    lbl.unload()
                    lbl.load('treasure.gif')
                    return "You found some gold!"
                else:
                    lbl.unload()
                    lbl.load('trapchest.gif')
                    return "You lost some gold!"
            if (Labirynt[pos_y+1][pos_x] == '◩'):
                if roll < 30:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(5, 10) + ((pos_x ** 2 + pos_y ** 2) / 5))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y + 1][pos_x] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_y += 1
                    return "You have been attacked by BRUTAL: " + bufforek
                else:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(1, 10) + ((pos_x ** 2 + pos_y ** 2) / 20))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y + 1][pos_x] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_y += 1
                    return "You have been attacked by: " + bufforek


def move_north():
    global pos_y
    global pos_x
    roll = randint(1, 100)
    if Jon.is_dead():
        a = 1
    else:
        if (Labirynt[pos_y-1][pos_x] == '◼'):
            lbl.unload()
            lbl.load('victory.gif')
            return "You have finished a level! - comming soon"

        if (Labirynt[pos_y - 1][pos_x] == '▣'):
            Labirynt[pos_y - 1][pos_x] = '◫'
            lbl.unload()
            lbl.load('body.gif')
            Jon.gold += 1000
            Jon.defence += 4
            Jon.attack += 4
            Jon.lvl_up
            Jon.hp -= 10
            return "You found a looted dead body of your ancestor"

        if (Labirynt[pos_y-1][pos_x] == '▩'):
            lbl.unload()
            lbl.load('wall.gif')
            return "Oups! I hit a wall!"

        if (Labirynt[pos_y-1][pos_x] == '◫'):
            Labirynt[pos_y-1][pos_x] = '▣'
            Labirynt[pos_y][pos_x] = '◫'
            pos_y -= 1
            lbl.unload()
            lbl.load('giphy.gif')
            return "You moved north!"

        else:
            if (Labirynt[pos_y-1][pos_x] == '◨'):
                Labirynt[pos_y-1][pos_x] = '▣'
                Labirynt[pos_y][pos_x] = '◫'
                pos_y -=1
                temp = Jon.gold
                Jon.travel_event_gold()
                if temp < Jon.gold:
                    lbl.unload()
                    lbl.load('treasure.gif')
                    return "You found some gold!"
                else:
                    lbl.unload()
                    lbl.load('trapchest.gif')
                    return "You lost some gold!"
            if (Labirynt[pos_y-1][pos_x] == '◩'):
                if roll < 30:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(5, 10) + ((pos_x ** 2 + pos_y ** 2) / 5))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y - 1][pos_x] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_y -= 1
                    return "You have been attacked by BRUTAL: " + bufforek
                else:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(1, 10) + ((pos_x ** 2 + pos_y ** 2) / 20))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y - 1][pos_x] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_y -= 1

                    return "You have been attacked by: "+ bufforek



def move_west():
    global pos_y
    global pos_x
    roll = randint(1, 100)
    if Jon.is_dead():
        a = 1
    else:
        if (Labirynt[pos_y][pos_x-1] == '◼'):
            lbl.unload()
            lbl.load('victory.gif')
            return "You have finished a level! - comming soon"

        if (Labirynt[pos_y][pos_x-1] == '▣'):
            Labirynt[pos_y][pos_x-1] = '◫'
            lbl.unload()
            lbl.load('body.gif')
            Jon.gold += 1000
            Jon.defence += 4
            Jon.attack += 4
            Jon.lvl_up
            Jon.hp -= 10
            return "You found a looted dead body of your ancestor"


        if (Labirynt[pos_y][pos_x-1] == '▩'):
            lbl.unload()
            lbl.load('wall.gif')
            return "Oups! I hit a wall!"

        if (Labirynt[pos_y][pos_x-1] == '◫'):
            Labirynt[pos_y][pos_x-1] = '▣'
            Labirynt[pos_y][pos_x] = '◫'
            pos_x -= 1
            lbl.unload()
            lbl.load('giphy.gif')
            return "You moved west!"

        else:
            if (Labirynt[pos_y][pos_x-1] == '◨'):
                Labirynt[pos_y][pos_x-1] = '▣'
                Labirynt[pos_y][pos_x] = '◫'
                pos_x -=1
                temp = Jon.gold
                Jon.travel_event_gold()
                if temp < Jon.gold:
                    lbl.unload()
                    lbl.load('treasure.gif')
                    return "You found some gold!"
                else:
                    lbl.unload()
                    lbl.load('trapchest.gif')
                    return "You lost some gold!"
            if (Labirynt[pos_y][pos_x-1] == '◩'):
                if roll < 30:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(5, 10) + ((pos_x ** 2 + pos_y ** 2) / 5))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y][pos_x - 1] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_x -= 1

                    return "You have been attacked by BRUTAL: " + bufforek

                else:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(1, 10) + ((pos_x ** 2 + pos_y ** 2) / 20))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y][pos_x - 1] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_x -= 1

                    return "You have been attacked by: "+ bufforek



def move_east():
    global pos_y
    global pos_x
    roll = randint(1, 100)
    if Jon.is_dead():
        a = 1
    else:
        if (Labirynt[pos_y][pos_x + 1] == '◼'):
            lbl.unload()
            lbl.load('victory.gif')
            return "You have finished a level! - comming soon"

        if (Labirynt[pos_y][pos_x+1] == '▣'):
            Labirynt[pos_y][pos_x+1] = '◫'
            lbl.unload()
            lbl.load('body.gif')
            Jon.gold += 1000
            Jon.defence += 4
            Jon.attack += 4
            Jon.lvl_up
            Jon.hp -= 10
            return "You found a looted dead body of your ancestor"

        if (Labirynt[pos_y][pos_x + 1] == '▩'):
            lbl.unload()
            lbl.load('wall.gif')
            return "Oups! I hit a wall!"

        if (Labirynt[pos_y][pos_x + 1] == '◫'):
            Labirynt[pos_y][pos_x + 1] = '▣'
            Labirynt[pos_y][pos_x] = '◫'
            pos_x += 1
            lbl.unload()
            lbl.load('giphy.gif')
            return "You moved east!"

        else:
            if (Labirynt[pos_y][pos_x + 1] == '◨'):
                Labirynt[pos_y][pos_x + 1] = '▣'
                Labirynt[pos_y][pos_x] = '◫'
                pos_x += 1
                temp = Jon.gold
                Jon.travel_event_gold()
                if temp < Jon.gold:
                    lbl.unload()
                    lbl.load('treasure.gif')
                    return "You found some gold!"
                else:
                    lbl.unload()
                    lbl.load('trapchest.gif')
                    return "You lost some gold!"
            if (Labirynt[pos_y][pos_x + 1] == '◩'):
                if roll < 30:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(5, 10) + ((pos_x ** 2 + pos_y ** 2) / 5))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y][pos_x + 1] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_x += 1
                    return "You have been attacked by BRUTAL: " + bufforek
                else:
                    list_fight = ["Angry Woman", "Hornet", "Old Man", "None Chump", "Japanese Weirdo"]
                    Jon.travel_event_fight(randint(1, 10) + ((pos_x ** 2 + pos_y ** 2) / 20))
                    bufforek = choice(list_fight)
                    if bufforek == "Angry Woman":
                        lbl.unload()
                        lbl.load('angrywoman.gif')
                    if bufforek == "Hornet":
                        lbl.unload()
                        lbl.load('hornet.gif')
                    if bufforek == "Old Man":
                        lbl.unload()
                        lbl.load('oldman.gif')
                    if bufforek == "None Chump":
                        lbl.unload()
                        lbl.load('tenor.gif')
                    if bufforek == "Japanese Weirdo":
                        lbl.unload()
                        lbl.load('japan.gif')
                    Labirynt[pos_y][pos_x + 1] = '▣'
                    Labirynt[pos_y][pos_x] = '◫'
                    pos_x += 1
                    return "You have been attacked by: "+ bufforek

def current_pos():
    return pos_x, pos_y


window = Tk()
window.title("Night Rider")
window.geometry('1000x720')

field_text = ""

stat = Message(window, text=f"{Jon.stats()}")
stat.grid(column=0,  row=3, columnspan=3, sticky=W)

m1 = Message(window, text=f"Total score = {Jon.gold}")
m1.grid(column=6,  row=2, columnspan=3, sticky=W)

m = Message(window, text="Welcome to the 'Night Rider', as You can see, You are an alone rider, lost in the night. "
                         "You are trying to get home. Will you find a way out of"
                         " the Cursed Maze?""Will You solve the Mystery of the Cursed Maze???")

text2=''

for i in range(len(Labirynt)):
    for j in range(len(Labirynt[i])):
        text2 += Labirynt[i][j]

    text2 += '\n'

l = Message(window, text=text2)
#l.configure(font="-monotype-andale mono-medium-r-normal--12-120-75-75-m-0-iso8859-1")
m.grid(column=6,  row=4, columnspan=3, sticky=W)

l.grid(column=6,  row=3, columnspan=3, sticky=W)

def update_window(arg):
    global field_text
    field_text = str(arg) + '\n' + field_text
    if Jon.is_dead():
        lbl.unload()
        lbl.load('dead.gif')
        field_text = "You died!"
    else:
        m1.configure(text=f"Total score = {Jon.gold}")
        stat.configure( text=f"{Jon.stats()}")

    m.configure(text=field_text)
    text2=''
    for i in range(len(Labirynt)):
        for j in range(len(Labirynt[i])):
            text2 += Labirynt[i][j]

        text2 += '\n'

    l.configure(text=text2)


def btn_lvl_up():
    if Jon.is_lvl_up() == 1:
        Jon.lvl_up()
        lbl.unload()
        lbl.load('lvlup.gif')
    else:
        lbl.unload()
        lbl.load('noexp.gif')
        update_window("Not enough EXP!")


def btn_stats_func():
    global Jon
    global pos_y
    global pos_x
    Jon = Hero()
    Jon.lvl_up()
    pos_y = 10
    pos_x = 10
    lbl.unload()
    lbl.load('new.gif')
    update_window("New Game Started!")
    update_window("New Jon has been born!")
    Labirynt[pos_y][pos_x] = '▣'
    text2=''
    for i in range(len(Labirynt)):
        for j in range(len(Labirynt[i])):
            text2 += Labirynt[i][j]

        text2 += '\n'

    l.configure(text=text2)


def btn_move_north():
    update_window(move_north())


def btn_move_south():
    update_window(move_south())


def btn_move_east():
    update_window(move_east())


def btn_move_west():
    update_window(move_west())


def heal():
    lbl.unload()
    lbl.load('health.gif')
    update_window(Jon.heal())


def position():
    lbl.unload()
    lbl.load('where.gif')
    update_window(f"Your current position is X: {pos_x}, Y: {pos_y}")


def train():
    if Jon.gold >= 1000:
        roll = randint(1, 2)
        if roll == 1:
            Jon.attack += 1
            Jon.gold -= Jon.attack * 100
            lbl.unload()
            lbl.load('wood.gif')
            update_window("You chop wood for whole day! Attack +1")
        else:
            Jon.defence += 1
            Jon.gold -= Jon.defence * 100
            lbl.unload()
            lbl.load('muscle.gif')
            update_window("You flex your muscles very hard! Defence +1")
    else:
        lbl.unload()
        lbl.load('nogold.gif')
        update_window("Not enough Gold!")

#def pop_up():



# def btn_exit():
#     global exit_game
#     exit_game = 0
btn_stats = Button(window, text='Train', command=train)
btn_stats.grid(column=3, row=2)

btn_stats = Button(window, text='New Game', command=btn_stats_func)
btn_stats.grid(column=3, row=0)

btn_stats = Button(window, text='Position', command=position)
btn_stats.grid(column=1, row=2)

btn_stats = Button(window, text='Heal', command=heal)
btn_stats.grid(column=2, row=1)
#
# btn_stats = Button(window, text='EXIT', command=Jon.Exit())
# btn_stats.grid(column=1, row=2)

btn_lvl_up = Button(window, text='Level Up!', command=btn_lvl_up)
btn_lvl_up.grid(column=1, row=0)

btn_north = Button(window, text='North', command=btn_move_north)
btn_north.grid(column=2, row=0)

btn_south = Button(window, text='South', command=btn_move_south)
btn_south.grid(column=2, row=2)

btn_east = Button(window, text='East', command=btn_move_east)
btn_east.grid(column=3, row=1)

btn_west = Button(window, text='West', command=btn_move_west)
btn_west.grid(column=1, row=1)

img2 = PhotoImage(file="Night_Rider.png")
Iim2 = Label(window, image=img2)
Iim2.grid(column=5, row=0, rowspan=2)



# e = Entry(window)
# e.pack()

# style = Style()
#
# style.theme_use('default')
#
# style.configure("black.Horizontal.TProgressbar", background='black')
#
# bar = Progressbar(window, length=100, style='black.Horizontal.TProgressbar')
#
# bar_progress = Jon.exp_bar()
#
# bar['value'] = Jon.exp_bar()

#bar.grid(column=5, row=0)
lbl = ImageLabel(window)
lbl.grid(column=5, row=3)
lbl.load('giphy.gif')
window.mainloop()
