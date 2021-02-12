from pynput.keyboard import Key, KeyCode, Listener

class KeyListener:

    selection = [Key.f1, Key.f2, Key.f3]

    def __init__(self, standard, dictation):
        self.ctrl_pressed = False
        self.shift_pressed = False
        self.standard = standard
        self.dictation = dictation

        
    def on_press(self, key):
        if key == Key.ctrl: self.ctrl_pressed = True
        elif key == Key.shift: self.shift_pressed = True
        elif self.ctrl_pressed and self.shift_pressed and key in KeyListener.selection:
            if KeyListener.selection.index(key) == 0: # Stop Listening
                self.standard.disable()
                self.dictation.disable()
                print('STOPPED LISTENING')
            elif KeyListener.selection.index(key) == 1: # Listen in Standard Grammar
                self.standard.enable()
                self.dictation.disable()
                print('LISTENING IN STANDARD MODE')
            elif KeyListener.selection.index(key) == 2: # Listen in Dictation
                self.standard.disable()
                self.dictation.enable()
                print('LISTENING IN DICTATION MODE')

    def on_release(self, key):
        if key == Key.ctrl: self.ctrl_pressed = False
        elif key == Key.shift: self.shift_pressed = False

    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()