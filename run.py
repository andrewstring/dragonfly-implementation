import threading

from dragonfly import get_engine, Grammar

# import standard grammar rules
from grammar.rule.alphabet import AlphabetRule
from grammar.rule.key import KeyRule
from grammar.rule.mouse import MouseRule
from grammar.rule.number import NumberRule
from grammar.rule.shortcut import ShortcutRule
from grammar.rule.word import WordRule

# import dictation rule
from grammar.rule.dictation import DictationRule

from listener import KeyListener

engine = get_engine("kaldi",
  model_dir='kaldi_model',
  tmp_dir='kaldi_tmp',
  audio_input_device='Q9-1',
  audio_self_threaded=True,
  audio_auto_reconnect=True,
  audio_reconnect_callback=None,
  retain_dir=None,
  retain_audio=None,
  retain_metadata=None,
  retain_approval_func=None,
  vad_aggressiveness=3,
  vad_padding_start_ms=150,
  vad_padding_end_ms=150,
  vad_complex_padding_end_ms=500,
  auto_add_to_user_lexicon=True,
  lazy_compilation=True,
  invalidate_cache=False,
  expected_error_rate_threshold=None,
  alternative_dictation=None,
  cloud_dictation_lang='en-US',
  )

alphabet_rule = AlphabetRule()
key_rule = KeyRule()
mouse_rule = MouseRule()
number_rule = NumberRule()
shortcut_rule = ShortcutRule()
word_rule = WordRule()

standard = Grammar('Standard Grammar')
standard.add_rule(alphabet_rule)
standard.add_rule(key_rule)
standard.add_rule(mouse_rule)
standard.add_rule(number_rule)
standard.add_rule(shortcut_rule)
standard.add_rule(word_rule)
standard.load()

dictation_rule = DictationRule()

dictation = Grammar('Dictation Grammar')
dictation.add_rule(dictation_rule)
dictation.load()

def start_listening(engine):
    engine.connect()
    engine.do_recognition()

listener = KeyListener(standard=standard, dictation=dictation)

try:
    voice_thread = threading.Thread(target=start_listening, args=(engine,))
    listener_thread = threading.Thread(target=listener.start, args=())
    voice_thread.start()
    listener_thread.start()
except: print('error starting thread')
