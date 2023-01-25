movie_list = [] # All movies will be stored inside movie_list


##### FUNCTIONS #####
# add_movie() is responsible for appending movie to movie_list
def add_movie():
    print('-------------------------------------------')
    title = input("Enter the name of the title: ")
    director = input("Enter the name of the director: ")
    year = input("Enter the name of the release year: ")

    # Check if year is numeric
    while year.isnumeric() == False:
        print('\nThe year you entered is not numeric.')
        year = input("Enter the name of the release year: ")

    print('-------------------------------------------')


    movie_list.append({
        'title': title,
        'director': director,
        'year': year
    })

    return movie_list


# display_movies() is responsible for showing all movies in movie_list
def display_movies():
    for movie in movie_list:
        print('----------------------------')
        print(f"Title   : {movie['title']}")
        print(f"Director: {movie['director']}")
        print(f"Year    : {movie['year']}")
        print('----------------------------')


# find_movies() is responsible for finding a movie in movie_list
def find_movies():
    movie_name = input("Enter the name of the movie you'd like to search for: ")

    for movie in movie_list:

        # Check if searched movie is inside movie directionary
        if movie_name in movie['title']:
            print('---------------------------------------')
            print(f"{movie_name} exists in movie catalogue")
            print('---------------------------------------')