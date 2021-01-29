from pynput.keyboard import Key, Listener

class KeyListener:

    def __init__(self, grammar):
        self.ctrl_pressed = False
        self.grammar = grammar
        
    def on_press(self, key):
        if key == Key.ctrl: self.ctrl_pressed = True
        elif self.ctrl_pressed and key == Key.shift:
            if self.grammar.enabled:
                self.grammar.disable()
                print('STOPPED LISTENING')
            else:
                self.grammar.enable()
                print('STARTED LISTENING')

    def on_release(self, key):
        if key == Key.ctrl: self.ctrl_pressed = False

    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
