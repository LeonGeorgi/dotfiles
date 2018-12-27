import curses
from curses import panel
from subprocess import call
import subprocess
from os import system 

class Menu(object):

    def __init__(self, items, stdscreen):
        self.items = items
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items)-1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            y, x = self.window.getmaxyx()
            y_offset = int((y - len(self.items))/2)
            self.window.refresh()
            curses.doupdate()
            length = 0
            for i in range(0, len(self.items)):
                l = len(self.items[i].message)
                if l > length:
                    length = l 
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                item_ws =  item.with_whitspaces(length)
                self.window.addstr(index + y_offset, item_ws.calculate_x(x), item_ws.message, mode)

            key = self.window.getch()
            # print(str(key))

            if key in [curses.KEY_ENTER, ord('\n')]:
                self.items[self.position].invoke()

            elif key == curses.KEY_UP or key == ord('k'):
                self.navigate(-1)

            elif key == curses.KEY_DOWN or key == ord('j'):
                self.navigate(1)
            elif key == 27 or key == ord('q'):
                exit()
            elif key == curses.KEY_RESIZE:
                self.window.clear()
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class MenuItem(object):
    def __init__(self, message, function):
        self.message = message
        self.function = function

    def invoke(self):
        self.function()

    def with_whitspaces(self, length):
        before = int((length - len(self.message))/2)
        after = length - len(self.message) - before
        return MenuItem(' ' * (before + 1) + self.message + ' ' * (after + 1), self.function)

    def calculate_x(self, width):
        center = width / 2
        message_center = len(self.message) / 2
        return int(center - message_center)


class MyApp(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)
        curses.use_default_colors()

        menu_items = [
                MenuItem('Lock the screen', lock),
                MenuItem('Poweroff', poweroff),
                MenuItem('Reboot', reboot),
                ]
        menu = Menu(menu_items, self.screen)
        menu.display()

def reboot():
    call('reboot')

def poweroff():
    call('poweroff')

def lock():
    #call('lock', True)
    # a = subprocess.Popen('lock', close_fds = True)
    system('lock')
    #time.sleep(1)
    #a.wait()

if __name__ == '__main__':
    curses.wrapper(MyApp)
