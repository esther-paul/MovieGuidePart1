# [Your Name]
# CIS261
# Movie Guide Part 1


def display_menu():
    """
    Function to display the heading and menu choices
    
    Reference the sample screen shot for exact format
    """
    # TODO: Display "The Movie List program" heading
    # TODO: Display "COMMAND MENU" 
    # TODO: Display menu options: list, add, del, exit with descriptions
    pass


def create_movie_list():
    """
    Function to prepopulate a list with movie titles
    Minimum of three titles must be in the original list
    
    Returns:
        list: List containing initial movie titles
    """
    # TODO: Create and return a list with at least 3 movie titles
    pass


def display_movies(movie_list):
    """
    Function to display all titles in the list
    Use the list as a parameter passed into the function
    
    Args:
        movie_list (list): List of movie titles
    """
    # TODO: Display all movies in the list with numbers
    # Format: "1. Movie Title"
    pass


def add_movie(movie_list):
    """
    Function to add a title to the list
    Use the list as a parameter passed into the function
    
    Args:
        movie_list (list): List of movie titles
    """
    # TODO: Prompt user for movie name
    # TODO: Add movie to the list
    # TODO: Display confirmation message
    # TODO: Display the updated list
    pass


def delete_movie(movie_list):
    """
    Function to delete a title from the list
    Use the list as a parameter passed into the function
    If user enters invalid number, display a message
    
    Args:
        movie_list (list): List of movie titles
    """
    # TODO: Prompt user for movie number to delete
    # TODO: Validate the number (check if it's valid for the list)
    # TODO: If valid, remove movie and display confirmation
    # TODO: If invalid, display error message  
    # TODO: Display the updated list (if deletion was successful)
    pass


def main():
    """
    Main program function
    """
    # TODO: Call display_menu function
    
    # TODO: Call create_movie_list function to get initial list
    # movies = create_movie_list()
    
    # Main program loop
    while True:
        # TODO: Prompt user for command
        # command = input("Command: ").lower()
        
        # TODO: Use if/elif statements to handle each command:
        # - "list": call display_movies function
        # - "add": call add_movie function  
        # - "del": call delete_movie function
        # - "exit": break from loop
        # - invalid command: display error message
        
        pass
    
    # TODO: Display goodbye message


if __name__ == "__main__":
    main()