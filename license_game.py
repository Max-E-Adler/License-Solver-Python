import os
import re
import itertools
import time

longest_perfects = ['greens', 'ocreae', 'otaria', 'orpins', 'nasial', 'atorai', 'mesial', 'mesial', 'mesail', 'mesail', 'ordeal', 'scotia', 'nasial', 'nosine', 'nudens']

def main():
    words_list = dictionary_filepath_to_wordslist()
    # perfect_regex = perfect_finder_regex_from_string("eae")
    # output_list = matches_from_wordslist_and_regex(words_list, perfect_regex)
    # print(output_list)
    # aaa_zzz_matches_loop(words_list)
    # check_wordlist_for_longest_perfect_actual_word(words_list))
    # print(check_wordlist_for_truncated(words_list))
    # for word in longest_perfects:
    #     print(word)
    #     print(word in words_list)
    #     print(str(matches_from_wordslist_and_regex(words_list, perfect_finder_regex_from_string(word))))
    # consecutive_alphabet_checker(words_list)
    consonant_vowel_ratio(words_list)
    # print(find_swappable_three_letter_strings(words_list))

#finds all permutations of 3 letters without any repetition (aaa, aab, but not aba or baa)
#puts all of those into test_combinations
def find_swappable_three_letter_strings(wordslist):
    # _output is the result of this function, it takes a while to run
    _output = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aag', 'aah', 'aai', 'aak', 'aal', 'aam', 'aan', 'aao', 'aap', 'aar', 'aas', 'aat', 'aau', 'aay', 'acc', 'acd', 'ace', 'aci', 'acl', 'acm', 'aco', 'acp', 'acr', 'acs', 'ade', 'adl', 'adr', 'aee', 'aeh', 'aei', 'ael', 'aem', 'aen', 'aeo', 'aep', 'aer', 'aes', 'aet', 'aeu', 'afi', 'afl', 'agn', 'ahi', 'ahl', 'ahn', 'aho', 'ahr', 'ahu', 'aii', 'ail', 'aim', 'ain', 'aio', 'aip', 'air', 'ais', 'ait', 'aiu', 'aiy', 'all', 'aln', 'alo', 'alr', 'als', 'alt', 'alu', 'amn', 'amr', 'ann', 'ano', 'anp', 'anr', 'ant', 'anu', 'aoo', 'aor', 'aos', 'aot', 'aou', 'aoy', 'apr', 'arr', 'art', 'aru', 'ast', 'asu', 'att', 'atu', 'aty', 'auu', 'auy', 'bee', 'beu', 'bio', 'bno', 'brs', 'cce', 'cci', 'ccp', 'cee', 'cei', 'cel', 'cem', 'cen', 'ceo', 'ces', 'cet', 'ceu', 'cii', 'cil', 'cin', 'cio', 'cit', 'ciu', 'clm', 'cln', 'clo', 'clr', 'clt', 'clu', 'cnn', 'cno', 'cnp', 'cnr', 'cnt', 'cnu', 'coo', 'cop', 'cor', 'cou', 'crr', 'cru', 'ctu', 'dee', 'dei', 'del', 'des', 'det', 'deu', 'dil', 'dio', 'diu', 'dor', 'dsu', 'eee', 'eef', 'eeg', 'eeh', 'eei', 'eek', 'eel', 'eem', 'een', 'eeo', 'eep', 'eer', 'ees', 'eet', 'eeu', 'eey', 'egi', 'egn', 'egu', 'ehi', 'ehl', 'eho', 'ehr', 'ehu', 'eii', 'eil', 'eim', 'ein', 'eio', 'eip', 'eir', 'eis', 'eit', 'eiu', 'eln', 'elo', 'elr', 'els', 'elt', 'elu', 'ely', 'emn', 'emo', 'ems', 'emt', 'emu', 'enn', 'eno', 'enr', 'ens', 'ent', 'enu', 'eoo', 'eor', 'eos', 'eot', 'eou', 'epr', 'ept', 'epu', 'ers', 'eru', 'ery', 'ess', 'est', 'esu', 'ett', 'etu', 'euu', 'ggi', 'gio', 'gir', 'git', 'giu', 'glo', 'gnr', 'gou', 'grt', 'hhi', 'hii', 'hil', 'hin', 'hio', 'hir', 'his', 'hmo', 'hmr', 'hnr', 'hnt', 'hnu', 'hoo', 'hpr', 'hrt', 'hru', 'htt', 'huu', 'iii', 'iil', 'iim', 'iin', 'iio', 'iip', 'iir', 'iis', 'iit', 'iiu', 'iiv', 'iiy', 'iln', 'ilo', 'ilp', 'ilr', 'ils', 'ilt', 'ilu', 'imn', 'imt', 'ino', 'inp', 'inr', 'int', 'inu', 'ioo', 'iop', 'ior', 'ios', 'iot', 'iou', 'ipr', 'ipt', 'irr', 'irs', 'iru', 'iss', 'ist', 'isu', 'itu', 'ity', 'iuu', 'iuy', 'kll', 'lln', 'llt', 'lmr', 'lmt', 'lnn', 'lnp', 'lnr', 'lnt', 'lnu', 'lnz', 'loo', 'lor', 'lot', 'lou', 'lpp', 'lpt', 'lrs', 'lrt', 'ltt', 'ltu', 'luu', 'mnn', 'mnr', 'mnt', 'mnu', 'moo', 'mrr', 'mrs', 'mrt', 'mtt', 'nnn', 'nnp', 'nnr', 'nns', 'nnt', 'nnu', 'nnw', 'noo', 'nor', 'not', 'nou', 'noy', 'npr', 'npu', 'nrr', 'nrt', 'nru', 'nrv', 'nst', 'nuu', 'ooo', 'oop', 'oor', 'oot', 'oou', 'ooy', 'opt', 'orr', 'ors', 'oru', 'ory', 'osu', 'ott', 'oty', 'ouu', 'ppr', 'prr', 'prs', 'prt', 'psu', 'rrs', 'rrt', 'rru', 'rsu', 'rtt', 'rty', 'ruu', 'suu', 'ttt', 'uuu']
    characters = "abcdefghijklmnopqrstuvwxyz"
    output = []
    for subset in itertools.combinations_with_replacement(characters, 3):
        str = ""
        for char in subset:
            str += char
        
        if test_combinations(wordslist, str):
            output.append(str)

    return output

#takes a 3 letter combination of letters and finds all permutations of them
#this is done so that we can test them against each other
def test_combinations(wordslist, input):
    print(input)
    perm_strings = []
    for subset in itertools.permutations(input, 3):
        str = ""
        for char in subset:
            str += char        
        if str in perm_strings:
            continue
        else:
            perm_strings.append(str)
    for word in perm_strings:
        reg = perfect_finder_regex_from_string(word)
        if not match_exists_from_wordslist_and_regex(wordslist, reg):
            return False       
    return True

#calculates the ratio between consonants and vowels of all words in a wordslist    
def consonant_vowel_ratio(wordslist):
    #the results of this function are contained within this "winners" string, i just put it in there to collapse them
    winners = """
    Without Banned List

    Highest
    "shrrinkng",
    "strengths",
    "tsktsking",
    Lowest
    "ouabaio",
    "ukiyoye",

    With Banned List
    Highest is "strengths" but here are some others
    "borschts",
    "schlepps",
    "schmucks",
    "schnapps",
    "schticks",
    "strength",
    "twelfths",
    Lowest
    "adieu",
    "aioli",
    "aquae",
    "audio",
    "aurae",
    "bayou",
    "eerie",
    "gooey",
    "yaboo",
    "yahoo",
    "yowie",
    "ouija",
    "oxeye",
    "payee",
    "queue",

    """
    banned_words = {
        "strengths", #strengths is actually my favorite, best one, but i want to see other goodish ones
        "psychichthys",
        "ouabaio",
        "psychorhythm",
        "aeaean",
        "chrysophyll",
        "aeolia",
        "glycyphyllin",
        "eogaea",
        "rhythmless",
        "ooecia",
        "shrrinkng",
        "aalii",
        "abaue",
        "aecia",
        "aequi",
        "aevia",
        "ailie",
        "aimee",
        "ainee",
        "ainoi",
        "aloyau",
        "anoia",
        "aoife",
        "aotea",
        "aouad",
        "apayao",
        "araua",
        "areae",
        "arioi",
        "aueto",
        "aulae",
        "auloi",
        "aurei",
        "avoue",
        "cooee",
        "heiau",
        "heuau",
        "yautia",
        "iiasa",
        "iliau",
        "kioea",
        "lauia",
        "lieue",
        "looie",
        "louie",
        "miaou",
        "oidia",
        "oorie",
        "oozoa",
        "ouabe",
        "oukia",
        "ourie",
        "ousia",
        "outeye",
        "raiae",
        "tsktsking",
        "taoiya",
        "uaupe",
        "ukiyoe",
        "ukiyoye",
        "umaua",
        "uraei",
        "zoaea",
        "zoeae",
        "gayyou",
        "mayeye",
        "obeyeo",
        "aerie",
        "aguey",
        "aiery",
        "ayous",
        "aliya",
        "boyau",
        "cooey",
        "ediya",
        "eyoty",
        "eyrie",
        "hayey",
        "hooey",
        "hooye",
        "yagua",
        "yameo",
        "yaqui",
        "yaray",
        "yawey",
        "yazoo",
        "yeara",
        "yeuky",
        "ineye",
        "yogee",
        "youre",
        "youse",
        "youve",
        "youze",
        "kieye",
        "layia",
        "looey",
        "louey",
        "mayey",
        "nyaya",
        "noyau",
        "oyana",
        "oriya",
        "peeoy",
        "poyou",
        "royou",
        "sayee",
        "sooey",
        "teaey",
        "uayeb",
        "uneye",
        "upaya",
        "wayao",
        "nachtmml",
        "pschents",
        "schlocks",
        "schmaltz",
        "scrfchar",
        "scrunchs",
        "smrrebrd",
        "sprights",
        "tsktsked"
    }
    highest_ratio_words = [""]
    lowest_ratio_words = [""]
    highest_ratio = 0.0
    lowest_ratio = 1000.0
    for word in wordslist:
        if word in banned_words:
            continue
        cons_vowels = count_consonants_and_vowels(word)
        cons = cons_vowels[0]
        vowels = cons_vowels[1]
        if vowels == 0 or cons == 0:
            continue
        ratio = cons/vowels
        
        if ratio > highest_ratio:
            highest_ratio = ratio
            highest_ratio_words = [word]
        elif ratio == highest_ratio:
            highest_ratio_words += [word]
        elif ratio < lowest_ratio:
            lowest_ratio = ratio
            lowest_ratio_words = [word]
        elif ratio == lowest_ratio:
            lowest_ratio_words += [word]

    print("Highest is \"strengths\" but here are some others")
    for word in highest_ratio_words:
        print(f"\"{word}\",")
    print("Lowest")
    for word in lowest_ratio_words:
        print(f"\"{word}\",")

#counts vowels and consonants and returns them both in an array
def count_consonants_and_vowels(string):
    num_vowels=0
    num_cons=0
    for char in string:
        if char in "aeiouyAEIOUY":
            num_vowels += 1
        else:
            num_cons += 1
    return [num_cons, num_vowels]

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

#incomplete function: will return a grade on a string input by a string against the first may be graded
def grade_substrings(input):
    one_letter_grade = 100


# longest_perfects = ['greens', 'ocreae', 'otaria', 'orpins', 'nasial', 'atorai', 'mesial', 'mesial', 'mesail', 'mesail', 'ordeal', 'scotia', 'nasial', 'nosine', 'nudens'] came from this function
#this function truncates every word in the word list and then checks to see if that truncated word is in the word list
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

#returns matches from the word list, given the word list and a regex
def matches_from_wordslist_and_regex(wordslist, regex):
    output_list = []

    for word in wordslist:
        if re.search(regex, word):
            output_list.append(word)

    return output_list

#this just checks to see if any matches exist, given the word list and a regex
def match_exists_from_wordslist_and_regex(wordslist, regex):
    for word in wordslist:
        if re.search(regex, word):
            return True
    return False    

#creates a regex for "perfect" words (words that bookend the input by 1 character on each side, and separates the individual word by 1 character)
def perfect_finder_regex_from_string(input_string):
    regex = "^."
    for char in input_string:
        regex += char + "."
    regex += "$"
    return regex

#creates a regex for words that checks for words that have the input string within them, but not with all the letters connected to each other, just the same order
def finder_regex_from_string(input_string):
    regex = "^.*"
    for char in input_string:
        regex += char + ".*"
    regex += "$"
    return regex

#takes in a filepath (defaults to where this is on my machine) and outputs a string with all the words in this list
def dictionary_filepath_to_wordslist(dictionary_filepath = "C://Users//MaxAd//Desktop//python//license-solver-python//License-Solver-Python//words_alpha.txt"):
    with open(dictionary_filepath) as f:
        words_list = f.read().splitlines()
    return words_list

#loops through all 3 letter combinations of letters prints the three letter combination that has the most words that it works for (the answer is "eae")  
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

    print("max_length: " + str(max_length))
    print("longest_string: " + longest_string)
    print("output: " + str(output))


#checks all possible consecutive strings, looping around once when the end of the alphabet is reached
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

#required
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
