# indic-g2p

**A native Grapheme-to-Phoneme (G2P) engine for Indian languages, built for neural TTS.**

Part of the [IndicVoice](https://github.com/Bindkushal/indic-voice) research project — a Kokoro-based decoder-only TTS system for Indic scripts.

**Author:** Kushal Kant Bind — Department of Mathematics, Chandigarh University  
**License:** Apache 2.0

---

## What It Does

`indic-g2p` converts Indian language text into IPA phoneme sequences. It is the text frontend for IndicVoice, analogous to how [Misaki](https://github.com/hexgrad/misaki) serves [Kokoro](https://github.com/hexgrad/kokoro).

```
"नमस्ते दुनिया"  →  indic-g2p  →  n ə m əs t eː d ʊ n ɪ j aː
```

### Pipeline Position

```
Indian Text
    │
    ▼
indic-g2p          ← this repo
(Script → IPA)
    │
    ▼
IndicVoice Neural Decoder
(IPA → Mel → Audio)
    │
    ▼
Speech Audio (24 kHz)
```

---

## How It Works (Three-Stage Pipeline)

1. **Script Normalisation** — Unicode NFC normalisation, conjunct decomposition, nukta and zero-width joiner (ZWJ) handling
2. **Rule-Based Phoneme Mapping** — finite-state transducer maps each script character to IPA symbols with context-sensitive schwa deletion for Hindi/Marathi
3. **Exception Handler** — lookup table for loanwords, numerals, abbreviations, and dialect-specific pronunciations; falls back to `espeak-ng` for unknown words

---

## Supported Languages

| Language   | Code | Script      | Status      |
|------------|------|-------------|-------------|
| Hindi      | `hi` | Devanagari  | ✅ Active   |
| Punjabi    | `pa` | Gurmukhi    | 🔧 Beta     |
| Bengali    | `bn` | Bengali     | 🔧 Beta     |
| Marathi    | `mr` | Devanagari  | ⏳ Planned  |
| Tamil      | `ta` | Tamil       | ⏳ Planned  |
| Telugu     | `te` | Telugu      | ⏳ Planned  |
| Kannada    | `kn` | Kannada     | ⏳ Planned  |
| Gujarati   | `gu` | Gujarati    | ⏳ Planned  |
| Odia       | `or` | Odia        | ⏳ Planned  |
| Malayalam  | `ml` | Malayalam   | ⏳ Planned  |
| Urdu       | `ur` | Nastaliq    | ⏳ Planned  |
| Assamese   | `as` | Bengali     | ⏳ Planned  |
| English    | `en` | Roman       | ✅ Active (via espeak fallback) |

---

## Installation

### From PyPI (once published)
```bash
pip install indic-g2p
```

### From GitHub (current)
```bash
pip install git+https://github.com/Bindkushal/indic-g2p.git
```

### System dependency — espeak-ng (required for fallback)

`espeak-ng` is a **system-level** package, not a Python package. Install it before using the fallback:

```bash
# Ubuntu / Debian / Colab
sudo apt-get install espeak-ng

# macOS
brew install espeak-ng

# Windows
# Download the .msi from https://github.com/espeak-ng/espeak-ng/releases
```

### Optional: English G2P
```bash
pip install "indic-g2p[en]"   # installs spacy for English processing
```

---

## Quick Start

```python
from indicg2p import hi

g2p = hi.G2P()
phonemes, tokens = g2p("नमस्ते दुनिया")
print(phonemes)
# → n ə m əs t eː d ʊ n ɪ j aː
```

### With espeak fallback for out-of-vocabulary words
```python
from indicg2p import hi, espeak

fallback = espeak.EspeakFallback(lang='hi')
g2p = hi.G2P(fallback=fallback)

phonemes, tokens = g2p("नमस्ते OOV_word")
print(phonemes)
```

### Punjabi
```python
from indicg2p import pa

g2p = pa.G2P()
phonemes, tokens = g2p("ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ")
print(phonemes)
```

### Bengali
```python
from indicg2p import bn

g2p = bn.G2P()
phonemes, tokens = g2p("আমার সোনার বাংলা")
print(phonemes)
```

---

## Project Structure

```
indic-g2p/
├── indicg2p/
│   ├── __init__.py        # language routing, LANG_CODES map
│   ├── token.py           # Token dataclass
│   ├── transcription.py   # text chunking and normalisation
│   ├── espeak.py          # espeak-ng fallback for OOV words
│   ├── hi.py              # Hindi G2P
│   ├── pa.py              # Punjabi G2P
│   ├── bn.py              # Bengali G2P
│   └── data/
│       ├── hi_dict.json   # Hindi pronunciation dictionary
│       ├── pa_dict.json   # Punjabi dictionary
│       └── bn_dict.json   # Bengali dictionary
├── examples/
├── tests/
├── pyproject.toml
└── README.md
```

---

## G2P API Reference

Every language module exposes the same interface:

```python
class G2P:
    def __init__(self, fallback=None):
        """
        fallback: optional EspeakFallback instance for OOV words.
                  If None, OOV words are passed through unchanged.
        """

    def __call__(self, text: str) -> tuple[str, list]:
        """
        Args:
            text: Input string in the target script.
        Returns:
            phonemes: Space-separated IPA string.
            tokens:   List of Token objects with grapheme/phoneme pairs.
        """
```

---

## Contributing — Adding a New Language

We welcome contributions for any Indian scheduled language.

1. Fork this repo
2. Create `indicg2p/XX.py` (ISO 639-1 code)
3. Implement `class G2P` with `__call__(text) -> (phonemes, tokens)`
4. Add dictionary at `indicg2p/data/XX_dict.json`
5. Register in `indicg2p/__init__.py` under `LANG_CODES`
6. Add tests in `tests/test_XX.py` — minimum 10 sample words
7. Open a Pull Request with: language name, script, phoneme inventory size

If you are a native speaker wanting to contribute phoneme rules or pronunciation data, open an Issue — all contributions welcome.

---

## Roadmap

| Version | Target |
|---------|--------|
| v0.1 | Hindi + Punjabi + Bengali |
| v1.0 | Full schwa deletion, tone handling, espeak fallback |
| v1.1 | Tamil + Telugu (Dravidian) |
| v2.0 | All 22 scheduled Indian languages |
| v2.1 | Seq2seq fallback model for OOV words |
| v3.0 | BERT-based homograph disambiguation |

---

## Citation

```bibtex
@misc{bind2025indicvoice,
  title     = {IndicVoice: Decoder-Only Neural TTS with Native G2P for Indian Languages},
  author    = {Kushal Kant Bind},
  year      = {2025},
  institution = {Chandigarh University},
  url       = {https://github.com/Bindkushal/indic-voice}
}
```

---

## Related

- **IndicVoice TTS** → [github.com/Bindkushal/indic-voice](https://github.com/Bindkushal/indic-voice)
- **Model on HuggingFace** → [huggingface.co/Bindkushal/indic-voice](https://huggingface.co/Bindkushal/indic-voice)
- **Kokoro TTS** (architecture base) → [github.com/hexgrad/kokoro](https://github.com/hexgrad/kokoro)
- **Misaki G2P** (inspiration) → [github.com/hexgrad/misaki](https://github.com/hexgrad/misaki)
