from dragonfly import MappingRule, Text, Dictation

class DictationRule(MappingRule):

    mapping = {
        '<text>': Text('%(text)s')
    }

    extras = [ Dictation('text') ]