from best_word_calculator import get_sorted_best_word_list

def word_finder(word_list, greens, yellows, reds):
    ret = []
    for word in word_list:
        good = True
        remaining_yellows = yellows[:]
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

def calculate_new_colors(guess,response,greens,yellows,reds):
    new_greens = ""
    for idx,color in enumerate(response):
        if color.upper() == "G":
            new_greens += guess[idx]
        elif color.upper() == "Y":
            yellows.append((guess[idx],idx))
            new_greens += greens[idx]
        else:
            reds += guess[idx]
            new_greens += greens[idx]
    return new_greens,yellows,reds


def main():
    greens = "-----"
    yellows = []
    reds = ""
    word_list = get_sorted_best_word_list()
    found = word_finder(word_list, greens, yellows, reds)
    guess = found[0]
    print(f"Hi, welcome to your personalized wordle solver! Start with {guess}")
    print("What does that give you?")
    user_answer = input()
    wordle_round = 1
    while user_answer.upper() != "GGGGG" and wordle_round < 6:
        greens,yellows,reds = calculate_new_colors(guess, user_answer, greens, yellows, reds)
        print(f"\ngreens: {greens}")
        print(f"yellows: {yellows}")
        print(f"reds: {reds}\n")
        found = word_finder(word_list, greens, yellows, reds)
        guess = found[0]
        print(f"These are you options now: {', '.join(w for w in found)}")
        print(f"Press enter to use {guess}, or else type what you want to use")
        user_guess = input().strip().upper()
        if user_guess != "":
            guess = user_guess
        print(f"You used {guess}. What does that give you?")
        user_answer = input()
        wordle_round += 1
    if user_answer.upper() == "GGGGG":
        print(f"Yay! you just got the wordle in {wordle_round} rounds!")
    else:
        greens,yellows,reds = calculate_new_colors(guess, user_answer, greens, yellows, reds)
        found = word_finder(word_list, greens, yellows, reds)
        print("I'm sorry you didn't get the wordle :( The other possible words are:")
        print("\n".join(word for word in found))
    
        
if __name__ == "__main__":
    main()