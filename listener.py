from pynput.keyboard import Key, KeyCode, Listener
from notification.notify import Notification

class KeyListener:

    selection = [Key.f5, Key.f6, Key.f7]

    def __init__(self, standard, dictation, notifier):
        self.ctrl_pressed = False
        self.shift_pressed = False
        self.standard = standard
        self.dictation = dictation
        
        assert isinstance(notifier, Notification), 'notifier must be an instance of Notification'
        self.notifier = notifier

        
    def on_press(self, key):
        if key == Key.ctrl_r: self.ctrl_pressed = True
        elif key == Key.shift_r: self.shift_pressed = True
        elif self.ctrl_pressed and self.shift_pressed and key in KeyListener.selection:
            if KeyListener.selection.index(key) == 2: # Stop Listening
                self.standard.disable()
                self.dictation.disable()
                for notification in self.notifier.notifications.values():
                    notification.close()
                self.notifier.notifications['mute'].show()
            elif KeyListener.selection.index(key) == 0: # Listen in Standard Grammar
                self.standard.enable()
                self.dictation.disable()
                for notification in self.notifier.notifications.values():
                    notification.close()
                self.notifier.notifications['standard'].show()
            elif KeyListener.selection.index(key) == 1: # Listen in Dictation
                self.standard.disable()
                self.dictation.enable()
                for notification in self.notifier.notifications.values():
                    notification.close()
                self.notifier.notifications['dictation'].show()

    def on_release(self, key):
        if key == Key.ctrl_r: self.ctrl_pressed = False
        elif key == Key.shift_r: self.shift_pressed = False

    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == '__main__':
    listener = KeyListener() 