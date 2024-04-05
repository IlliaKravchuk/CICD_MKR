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
