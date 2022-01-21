from dictionary_helper import pull_word_list_from_dictionary
from frequency_calculator import create_frequency_dict

def get_words_with_most_yellows(word_list, frequency_dist):
    word_value_tuples = []
    for word in word_list:
        wordset = set(word)
        score = 0
        for letter in wordset:
            score += frequency_dist[letter]
        word_value_tuples.append((word, score))
    word_value_tuples.sort(key=lambda x: x[1], reverse=True)
    return word_value_tuples

def main():
    word_list = pull_word_list_from_dictionary()
    frequency_dict = create_frequency_dict(word_list)
    most_yellow_words = get_words_with_most_yellows(word_list, frequency_dict)
    with open("wordle_results/wordle_most_yellow_words.txt", "w") as f:
        f.write("\n".join(f"{idx+1}. {score_tuple[0]} ({score_tuple[1]})" for idx,score_tuple in enumerate(most_yellow_words)))

if __name__ == "__main__":
    main()