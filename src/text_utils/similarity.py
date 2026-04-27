from collections import Counter
import math
import re

def _vectorize(text: str):
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)

def cosine_similarity(a: str, b: str) -> float:
    v1 = _vectorize(a)
    v2 = _vectorize(b)
    intersection = set(v1.keys()) & set(v2.keys())
    num = sum(v1[x] * v2[x] for x in intersection)
    sum1 = sum(v**2 for v in v1.values())
    sum2 = sum(v**2 for v in v2.values())
    denom = math.sqrt(sum1) * math.sqrt(sum2)
    return num / denom if denom else 0.0

def jaccard_similarity(a: str, b: str) -> float:
    words_a = set(re.findall(r"\b\w+\b", a.lower()))
    words_b = set(re.findall(r"\b\w+\b", b.lower()))

    if not words_a or not words_b:
        return 0.0

    intersection = words_a & words_b
    union = words_a | words_b

    return len(intersection) / len(union)
