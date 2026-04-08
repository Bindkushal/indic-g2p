# Punjabi (Gurmukhi) G2P module for indicg2p
# Language: Punjabi | Code: pa | Script: Gurmukhi
# Author: Kushal Kant Bind

import regex

# Gurmukhi vowel carriers and matras → IPA
VOWELS = {
    'ਅ': 'ə', 'ਆ': 'aː', 'ਇ': 'ɪ', 'ਈ': 'iː',
    'ਉ': 'ʊ', 'ਊ': 'uː', 'ਏ': 'eː', 'ਐ': 'æː',
    'ਓ': 'oː', 'ਔ': 'ɔː',
    # Matras
    'ਾ': 'aː', 'ਿ': 'ɪ', 'ੀ': 'iː',
    'ੁ': 'ʊ', 'ੂ': 'uː', 'ੇ': 'eː',
    'ੈ': 'æː', 'ੋ': 'oː', 'ੌ': 'ɔː',
}

CONSONANTS = {
    'ਕ': 'k', 'ਖ': 'kʰ', 'ਗ': 'ɡ', 'ਘ': 'ɡʱ',
    'ਚ': 'tʃ', 'ਛ': 'tʃʰ', 'ਜ': 'dʒ', 'ਝ': 'dʒʱ',
    'ਟ': 'ʈ', 'ਠ': 'ʈʰ', 'ਡ': 'ɖ', 'ਢ': 'ɖʱ',
    'ਤ': 't', 'ਥ': 'tʰ', 'ਦ': 'd', 'ਧ': 'dʱ',
    'ਪ': 'p', 'ਫ': 'pʰ', 'ਬ': 'b', 'ਭ': 'bʱ',
    'ਨ': 'n', 'ਮ': 'm', 'ਰ': 'r', 'ਲ': 'l',
    'ਵ': 'ʋ', 'ਸ': 's', 'ਹ': 'h', 'ਯ': 'j',
    'ਙ': 'ŋ', 'ਞ': 'ɲ', 'ਣ': 'ɳ', 'ਲ਼': 'ɭ',
    'ੜ': 'ɽ',
}

# Tones: Punjabi has 3 tones
# High tone: words starting with ਹ
# Low tone: voiced aspirates ਘ ਝ ਢ ਧ ਭ
# Mid tone: default

HIGH_TONE_MARKER = 'ˉ'
LOW_TONE_MARKER = 'ˬ'

HIGH_TONE_INITIALS = {'ਹ'}
LOW_TONE_CONSONANTS = {'ਘ', 'ਝ', 'ਢ', 'ਧ', 'ਭ'}

class G2P:
    def __init__(self):
        self.vowels = VOWELS
        self.consonants = CONSONANTS

    def __call__(self, text):
        from indicg2p.token import MToken
        tokens = []
        phonemes = []
        words = text.strip().split()
        for word in words:
            ps = self._word_to_phonemes(word)
            phonemes.extend(ps)
            tokens.append(MToken(text=word, phonemes=''.join(ps)))
        return ' '.join(phonemes), tokens

    def _word_to_phonemes(self, word):
        result = []
        i = 0
        # Detect tone
        tone = ''
        if word and word[0] in HIGH_TONE_INITIALS:
            tone = HIGH_TONE_MARKER
        elif word and word[0] in LOW_TONE_CONSONANTS:
            tone = LOW_TONE_MARKER
        if tone:
            result.append(tone)
        while i < len(word):
            char = word[i]
            if char in self.consonants:
                result.append(self.consonants[char])
                # Check for inherent vowel (schwa) if no matra follows
                if i + 1 < len(word) and word[i+1] not in self.vowels:
                    if i + 1 == len(word) - 1 or word[i+1] in self.consonants:
                        result.append('ə')
            elif char in self.vowels:
                result.append(self.vowels[char])
            i += 1
        return result
