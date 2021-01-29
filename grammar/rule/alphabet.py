from dragonfly import MappingRule, Key

class AlphabetRule(MappingRule):

    mapping = {
            'air': Key('a'), 'bat': Key('b'), 'cap': Key('c'), 'drum': Key('d'), 'each': Key('e'), 'fine': Key('f'),
            'gust': Key('g'), 'harp': Key('h'), 'sit': Key('i'), 'jury': Key('j'), 'crunch': Key('k'), 'look': Key('l'),
            'made': Key('m'), 'near': Key('n'), 'odd': Key('o'), 'pit': Key('p'), 'quench': Key('q'), 'red': Key('r'),
            'sun': Key('s'), 'trap': Key('t'), 'urge': Key('u'), 'vest': Key('v'), 'whip': Key('w'), 'plex': Key('x'),
            'yank': Key('y'), 'zip': Key('z'), 'upper air': Key('A'), 'upper bat': Key('B'), 'upper cap': Key('C'),
            'upper drum': Key('D'), 'upper each': Key('E'), 'upper fine': Key('F'), 'upper gust': Key('G'), 'upper harp': Key('H'),
            'upper sit': Key('I'), 'upper jury': Key('J'), 'upper crunch': Key('K'), 'upper look': Key('L'), 'upper made': Key('M'),
            'upper near': Key('N'), 'upper odd': Key('O'), 'upper pit': Key('P'), 'upper quench': Key('Q'), 'upper red': Key('R'),
            'upper sun': Key('S'), 'upper trap': Key('T'), 'upper urge': Key('U'), 'upper vest': Key('V'), 'upper whip': Key('W'),
            'upper plex': Key('X'), 'upper yank': Key('Y'), 'upper zip': Key('Z')
    }
