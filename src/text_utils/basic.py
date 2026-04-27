import re
from collections import Counter

def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))

def sentence_split(text: str):
    return [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]

def keyword_extract(text: str, top_k: int = 5):
    words = re.findall(r"\b\w+\b", text.lower())
    counts = Counter(words)
    return [w for w, _ in counts.most_common(top_k)]
