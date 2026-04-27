import re

def _syllable_count(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prev = False
    for c in word:
        is_vowel = c in vowels
        if is_vowel and not prev:
            count += 1
        prev = is_vowel
    if word.endswith("e"):
        count = max(1, count - 1)
    return count or 1

def flesch_reading_ease(text: str) -> float:
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    words = re.findall(r"\b\w+\b", text)
    syllables = sum(_syllable_count(w) for w in words)

    if not sentences or not words:
        return 0.0

    wps = len(words) / len(sentences)
    spw = syllables / len(words)

    return 206.835 - (1.015 * wps) - (84.6 * spw)
