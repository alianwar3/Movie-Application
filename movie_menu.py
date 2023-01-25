from functions import *


user_options = {
    'a': add_movie,
    'l': display_movies,
    'f': find_movies
}


###### MENU APPLICATION ######
def menu():
    MENU_PROMPT = input("\nSelect 'a' to add movies\nSelect 'l' to see your movies\nSelect 'f' to find movies in your list\nSelect 'q' to quit program\nOption: ")

    while MENU_PROMPT != 'q':

        if MENU_PROMPT in user_options:
            selected_function = user_options[MENU_PROMPT]
            selected_function()

        else:
            print("Unknown command, please try again.")

        MENU_PROMPT = input("\nSelect 'a' to add movies\nSelect 'l' to see your movies\nSelect 'f' to find movies in your list\nSelect 'q' to quit program\nOption: ")

menu() # Call menu function