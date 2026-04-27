from text_utils.basic import word_count, sentence_split, keyword_extract
from text_utils.similarity import cosine_similarity
from text_utils.readability import flesch_reading_ease

print(word_count("hello world"))
print(sentence_split("Hello world. This is a test!"))
print(keyword_extract("AI is useful and AI is powerful"))
print(cosine_similarity("hello world", "hello there"))
print(flesch_reading_ease("Hello world. This is a simple test."))