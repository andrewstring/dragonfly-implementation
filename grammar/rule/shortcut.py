from dragonfly import MappingRule, Key

class ShortcutRule(MappingRule):

    mapping = {
        'cancel': Key('c-c'),
        'desktop': Key('w-d'),
        'hide': Key('w-h'),
        'linux': Key('win'),
        'save': Key('c-s')
    }
