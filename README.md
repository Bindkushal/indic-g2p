# indic-g2p

A native G2P engine for Indian languages, built for neural TTS systems. Part of the **IndicVoice** research project.

---

## Supported Languages

| Language  | Code | Script     | Status         |
|-----------|------|------------|----------------|
| Hindi     | `hi` | Devanagari | Active      |
| Punjabi   | `pa` | Gurmukhi   | In Progress |
| Bengali   | `bn` | Bengali    | In Progress |
| Tamil     | `ta` | Tamil      | Planned     |
| Telugu    | `te` | Telugu     | Planned     |
| Kannada   | `kn` | Kannada    | Planned     |
| Marathi   | `mr` | Devanagari | Planned     |
| Gujarati  | `gu` | Gujarati   | Planned     |
| Odia      | `or` | Odia       | Planned     |
| Malayalam | `ml` | Malayalam  | Planned     |
| Urdu      | `ur` | Nastaliq   | Planned     |
| Assamese  | `as` | Bengali    | Planned     |

---

## Usage

from indicg2p import hi
g2p = hi.G2P()
phonemes, tokens = g2p("namaste duniya")
print(phonemes)

---

## Installation

pip install indic-g2p

---

## Project Structure

indicg2p/
  __init__.py
  token.py
  transcription.py
  espeak.py
  hi.py
  pa.py
  bn.py
  data/
    hi_dict.json
    pa_dict.json
    bn_dict.json

---

## Part of IndicVoice

Paper: IndicVoice: Decoder-Only Neural TTS with Native G2P for Indian Languages
Model: Coming soon on Hugging Face

---

## Author

Kushal Kant Bind
Department of Mathematics, Chandigarh University, Kharar, Punjab, India
bindkushalkant@gmail.com

---

## License

Apache 2.0
