# indicg2p - Native G2P engine for Indian languages
# Based on Misaki G2P architecture (hexgrad/misaki)
# Extended for Indian languages by Kushal Kant Bind

LANG_CODES = {
    'hi': 'Hindi',
    'pa': 'Punjabi',
    'bn': 'Bengali',
    'ta': 'Tamil',
    'te': 'Telugu',
    'kn': 'Kannada',
    'mr': 'Marathi',
    'gu': 'Gujarati',
    'or': 'Odia',
    'ml': 'Malayalam',
    'ur': 'Urdu',
    'as': 'Assamese',
    'en': 'English',
}

def get_g2p(lang_code):
    if lang_code == 'hi':
        from indicg2p import hi
        return hi.G2P()
    elif lang_code == 'pa':
        from indicg2p import pa
        return pa.G2P()
    elif lang_code == 'bn':
        from indicg2p import bn
        return bn.G2P()
    elif lang_code == 'en':
        from indicg2p import en
        return en.G2P(trf=False, british=False, fallback=None)
    else:
        raise NotImplementedError(f"Language '{lang_code}' ({LANG_CODES.get(lang_code, 'unknown')}) is not yet implemented. Contributions welcome at https://github.com/Bindkushal/indic-g2p")
