import curses


myscreen = curses.initscr()
myscreen.addstr(12, 25, "See Curses, See Curses Run!")
myscreen.getch()
myscreen.addstr(12, 25, " {}".format(myscreen.getch()))
curses.endwin()