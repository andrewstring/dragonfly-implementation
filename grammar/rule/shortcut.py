from dragonfly import MappingRule, Key

class ShortcutRule(MappingRule):

    mapping = {
        'cancel': Key('c-c'),
        'copy': Key('c-c'),
        'desktop': Key('w-d'),
        'hide': Key('w-h'),
        'linux': Key('win'),
        'linux lock': Key('w-l'),
        'paste': Key('c-v'),
        'save': Key('c-s')
    }
