#!/usr/bin/env python3
"""
indic-g2p usage examples
"""

# Hindi example
from indicg2p import hi

g2p = hi.G2P()
phonemes, tokens = g2p("नमस्ते दुनिया")
print("Hindi:", phonemes)

# English fallback example
from indicg2p import en

g2p_en = en.G2P(trf=False, british=False, fallback=None)
phonemes_en, tokens_en = g2p_en("Hello world")
print("English:", phonemes_en)
