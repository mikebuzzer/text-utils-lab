from text_utils.basic import (
    word_count,
    sentence_split,
    keyword_extract,
    remove_stopwords,
    generate_ngrams,
)

from text_utils.similarity import cosine_similarity, jaccard_similarity
from text_utils.readability import flesch_reading_ease

def test_word_count_simple():
    assert word_count("hello world") == 2

def test_word_count_with_punctuation():
    assert word_count("Hello, world!") == 2

def test_word_count_empty_text():
    assert word_count("") == 0

def test_word_count_numbers():
    assert word_count("python 3 is cool") == 4

def test_sentence_split_period():
    assert sentence_split("Hello world. This is a test.") == [
        "Hello world",
        "This is a test",
    ]

def test_sentence_split_multiple_punctuation():
    assert sentence_split("Hello! Are you okay? Yes.") == [
        "Hello",
        "Are you okay",
        "Yes",
    ]

def test_sentence_split_empty_text():
    assert sentence_split("") == []

def test_sentence_split_extra_spaces():
    assert sentence_split(" Hello world.   This is a test. ") == [
        "Hello world",
        "This is a test",
    ]

def test_keyword_extract_basic():
    assert keyword_extract("AI is useful and AI is powerful", top_k=2) == [
        "ai",
        "useful",
    ]

def test_keyword_extract_top_k():
    assert keyword_extract("python python data ai ai ai", top_k=2) == [
        "ai",
        "python",
    ]

def test_keyword_extract_empty_text():
    assert keyword_extract("") == []

def test_keyword_extract_case_normalization():
    assert keyword_extract("Python python PYTHON", top_k=1) == ["python"]

def test_remove_stopwords_basic():
    result = remove_stopwords("AI is the future and the future is powerful")
    assert result == ["ai", "future", "future", "powerful"]

def test_remove_stopwords_no_stopwords():
    assert remove_stopwords("python data science") == [
        "python",
        "data",
        "science",
    ]

def test_remove_stopwords_empty_text():
    assert remove_stopwords("") == []

def test_remove_stopwords_with_punctuation():
    assert remove_stopwords("The AI, and the future!") == ["ai", "future"]

def test_generate_ngrams_bigrams():
    assert generate_ngrams("hello world test", 2) == [
        "hello world",
        "world test",
    ]

def test_generate_ngrams_trigrams():
    assert generate_ngrams("one two three four", 3) == [
        "one two three",
        "two three four",
    ]

def test_generate_ngrams_single_word():
    assert generate_ngrams("hello", 2) == []

def test_generate_ngrams_empty_text():
    assert generate_ngrams("", 2) == []

def test_generate_ngrams_with_punctuation():
    assert generate_ngrams("Hello, world! Test.", 2) == [
        "hello world",
        "world test",
    ]

def test_cosine_similarity_identical_text():
    assert cosine_similarity("hello world", "hello world") == 1.0

def test_cosine_similarity_partial_overlap():
    assert round(cosine_similarity("hello world", "hello there"), 2) == 0.50

def test_cosine_similarity_no_overlap():
    assert cosine_similarity("cat dog", "apple banana") == 0.0

def test_cosine_similarity_empty_text():
    assert cosine_similarity("", "hello world") == 0.0

def test_jaccard_similarity_identical_text():
    assert jaccard_similarity("hello world", "hello world") == 1.0

def test_jaccard_similarity_partial_overlap():
    assert round(jaccard_similarity("hello world", "hello there"), 2) == 0.33

def test_jaccard_similarity_no_overlap():
    assert jaccard_similarity("cat dog", "apple banana") == 0.0

def test_jaccard_similarity_empty_text():
    assert jaccard_similarity("", "hello world") == 0.0

def test_flesch_reading_ease_simple_text():
    assert flesch_reading_ease("Hello world. This is a simple test.") > 0

def test_flesch_reading_ease_empty_text():
    assert flesch_reading_ease("") == 0.0

def test_flesch_reading_ease_single_sentence():
    score = flesch_reading_ease("This is a readable sentence.")
    assert isinstance(score, float)
