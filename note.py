import curses
from curses import wrapper


def curses_main(main_screen):
    main_screen.addstr('test')
    main_screen.refresh()

    curses.napms(2000)


if __name__ == '__main__':
    wrapper(curses_main)