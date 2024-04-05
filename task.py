def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def count_words(content):
    return len(content.split())
def count_sentences(content):
    sentence_delimiters = ['.', '!', '?', '...']
    sentence_count = 0
    for char in content:
        if char in sentence_delimiters:
            sentence_count += 1
    return sentence_count
def count_words_and_sentences(file_path):
    content = read_file_content(file_path)
    word_count = count_words(content)
    sentence_count = count_sentences(content)
    return word_count, sentence_count
def main(file_path):
    try:
        words, sentences = count_words_and_sentences(file_path)
        print(f"Кількість слів: {words}")
        print(f"Кількість речень: {sentences}")
    except FileNotFoundError:
        print("Вказаний файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
        
if __name__ == "__main__":
    file_path = input("Будь ласка, введіть шлях до файлу у форматі(C:\cicd): ")
    main(file_path)
