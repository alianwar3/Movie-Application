movie_list = [] # All movies will be stored inside movie_list


##### FUNCTIONS #####
# add_movie() is responsible for appending movie to movie_list
def add_movie(movie_list):
    movie = input("Enter the name of the movie you would like to add: ")
    movie_list.append(movie)
    return movie_list


# display_movies() is responsible for showing all movies in movie_list
def display_movies(movie_list):
    for movie in movie_list:
        print(movie)


# find_movies() is responsible for finding a movie in movie_list
def find_movies(movie_list):
    movie_name = input("Enter the name of the movie you'd like to search for: ")

    if movie_name in movie_list:
        print(f"{movie_name} is in our store")

    else:
        print("That movie is not in our store")