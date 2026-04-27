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

def remove_stopwords(text: str):
    stopwords = {"the", "is", "and", "a", "an"}
    words = re.findall(r"\b\w+\b", text.lower())
    return [word for word in words if word not in stopwords]

def generate_ngrams(text: str, n: int = 2):
    words = re.findall(r"\b\w+\b", text.lower())
    return [" ".join(words[i:i+n]) for i in range(len(words) - n + 1)]
