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
    for letter in caps:
        heatmap = create_letter_heatmap(letter, word_list)
        heatmap_graphic = create_heatmap_graphic(heatmap)
        heatmap_strings.append(f"heatmap for {letter} is:\n{heatmap}\n{heatmap_graphic}\n")
    return heatmap_strings

def write_heatmap_strings(heatmap_strings):
    with open("heatmaps.txt", "w") as f:
        f.write("\n".join(line for line in heatmap_strings))

def main():
    word_list = pull_word_list_from_dictionary()
    hm_strings = create_letter_heatmaps(word_list)
    write_heatmap_strings(hm_strings)
        
if __name__ == "__main__":
    main()