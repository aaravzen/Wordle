from dictionary_helper import pull_word_list_from_dictionary

def create_frequency_dict(word_list):
    freq = {}
    for word in word_list:
        unique_letters = set(word)
        for letter in unique_letters:
            if letter not in freq:
                freq[letter] = 0
            freq[letter] += 1
    return freq

def create_frequency_graph(frequency_distribution, max_bar_length=80):
    letters = [x for x in frequency_distribution.items()]
    letters.sort(key=lambda x : x[1], reverse=True)
    most = letters[0][1]
    lines = []
    for letter,occurences in letters:
        bar_length = occurences * max_bar_length // most
        line = f"{letter} "
        for i in range(bar_length):
            line += "X"
        line += f" {occurences}"
        lines.append(line)
    return lines

def write_frequency_graph(fname, frequency_distribution, word_count):
    frequency_graph = create_frequency_graph(frequency_distribution)
    with open(fname, "w") as f:
        f.write(f"How many five-letter words out of {word_count} contain each letter:\n\n")
        f.write("\n".join(line for line in frequency_graph))
        f.write('\n\nie. the word "AARAV" would only increment the count of A by 1')
        f.write("\n(but that word isn't included because it's not in the dictionary, dw)")

def main():
    word_list = pull_word_list_from_dictionary()
    frequency_dict = create_frequency_dict(word_list)
    frequency_fname = "frequency.txt"
    write_frequency_graph(frequency_fname, frequency_dict, len(word_list))
        
if __name__ == "__main__":
    main()