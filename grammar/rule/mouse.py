from dragonfly import MappingRule, Mouse

class MouseRule(MappingRule):

    mapping = {
        'click': Mouse('left'),
        'dub click': Mouse('left:2'),
        'drag': Mouse('left:down'),
        'release': Mouse('left:up'),
        'righty': Mouse('right')
    }
