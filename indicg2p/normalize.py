# indicg2p/normalize.py
# Stage 0 — Text normalization before G2P

import re
import unicodedata

try:
    import emoji
    HAS_EMOJI = True
except ImportError:
    HAS_EMOJI = False


def _remove_emojis(text):
    if HAS_EMOJI:
        return emoji.replace_emoji(text, replace='')
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002500-\U00002BEF"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d\u23cf\u23e9\u231a\ufe0f\u3030"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text)


def _remove_urls(text):
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'www\.\S+', '', text)
    text = re.sub(r'\S+@\S+\.\S+', '', text)
    return text


def _remove_social_noise(text):
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    return text


def _remove_invisible_chars(text):
    invisible = [
        '\u200b', '\u200c', '\u200d',
        '\u200e', '\u200f', '\ufeff', '\u2060',
    ]
    for ch in invisible:
        text = text.replace(ch, '')
    text = text.replace('\u00a0', ' ')
    return text


def _normalize_indic_unicode(text):
    return unicodedata.normalize('NFC', text)


def _remove_symbols(text):
    text = re.sub(
        r'[^\w\s'
        r'\u0900-\u097F'
        r'\u0980-\u09FF'
        r'\u0A00-\u0A7F'
        r'\u0A80-\u0AFF'
        r'\u0B00-\u0B7F'
        r'\u0B80-\u0BFF'
        r'\u0C00-\u0C7F'
        r'\u0C80-\u0CFF'
        r'\u0D00-\u0D7F'
        r'\u0600-\u06FF'
        r'.,?!\'\-]',
        ' ',
        text
    )
    return text


def _clean_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()


def normalize_text(text):
    """
    Main normalizer — call this before any G2P processing.
    Handles: emojis, URLs, mentions, hashtags,
             invisible unicode, Indic unicode normalization,
             symbols, whitespace.
    """
    if not text or not isinstance(text, str):
        return ''
    text = _remove_emojis(text)
    text = _remove_urls(text)
    text = _remove_social_noise(text)
    text = _remove_invisible_chars(text)
    text = _normalize_indic_unicode(text)
    text = _remove_symbols(text)
    text = _clean_whitespace(text)
    return text
