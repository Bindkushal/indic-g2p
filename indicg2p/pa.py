# indicg2p/pa.py — Punjabi (Gurmukhi) G2P
# Author: Kushal Kant Bind | IndicVoice Research Project

import regex
from typing import Optional, List, Tuple

VOWELS = {
    'ਅ': 'ə', 'ਆ': 'aː', 'ਇ': 'ɪ', 'ਈ': 'iː',
    'ਉ': 'ʊ', 'ਊ': 'uː', 'ਏ': 'eː', 'ਐ': 'ɛː',
    'ਓ': 'oː', 'ਔ': 'ɔː',
}

MATRAS = {
    'ਾ': 'aː', 'ਿ': 'ɪ', 'ੀ': 'iː',
    'ੁ': 'ʊ', 'ੂ': 'uː', 'ੇ': 'eː',
    'ੈ': 'ɛː', 'ੋ': 'oː', 'ੌ': 'ɔː',
    'ੰ': '̃',   # tippi — nasalise
    'ਂ': '̃',   # bindi — nasalise
    'ੱ': '',    # addak — geminate next consonant (handled below)
    '੍': '',    # virama
}

CONSONANTS = {
    'ਕ': 'k', 'ਖ': 'kʰ', 'ਗ': 'ɡ', 'ਘ': 'ɡʱ', 'ਙ': 'ŋ',
    'ਚ': 'tʃ', 'ਛ': 'tʃʰ', 'ਜ': 'dʒ', 'ਝ': 'dʒʱ', 'ਞ': 'ɲ',
    'ਟ': 'ʈ', 'ਠ': 'ʈʰ', 'ਡ': 'ɖ', 'ਢ': 'ɖʱ', 'ਣ': 'ɳ',
    'ਤ': 't', 'ਥ': 'tʰ', 'ਦ': 'd', 'ਧ': 'dʱ', 'ਨ': 'n',
    'ਪ': 'p', 'ਫ': 'pʰ', 'ਬ': 'b', 'ਭ': 'bʱ', 'ਮ': 'm',
    'ਯ': 'j', 'ਰ': 'r', 'ਲ': 'l', 'ਵ': 'ʋ',
    'ਸ': 's', 'ਹ': 'h', 'ੜ': 'ɽ',
}

# Punjabi tone rules
# Low tone: words starting with voiced aspirates
LOW_TONE = {'ਘ', 'ਝ', 'ਢ', 'ਧ', 'ਭ'}
# High tone: words starting with ਹ
HIGH_TONE = {'ਹ'}

VIRAMA = '੍'
ADDAK = 'ੱ'

def _word_to_ipa(word: str) -> str:
    result = []
    i = 0
    # Tone detection
    if word and word[0] in HIGH_TONE:
        result.append('˥')
    elif word and word[0] in LOW_TONE:
        result.append('˩')

    while i < len(word):
        ch = word[i]

        # Addak — geminate the next consonant
        if ch == ADDAK:
            i += 1
            if i < len(word) and word[i] in CONSONANTS:
                result.append(CONSONANTS[word[i]] * 2)
                i += 1
            continue

        if ch in CONSONANTS:
            result.append(CONSONANTS[ch])
            # Check next char
            nxt = word[i+1] if i+1 < len(word) else ''
            if nxt == VIRAMA:
                i += 2  # suppress inherent vowel
                continue
            elif nxt in MATRAS:
                result.append(MATRAS[nxt])
                i += 2
                continue
            elif nxt not in CONSONANTS and nxt not in VOWELS and nxt != ADDAK:
                result.append('ə')  # inherent schwa
        elif ch in VOWELS:
            result.append(VOWELS[ch])
        elif ch in MATRAS:
            result.append(MATRAS[ch])

        i += 1
    return ''.join(result)


class G2P:
    def __call__(self, text: str) -> Tuple[str, List[Tuple[str, str]]]:
        words = text.strip().split()
        tokens = []
        parts = []
        for word in words:
            ipa = _word_to_ipa(word)
            tokens.append((word, ipa))
            parts.append(ipa)
        return ' '.join(parts), tokens
