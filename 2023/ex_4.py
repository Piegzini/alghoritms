# file_path = 'Dane_2305/slowa.txt'
file_path = 'Dane_2305/przyklad.txt'
file = open(file_path, 'r')
file_content = file.readlines()

result_file_path = 'wyniki/wyniki4_1.txt'


def save_wk_words():
    wk_words = []

    for word in file_content:
        letters = [*word.strip()]

        w_count = get_letter_count(letters, 'w')
        k_count = get_letter_count(letters, 'k')

        if check_wk_word(w_count, k_count):
            wk_words.append(word)

def check_wk_word(w_count, k_count):
    if w_count == 0 or k_count == 0:
        return False
    if w_count != k_count:
        return False

    return True


def get_letter_count(letters, symbol):
    w_filtered = filter(lambda element: element == symbol, letters)
    return len(tuple(w_filtered))



# file.close()
# result_file = open(result_file_path, 'w')
#
# for wk_word in wk_words:
#     result_file.write(wk_word)
#
# result_file.close()

def count_words(filename):
    words = []
    with open(filename, 'r') as file:
        words = file.read().splitlines()

    word = 'wakacje'
    word_counts = {char: word.count(char) for char in word}
    result = []

    for line in words:
        line_counts = {char: line.count(char) for char in line}
        counts = [min(line_counts.get(char, 0), word_counts[char]) for char in word_counts]
        result.append(min(counts))

    return result


result = count_words(file_path)

with open('wyniki4_2.txt', 'w') as file:
    file.write(' '.join(map(str, result[:50])))