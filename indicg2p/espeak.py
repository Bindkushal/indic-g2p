from phonemizer.backend.espeak.wrapper import EspeakWrapper
from typing import Tuple
import re

# Use system espeak-ng — more reliable than espeakng-loader
try:
    import espeakng_loader
    lib_path = espeakng_loader.get_library_path()
    if lib_path:
        EspeakWrapper.set_library(lib_path)
except Exception:
    pass  # Fall back to system espeak-ng

# EspeakFallback is used as a last resort for English
class EspeakFallback:
    E2M = sorted({
        'ʔˌn\u0329':'ʔn', 'ʔn\u0329':'ʔn',
    }.items(), key=lambda x: -len(x[0]))

    def __init__(self, british=False):
        import phonemizer
        self.backend = phonemizer.backend.EspeakBackend(
            language='en-gb' if british else 'en-us',
            preserve_punctuation=True,
            with_stress=True,
        )

    def __call__(self, text):
        result = self.backend.phonemize([text], strip=True)
        return result[0] if result else ''

class EspeakG2P:
    def __init__(self, language='hi'):
        import phonemizer
        self.backend = phonemizer.backend.EspeakBackend(
            language=language,
            preserve_punctuation=True,
            with_stress=True,
        )

    def __call__(self, text):
        from indicg2p.token import MToken
        result = self.backend.phonemize([text], strip=True)
        phonemes = result[0] if result else ''
        tokens = [(text, phonemes)]
        return phonemes, tokens
