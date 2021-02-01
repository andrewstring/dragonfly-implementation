from dragonfly import MappingRule, Mouse

class MouseRule(MappingRule):

    mapping = {
        'clip': Mouse('left'),
        'dub clip': Mouse('left:2'),
        'try clip': Mouse('left:3'), 
        'drag': Mouse('left:down'),
        'release': Mouse('left:up'),
        'righty': Mouse('right')
    }
