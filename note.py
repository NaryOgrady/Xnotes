import curses
from curses import wrapper


def curses_main(main_screen):
    curses.start_color()
    curses.use_default_colors()
    setup_layout(main_screen)
    curses.napms(2000)


def setup_layout(main_screen):
    sidebar = curses.newwin(curses.LINES, int(curses.COLS * 0.25), 0, 0)
    sidebar.box()
    sidebar.addstr(1, 20, 'XNOTES')
    main = curses.newwin(curses.LINES, int(
        curses.COLS * 0.75), 0, int(curses.COLS * 0.25))
    main.box()
    main_screen.refresh()
    main.refresh()
    sidebar.refresh()


if __name__ == '__main__':
    wrapper(curses_main)
