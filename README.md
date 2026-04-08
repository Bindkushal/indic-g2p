# indic-g2p

A native Grapheme-to-Phoneme (G2P) engine for Indian languages, built for neural TTS systems. Part of the **IndicVoice** research project.

---

## How It Works

indic-g2p converts Indian language text into IPA phoneme sequences in three stages:

1. **Script Normalisation** - Unicode NFC normalisation, conjunct decomposition, nukta and zero-width joiner handling
2. **Rule-Based Phoneme Mapping** - finite-state transducer maps each script character to IPA symbols with context-sensitive schwa deletion for Hindi
3. **Exception Handler** - lookup table for loanwords, numbers, abbreviations and dialect-specific pronunciations

Input: Indian text (any supported script)
Output: IPA phoneme sequence + token list

Example:
  Input:  namaste
  Output: n ə m ə s t eː

---

## Supported Languages

| Language  | Code | Script     | Status      |
|-----------|------|------------|-------------|
| Hindi     | hi   | Devanagari | Active      |
| Punjabi   | pa   | Gurmukhi   | In Progress |
| Bengali   | bn   | Bengali    | In Progress |
| Tamil     | ta   | Tamil      | Planned     |
| Telugu    | te   | Telugu     | Planned     |
| Kannada   | kn   | Kannada    | Planned     |
| Marathi   | mr   | Devanagari | Planned     |
| Gujarati  | gu   | Gujarati   | Planned     |
| Odia      | or   | Odia       | Planned     |
| Malayalam | ml   | Malayalam  | Planned     |
| Urdu      | ur   | Nastaliq   | Planned     |
| Assamese  | as   | Bengali    | Planned     |

---

## Usage

  from indicg2p import hi
  g2p = hi.G2P()
  phonemes, tokens = g2p("namaste duniya")
  print(phonemes)

---

## Installation

  pip install indic-g2p

Or clone locally:

  git clone https://github.com/Bindkushal/indic-g2p.git
  cd indic-g2p
  pip install -e .

---

## How IndicVoice Uses This

IndicVoice is a lightweight decoder-only neural TTS system for Indian languages. indic-g2p is its text frontend.

  Indian Text
      |
  indic-g2p  <-- this repo
      |
  IPA Phonemes
      |
  IndicVoice Neural Decoder
      |
  Speech Audio (24kHz)

Without a proper Indic G2P layer, the TTS model receives incorrect phoneme inputs, directly reducing naturalness and intelligibility. This is why indic-g2p exists as a standalone module - it can also be used independently of IndicVoice in any Indic NLP pipeline.

---

## Project Structure

  indicg2p/
    __init__.py        language routing and LANG_CODES map
    token.py           Token dataclass
    transcription.py   text chunking logic
    espeak.py          fallback for unknown words
    hi.py              Hindi G2P module
    pa.py              Punjabi G2P module
    bn.py              Bengali G2P module
    data/
      hi_dict.json     Hindi pronunciation dictionary
      pa_dict.json     Punjabi dictionary
      bn_dict.json     Bengali dictionary

---

## Contributing

We welcome contributions for any Indian language. To add a new language:

1. Fork this repo
2. Create a new file indicg2p/XX.py where XX is the ISO 639-1 language code
3. Follow the same class structure as hi.py
   - Class must be named G2P
   - Must implement __call__(text) returning (phonemes, tokens)
4. Add your pronunciation dictionary at indicg2p/data/XX_dict.json
5. Register your language in indicg2p/__init__.py under LANG_CODES
6. Add tests in tests/test_XX.py with at least 10 sample words
7. Open a Pull Request with language name, script, and phoneme inventory size

Every Indian scheduled language is welcome. If you are a native speaker and want to contribute phoneme rules or pronunciation data, open an Issue.

---

## Roadmap

- v1.0 - Hindi and Punjabi with full schwa deletion and tone handling
- v1.1 - Bengali support
- v1.2 - Tamil and Telugu (Dravidian family)
- v2.0 - All 22 scheduled Indian languages
- v2.1 - Seq2seq fallback model for OOV words
- v3.0 - BERT-based homograph disambiguation

---

## Citation

If you use indic-g2p in your research, please cite:

  Bind, K. K. (2025). IndicVoice: Decoder-Only Neural TTS with Native G2P
  for Indian Languages. Department of Mathematics, Chandigarh University.

---

## Part of IndicVoice

Paper: IndicVoice: Decoder-Only Neural TTS with Native G2P for Indian Languages
TTS Repo: Coming soon
Model on Hugging Face: Coming soon

---

## Author

Kushal Kant Bind
Department of Mathematics, Chandigarh University, Kharar, Punjab, India
bindkushalkant@gmail.com

---

## License

Apache 2.0 - see LICENSE

Builds on the Misaki G2P engine architecture by hexgrad.
