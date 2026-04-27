# text-utils-lab
A tiny, practical Python library for common text processing tasks.

## Features
- Word count
- Sentence splitting
- Keyword extraction (simple frequency-based)
- Cosine similarity
- Readability (Flesch Reading Ease)

## Installation

```bash
pip install -e .
```

## Usage

```python
from text_utils.basic import word_count, sentence_split
from text_utils.similarity import cosine_similarity
from text_utils.readability import flesch_reading_ease

text = "Hello world. This is a simple example."

print(word_count(text))
print(sentence_split(text))
print(flesch_reading_ease(text))
```

## License
MIT
