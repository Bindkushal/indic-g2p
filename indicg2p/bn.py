# Bengali G2P module for indicg2p
# Language: Bengali | Code: bn | Script: Bengali
# Author: Kushal Kant Bind

VOWELS = {
    'অ': 'ɔ', 'আ': 'aː', 'ই': 'i', 'ঈ': 'iː',
    'উ': 'u', 'ঊ': 'uː', 'এ': 'e', 'ঐ': 'oj',
    'ও': 'o', 'ঔ': 'ow',
    # Matras
    'া': 'aː', 'ি': 'i', 'ী': 'iː',
    'ু': 'u', 'ূ': 'uː', 'ে': 'e',
    'ৈ': 'oj', 'ো': 'o', 'ৌ': 'ow',
}

CONSONANTS = {
    'ক': 'k', 'খ': 'kʰ', 'গ': 'ɡ', 'ঘ': 'ɡʱ',
    'ঙ': 'ŋ', 'চ': 'tʃ', 'ছ': 'tʃʰ', 'জ': 'dʒ',
    'ঝ': 'dʒʱ', 'ঞ': 'n', 'ট': 'ʈ', 'ঠ': 'ʈʰ',
    'ড': 'ɖ', 'ঢ': 'ɖʱ', 'ণ': 'n', 'ত': 't',
    'থ': 'tʰ', 'দ': 'd', 'ধ': 'dʱ', 'ন': 'n',
    'প': 'p', 'ফ': 'pʰ', 'ব': 'b', 'ভ': 'bʱ',
    'ম': 'm', 'য': 'dʒ', 'র': 'r', 'ল': 'l',
    'শ': 'ʃ', 'ষ': 'ʃ', 'স': 's', 'হ': 'h',
}

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
        while i < len(word):
            char = word[i]
            if char in self.consonants:
                result.append(self.consonants[char])
                if i + 1 >= len(word) or word[i+1] not in self.vowels:
                    result.append('ɔ')  # inherent vowel in Bengali
            elif char in self.vowels:
                result.append(self.vowels[char])
            i += 1
        return result
