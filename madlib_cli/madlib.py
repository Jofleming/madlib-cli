import re

with open("assets/dark_and_stormy_template.txt","w") as dark_stormy:
    dark_stormy.write("It was a {Adjective} and {Adjective} {Noun}.")

def welcome_text():
    print("""
    Welcome to Jordan's MADlibs game!
    To play please type: start
    You will recieve a list of types of words.
    Please input a corresponding type of word.
    ex. If asked for an adjective: 
    input gloomy
    To stop input enter: quit
    """)

def madlib():
    welcome_text()
    player_input = input("> ")
    if player_input.lower() == "start":
        player_quit = False
    while not player_quit:
        if player_input.lower() == "quit":
            player_quit = True
        else:
            line_template = read_template("assets/dark_and_stormy_template.txt")
            decon_line_template = parse_template(line_template)
            list_of_words = list(decon_line_template[1])
            player_response_tuple = ask_for_words(list_of_words, player_quit)
            finished_madlib = merge(decon_line_template[0], player_response_tuple)
            write_it_down(finished_madlib)
            print(finished_madlib)
            player_quit = True
    print("Thanks for playing!")

def write_it_down(finished_madlib):
    split_madlib = finished_madlib.split("\n")
    polished_madlib = split_madlib[1][2:].replace(" ","_")
    with open(f"assets/{polished_madlib}.txt","w") as new_file:
        new_file.write(finished_madlib)

def ask_for_words(list_of_word_types, player_quit):
    player_input_words = []
    for word in list_of_word_types:
        response_from_input = input(f"{word} : ")
        if response_from_input.lower() == "quit":
            player_quit = True
            return player_quit
        player_input_words.append(response_from_input)
    return tuple(player_input_words)

def read_template(file_path):
    with open(file_path,"r") as line_template:
        return line_template.read()

dark_stormy = read_template("assets/dark_and_stormy_template.txt")

def parse_template(line_template):
    pattern = r"\{(\w+\s*\w+\s*\w+\s*\w+)\}"
    actual_stripped = re.sub(pattern,"{}", line_template)
    actual_parts = tuple(re.findall(pattern, line_template))
    return (actual_stripped, actual_parts)

def merge(stripped_line, user_words):
    new_string = stripped_line.format(*user_words)
    return new_string

madlib()
