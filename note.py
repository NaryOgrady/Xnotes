import curses
from curses import wrapper


def curses_main(main_screen):
    main_screen.addstr('test')
    max_y, max_x = main_screen.getmaxyx()
    sidebar = curses.newwin(max_y, 78, 0, 0)
    sidebar.box()
    main_screen.refresh()
    sidebar.refresh()
    curses.napms(2000)


if __name__ == '__main__':
    wrapper(curses_main)