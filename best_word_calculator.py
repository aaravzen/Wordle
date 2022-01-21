def get_best_words(fname):
    ret = []
    with open(fname) as f:
        for line in f:
            rank,word,score = line.split()
            score = int(score.replace("(","").replace(")",""))
            ret.append((word,score))
    return ret

def get_yellow_words():
    return get_best_words("wordle_results/wordle_most_yellow_words.txt")

def get_green_words():
    return get_best_words("wordle_results/wordle_most_green_words.txt")

def find_best_words():
    yellow_words = get_yellow_words()
    green_words = get_green_words()
    green_dict = {x[0]:x[1] for x in green_words}
    combined_words = []
    for word,yellow_score in yellow_words:
        green_score = green_dict[word]
        combined_words.append((word, yellow_score, green_score))
    combined_words.sort(key=lambda x: (x[1],x[2]), reverse=True)
    return combined_words

def get_sorted_best_word_list():
    best_words = find_best_words()
    return [x[0] for x in best_words]

def main():
    best_words = find_best_words()
    with open("wordle_results/wordle_best_words.txt", "w") as f:
        f.write("\n".join(f"{idx+1}. {w_t[0]} ({w_t[1]}, {w_t[2]})" for idx,w_t in enumerate(best_words)))

if __name__ == "__main__":
    main()