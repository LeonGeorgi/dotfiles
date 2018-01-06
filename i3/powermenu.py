import curses
from curses import panel
from subprocess import call
import subprocess

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
            for index, item in enumerate(self.items):                        
                if index == self.position:                                   
                    mode = curses.A_REVERSE                                  
                else:                                                        
                    mode = curses.A_NORMAL                                   

                msg =  item.message                            
                self.window.addstr(index + y_offset, item.calculate_x(x), msg, mode)

            key = self.window.getch()
            # print(str(key))

            if key in [curses.KEY_ENTER, ord('\n')]:                         
                if self.position == len(self.items)-1:                       
                    break                                                    
                else:                                                        
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

def poweroff():
    call('poweroff')

def reboot():
    call('reboot')

def lock():
    #call('lock', True)
    a = subprocess.Popen('lock', close_fds = True)
    #time.sleep(1)
    #a.wait()
    #exit()

if __name__ == '__main__':                                                       
    curses.wrapper(MyApp)   
