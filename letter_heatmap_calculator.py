from dictionary_helper import pull_word_list_from_dictionary

def create_letter_heatmap(letter, word_list):
    heatmap = [0] * 5
    for word in word_list:
        for idx,c in enumerate(word):
            if c == letter:
                heatmap[idx] += 1
    return heatmap

def create_heatmap_graphic(heatmap, max_length=10):
    most = max(heatmap)
    bar_lengths = []
    for position,occurences in enumerate(heatmap):
        bar_length = occurences * max_length // most
        bar_lengths.append(bar_length)
    
    lines = []
    for i in range(max_length):
        line = " "
        for j in bar_lengths:
            if i < j:
                line += "X    "
            else:
                line += "     "
        lines.append(line)
    return "\n".join(x for x in reversed(lines))

def create_letter_heatmaps(word_list):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    heatmap_strings = []
    heatmaps = {}
    for letter in caps:
        heatmap = create_letter_heatmap(letter, word_list)
        heatmap_graphic = create_heatmap_graphic(heatmap)
        heatmap_strings.append(f"heatmap for {letter} is:\n{heatmap}\n{heatmap_graphic}\n")
        heatmaps[letter] = heatmap
    return heatmaps, heatmap_strings

def write_heatmap_strings(heatmap_strings):
    with open("unix_results/unix_heatmaps.txt", "w") as f:
        f.write("\n".join(line for line in heatmap_strings))

def compare_words_with_heatmaps(word_list, heatmaps):
    score_tuples = []
    for word in word_list:
        score = 0
        for idx,c in enumerate(word):
            score += heatmaps[c][idx]
        t = (word, score)
        score_tuples.append(t)
    
    score_tuples.sort(key=lambda a : a[1], reverse=True)
    return score_tuples

def write_most_green_words(most_green_words):
    with open("unix_results/unix_most_green_words.txt", "w") as f:
        f.write("\n".join(f"{idx+1}. {score_tuple[0]} ({score_tuple[1]})" for idx,score_tuple in enumerate(most_green_words)))

def main():
    word_list = pull_word_list_from_dictionary()
    heatmaps, hm_strings = create_letter_heatmaps(word_list)
    write_heatmap_strings(hm_strings)
    most_green_words = compare_words_with_heatmaps(word_list, heatmaps)
    write_most_green_words(most_green_words)
        
if __name__ == "__main__":
    main()