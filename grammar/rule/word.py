from dragonfly import MappingRule, Text, Dictation

class WordRule(MappingRule):

    mapping = {
            'word <text>': Text('%(text)s')
    }

    extras = [ Dictation('text') ]
