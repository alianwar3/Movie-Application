from functions import *

###### MENU APPLICATION ######
MENU_PROMPT = input("\nSelect 'a' to add movies\nSelect 'l' to see your movies\nSelect 'f' to find movies in your list\nSelect 'q' to quit program\nOption: ")
while MENU_PROMPT != 'q':

    # If user selects 'a', call the add movies function
    if MENU_PROMPT == 'a':
        add_movie(movie_list)

    # If user selects 'l', display all movies
    elif MENU_PROMPT == 'l':
        display_movies(movie_list)

    # If user selects 'f', find all the movies
    elif MENU_PROMPT == 'f':
        find_movies(movie_list)

    else:
        print("Unknown command, please try again.")

    MENU_PROMPT = input("\nSelect 'a' to add movies\nSelect 'l' to see your movies\nSelect 'f' to find movies in your list\nSelect 'q' to quit program\nOption: ")