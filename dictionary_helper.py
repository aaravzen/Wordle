caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_words_from_dictionary(fname):
    s = set()
    arr = []
    with open(fname) as f:
        for line in f:
            words = line.strip().split()
            if len(words) > 0:
                word = words[0]
            else:
                continue
            
            if word in s:
                continue
            if len(word) != 5:
                continue

            if all(c in caps for c in word):
                arr.append(word)
                s.add(word)
    return arr

def output_five_word_dictionary(fname, dictionary_contents):
    with open(fname, "w") as f:
        f.write("\n".join(word for word in dictionary_contents))
            
def main():
    raw_dict_fname = "raw_dictionary.txt"
    words = get_words_from_dictionary(raw_dict_fname)
    parsed_dict_fname = "dictionary.txt"
    output_five_word_dictionary(parsed_dict_fname, words)
        
if __name__ == "__main__":
    main()