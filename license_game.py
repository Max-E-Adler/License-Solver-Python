import os
import re

longest_perfects = ['greens', 'ocreae', 'otaria', 'orpins', 'nasial', 'atorai', 'mesial', 'mesial', 'mesail', 'mesail', 'ordeal', 'scotia', 'nasial', 'nosine', 'nudens']

def main():
    words_list = dictionary_filepath_to_wordslist()
    perfect_regex = perfect_finder_regex_from_string("eae")
    output_list = matches_from_wordslist_and_regex(words_list, perfect_regex)
    print(output_list)
    # aaa_zzz_matches_loop(words_list)
    # check_wordlist_for_longest_perfect_actual_word(words_list))
    # print(check_wordlist_for_truncated(words_list))
    # for word in longest_perfects:
    #     print(word)
    #     print(word in words_list)
    #     print(str(matches_from_wordslist_and_regex(words_list, perfect_finder_regex_from_string(word))))
    # consecutive_alphabet_checker(words_list)
    print(grade_word("lmnppo", "lmno"))
    

def grade_word(input, key):
    #given an input and a key against which the input may be graded, return a "score" that is higher the closer it is to perfect

    if re.search(perfect_finder_regex_from_string(key), input):
        return 100 #this is a perfect perfect perfect!! great job!!!
    elif re.search(finder_regex_from_string(key), input):
        
        # regex_string = r'\w+(?=l)|(?<=l)\w+(?=m)|(?<=m)\w+(?=n)|(?<=n)\w+(?=o)|(?<=o)\w+'  #this was a test string using 'lmno' as the inputs, from there I built the components
        # #                aaaaaa1bbbbbb1ccccccc2bbbbbb2ccccccc3bbbbbb3ccccccc4bbbbbb4dddd
        a_component = r'\w+(?='
        b_component = r')|(?<='
        c_component = r')\w+(?='
        d_component = r')\w+'

        output = a_component
        for index, char in enumerate(key):
            output += char + b_component + char
            if index != len(key) - 1:
                output += c_component
        output += d_component
        substrings = re.findall(output, input)
        return substrings
    else:
        return 0 #this one does not work

def grade_substrings(input):
    one_letter_grade = 100


# longest_perfects = ['greens', 'ocreae', 'otaria', 'orpins', 'nasial', 'atorai', 'mesial', 'mesial', 'mesail', 'mesail', 'ordeal', 'scotia', 'nasial', 'nosine', 'nudens'] came from this function
def check_wordlist_for_truncated(wordslist):
    max_length = 0
    output = []
    for word in wordslist:
        if len(word) % 2 == 0:
            continue
        check_string = word[1::2]
        is_in = check_string in wordslist
        if is_in and len(check_string) > max_length:
            max_length = len(check_string)
            output = [check_string]
        elif is_in and len(check_string) == max_length:
            output += [check_string]
    return output


def matches_from_wordslist_and_regex(wordslist, regex):
    output_list = []

    for word in wordslist:
        if re.search(regex, word):
            output_list.append(word)

    return output_list

def perfect_finder_regex_from_string(input_string):
    regex = "^."
    for char in input_string:
        regex += char + "."
    regex += "$"
    return regex

def finder_regex_from_string(input_string):
    regex = "^.*"
    for char in input_string:
        regex += char + ".*"
    regex += "$"
    return regex

def dictionary_filepath_to_wordslist(dictionary_filepath = "C://Users//MaxAd//Desktop//python//words_alpha.txt"):

    #filepath = input("What's the filepath?")
    # filepath = "C://Users//MaxAd//Desktop//python"
    # files = os.listdir(filepath)
    # counter = 0
    # for filename in files:
    #     print (str(counter) + ": " + filename)
    #     counter += 1
    # filecounter = int(input("Which file would you like to use as your dictionary?\n"))
    # dictionary_filepath = filepath + "//" +  files[filecounter]
    with open(dictionary_filepath) as f:
        words_list = f.read().splitlines()
    return words_list

def aaa_zzz_matches_loop(wordslist):
    characters = "abcdefghijklmnopqrstuvwxyz"
    max_length = 0
    longest_string = ""
    output = []
    for char1 in characters:
        for char2 in characters:
            for char3 in characters:
                chars = char1 + char2 + char3
                perfect_regex = perfect_finder_regex_from_string(chars)
                output_list = matches_from_wordslist_and_regex(wordslist, perfect_regex)
                print(chars + ": " + str(len(output_list)))
                if len(output_list) > max_length:
                    max_length = len(output_list)
                    output = output_list
                    longest_string = chars
                    print("new max length! wooooooooooooooooooooooooooooooooooooooooooo")
                    print("max_length: " + str(max_length))
                    print("longest_string: " + longest_string)
                    print("output: " + str(output))

    print("max_length: " + str(max_length))
    print("longest_string: " + longest_string)
    print("output: " + str(output))

def consecutive_alphabet_checker(wordslist):
    #here are the results of this function when it went to the end of the alphabet
# abcde
# ['abecedaire', 'abecedaries', 'abjectedness', 'aborticide', 'absconded', 'abscondedly', 'abscondence', 'absconder', 'absconders', 'abstractedness', 'amblycephalidae', 'ambuscade', 'ambuscaded', 'ambuscader', 'ambuscades', 'ambuscadoed', 'amebicide', 'amoebicide', 'bambocciade', 'bambochade', 'carbacidometer', 'cerambycidae', 'nonabstractedness', 'oxylabracidae', 'scabicide', 'unabstractedness']
# defgh
# ['underfreight']
# efghi
# ['firefighting', 'prizefighting', 'refighting', 'refugeeship', 'scientificogeographical']
# klmno
# ['alkylamino', 'kilmarnock']
# lmnop
# ['albuminoscope', 'albuminurophobia', 'alimentotherapy', 'aluminography', 'aluminographic', 'aluminotype', 'helminthophobia', 'helminthosporiose', 'helminthosporium', 'helminthosporoid', 'lymhpangiophlebitis', 'limnograph', 'limnophil', 'limnophile', 'limnophilid', 'limnophilidae', 'limnophilous', 'limnophobia', 'limnoplankton', 'lymphadenopathy', 'lymphangioplasty', 'luminophor', 'luminophore']
# rstuv
# ['interdestructive', 'interdestructively', 'interdestructiveness', 'overdestructive', 'overdestructively', 'overdestructiveness', 'overgesticulative', 'overgesticulatively', 'overgesticulativeness', 'overinstructive', 'overinstructively', 'overinstructiveness', 'overstimulative', 'overstimulatively', 'overstimulativeness', 'preinstructive', 'reconstructive', 'reconstructively', 'reconstructiveness', 'redistributive', 'restitutive', 'superstructive', 'unrestitutive']
    #and when i added the end of the alphabet onto the end, the only addition was
# xyzab
# ['oxygenizable']    
    
    characters = "abcdefghijklmnopqrstuvwxyz"
    max_length = 0
    output = []
    for index, _char in enumerate(characters):
        # index = characters.find(char)
        added_string = ""
        for added in characters[index:] + characters[:index]:
            added_string += added
            matches = matches_from_wordslist_and_regex(wordslist, perfect_finder_regex_from_string(added_string))
            # print("added_string: " + added_string)
            # print("matches: " + str(matches))
            if matches:
                if len(added_string) > max_length:
                    max_length = len(added_string)
                    output = [added_string]
                if len(added_string) == max_length:
                    output += [added_string]
            else:
                break
    for word in output:
        print (word)
        print (matches_from_wordslist_and_regex(wordslist, perfect_finder_regex_from_string(word)))
    return output

if __name__ == '__main__':
    main()