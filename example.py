import curses
from curses import wrapper


def main(main_screen):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    if curses.has_colors():
        curses.start_color()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # UI
    main_screen.addstr('RANDOM QUOTES', curses.A_REVERSE)
    main_screen.chgat(-1, curses.A_REVERSE)
    main_screen.addstr(curses.LINES-1, 0,
                       'Press "R" to request a new quote, "Q" to quit')
    main_screen.chgat(curses.LINES-1, 7, 1,
                      curses.A_BOLD | curses.color_pair(2))
    main_screen.chgat(curses.LINES-1, 35, 1,
                      curses.A_BOLD | curses.color_pair(1))

    main_screen.refresh()
    curses.napms(2000)


if __name__ == '__main__':
    wrapper(main)
