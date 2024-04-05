import pytest
from task import count_words, count_sentences, count_words_and_sentences

@pytest.fixture
def sample_content():
    # Приклад вмісту файлу для тестування
    return "Це приклад тексту. Це друге речення! А це третє. Останнє... Або ні?"

@pytest.mark.parametrize("content, expected_word_count", [
    ("Це приклад тексту.", 3),
    ("Це друге речення!", 3),
    ("А це третє.", 3),
    ("Останнє...", 2),
    ("Або ні?", 2),
    ("", 0),  # Порожній рядок
    ("Тест деякий текст з числами 123 456.", 7),  # Текст з числами
])
def test_count_words(content, expected_word_count):
    assert count_words(content) == expected_word_count

@pytest.mark.parametrize("content, expected_sentence_count", [
    ("Це приклад тексту.", 1),
    ("Це друге речення!", 1),
    ("А це третє.", 1),
    ("Останнє...", 1),
    ("Або ні?", 1),
    ("Це речення! І ще одне.", 2),
    ("", 0),  # Порожній рядок
    ("Запитання з трьома крапками...", 1),  # Речення з трьома крапками
])
def test_count_sentences(content, expected_sentence_count):
    assert count_sentences(content) == expected_sentence_count

@pytest.mark.parametrize("content, expected_word_count, expected_sentence_count", [
    ("Це приклад тексту. Це друге речення! А це третє.", 9, 3),
    ("Останнє... Або ні?", 4, 2),
    ("", 0, 0),  # Порожній рядок
    ("Тест з числами 123 456. Текст без розділових знаків", 7, 2),
])
def test_count_words_and_sentences(content, expected_word_count, expected_sentence_count):
    words, sentences = count_words_and_sentences(content)
    assert words == expected_word_count
    assert sentences == expected_sentence_count
