from dragonfly import get_engine, Grammar
from grammar.rule.alphabet import AlphabetRule
from grammar.rule.key import KeyRule
from grammar.rule.number import NumberRule
from grammar.rule.word import WordRule

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
number_rule = NumberRule()
word_rule = WordRule()

standard = Grammar('Standard Grammar')
standard.add_rule(alphabet_rule)
standard.add_rule(key_rule)
standard.add_rule(number_rule)
standard.add_rule(word_rule)
standard.load()


engine.connect()
engine.do_recognition()
