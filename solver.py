from best_word_calculator import get_sorted_best_word_list

def calculate_refreshed_yellow_words(word_list, greens):
    # calculate modified frequency distribution
    frequency_dist = {}
    for word in word_list:
        unique_letters = set()
        for idx,c in enumerate(greens):
            if c == '-':
                unique_letters.add(word[idx])
        for letter in unique_letters:
            if letter not in frequency_dist:
                frequency_dist[letter] = 0
            frequency_dist[letter] += 1
    # calculate words with most yellow in modified fashion
    word_value_tuples = []
    for word in word_list:
        wordset = set()
        for idx,c in enumerate(greens):
            if c == '-':
                wordset.add(word[idx])
        score = 0
        for letter in wordset:
            score += frequency_dist[letter]
        word_value_tuples.append((word, score))
    word_value_tuples.sort(key=lambda x: x[1], reverse=True)
    return word_value_tuples

def word_finder(word_list, greens, yellows, reds, singles, multiples):
    ret = []
    for word in word_list:
        good = True
        remaining_yellows = yellows[:]

        for letter in multiples:
            if word.count(letter) < 2:
                good = False
        
        for letter in singles:
            if word.count(letter) != 1:
                good = False

        for idx,c in enumerate(word):
            if greens[idx] != "-" and greens[idx] != c:
                good = False
                break
            if c in reds:
                good = False
                break
            for jdx,yellow_letter_tuple in enumerate(yellows):
                yellow_letter,kdx = yellow_letter_tuple
                if idx == kdx and c == yellow_letter:
                    good = False
                    break
            if not good:
                break

            remaining_yellows = [x for x in remaining_yellows if x[0] != c]
        
        if good and not len(remaining_yellows):
            ret.append(word)
    return ret

def calculate_new_colors(guess,response,greens,yellows,reds,singles,multiples):
    new_greens = ""
    good_letters = set()
    for idx,color in enumerate(response):
        if color.upper() == "G":
            new_greens += guess[idx]
            if guess[idx] in good_letters:
                multiples.add(guess[idx])
            good_letters.add(guess[idx])
        elif color.upper() == "Y":
            yellows.append((guess[idx],idx))
            new_greens += greens[idx]
            if guess[idx] in good_letters:
                multiples.add(guess[idx])
            good_letters.add(guess[idx])
        else:
            new_greens += greens[idx]
    
    for idx,color in enumerate(response):
        if color.upper() != "G" and color.upper() != "Y":
            if guess[idx] not in good_letters:
                reds += guess[idx]
            else:
                singles.add(guess[idx])
    return new_greens,reds


def main():
    greens = "-----"
    yellows = []
    reds = ""
    confirmed_singles = set()
    confirmed_multiples = set()
    word_list = get_sorted_best_word_list()
    found = word_finder(word_list, greens, yellows, reds, confirmed_singles, confirmed_multiples)
    guess = found[0]
    print(f"Hi, welcome to your personalized wordle solver! Start with {guess}")
    print("What does that give you?")
    user_answer = input()
    wordle_round = 1
    while user_answer.upper() != "GGGGG" and wordle_round < 6:
        wordle_round += 1
        greens,reds = calculate_new_colors(guess, user_answer, greens, yellows, reds, confirmed_singles, confirmed_multiples)
        print(f"\ngreens: {greens}")
        print(f"yellows: {yellows}")
        print(f"reds: {reds}")
        print(f"singles: {confirmed_singles}")
        print(f"multiples: {confirmed_multiples}\n")
        found = word_finder(word_list, greens, yellows, reds, confirmed_singles, confirmed_multiples)
        found = get_sorted_best_word_list(calculate_refreshed_yellow_words(found, greens))
        guess = found[0]
        print(f"These are you options now: {', '.join(w for w in found)}")
        print(f"Press enter to use {guess}, or else type what you want to use")
        user_guess = input().strip().upper()
        if user_guess == "GGGGG":
            user_answer = "GGGGG"
            break
        while "-" in user_guess:
            print("don't think you wanted to do that champ. try again")
            user_guess = input().strip().upper()
        if user_guess != "":
            guess = user_guess
        print(f"You used {guess}. What does that give you?")
        user_answer = input()
    if user_answer.upper() == "GGGGG":
        print(f"Yay! you just got the wordle in {wordle_round} rounds!")
    else:
        greens,reds = calculate_new_colors(guess, user_answer, greens, yellows, reds, confirmed_singles, confirmed_multiples)
        found = word_finder(word_list, greens, yellows, reds, confirmed_singles, confirmed_multiples)
        print("I'm sorry you didn't get the wordle :( The other possible words are:")
        print("\n".join(word for word in found))
    
        
if __name__ == "__main__":
    main()