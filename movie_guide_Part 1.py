#Esther Paul
#CIS261
#Movie Guide Part1

def display_menu():
    """
    Function to display the heading and menu choices
    """
    print("The Movie List program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit Program\n")


def create_movie_list():
    """
    Function to prepopulate a list with movie titles
    """
    return ["Squid Game", "Super Man", "Spider Man"]


def display_movies(movie_list):
    """
    Display all movies in the list with numbering
    """
    if not movie_list:
        print("No movies in the list.\n")
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie}")
        print(end='\n')  


def add_movie(movie_list):
    """
    Add a new movie to the list
    """
    name = input("Name: ").strip()
    if name:
        movie_list.append(name)
        print(f'"{name}" was added.\n')
        display_movies(movie_list)
    else:
        print("Movie name cannot be empty.\n")


def delete_movie(movie_list):
    """
    Delete a movie by its number
    """
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movie_list):
            removed = movie_list.pop(number - 1)
            print(f'"{removed}" was deleted.\n')
            display_movies(movie_list)
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def main():
    """
    Main program loop
    """
    display_menu()
    movies = create_movie_list()

    while True:
        command = input("Command: ").strip().lower()

        if command == "list":
            display_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
