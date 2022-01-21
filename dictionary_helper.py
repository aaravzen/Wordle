caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_words_from_webster_dictionary(fname):
    s = set()
    arr = []
    with open(fname) as f:
        for line in f:
            words = line.strip().split()
            if len(words) > 0:
                word = words[0]
            else:
                continue
            
            if word in s or len(word) != 5:
                continue

            if all(c in caps for c in word):
                arr.append(word)
                s.add(word)
    return arr

def get_words_from_words_file(fname):
    s = set()
    arr = []
    with open(fname) as f:
        for line in f:
            word = line.strip().upper()
            if word in s or len(word) != 5:
                continue
            arr.append(word)
            s.add(word)
    return arr

def output_five_word_dictionary(fname, dictionary_contents):
    with open(fname, "w") as f:
        f.write("\n".join(word for word in dictionary_contents))

def pull_word_list_from_dictionary(fname="dictionaries/dictionary.txt"):
    arr = []
    with open(fname) as f:
        for line in f:
            arr.append(line.strip())
    return arr

def webster_workflow():
    # Pulls words from Webster's Unabridged Dictionary off Project Gutenburg
    raw_dict_fname = "dictionaries/raw_dictionary.txt"
    words = get_words_from_webster_dictionary(raw_dict_fname)
    parsed_dict_fname = "dictionaries/websters_dictionary.txt"
    output_five_word_dictionary(parsed_dict_fname, words)

def unix_workflow():
    raw_words_fname = "dictionaries/words.txt"
    words = get_words_from_words_file(raw_words_fname)
    parsed_dict_fname = "dictionaries/unix_dictionary.txt"
    output_five_word_dictionary(parsed_dict_fname, words)

def wordle_workflow():
    raw_words_fname = "dictionaries/wordle_words.txt"
    words = get_words_from_words_file(raw_words_fname)
    parsed_dict_fname = "dictionaries/dictionary.txt"
    output_five_word_dictionary(parsed_dict_fname, words)

def main():
    webster_workflow()
    unix_workflow()
    wordle_workflow()
        
if __name__ == "__main__":
    main()