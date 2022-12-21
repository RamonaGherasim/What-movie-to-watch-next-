# T38: Compulsory Task 2

# Import spacy module and load the medium english language module
import spacy
nlp = spacy.load("en_core_web_md")

# Open and read all the lines from the "movies.txt" file then close it.
file = open("movies.txt", "r")
movies_list = file.readlines()
file.close()


def find_similar_movie(description_param):
    """
    This function takes in a description as a parameter and converts it to an
    object using the nlp() method. Finds the most similar movie from the
    movies list using the .similarity() method of NLP and returns that movies
    title in a string message.

    :param description_param: list
    :return: string
    """
    nlp_description = nlp(description_param)

    # Initialise an empty list that will hold the movies similarity results
    similarity_results = []
    for movie in movies_list:
        # For each movie in the list
        # Find the title and the description of that movie by using .split()
        # Convert the movie description into an object using the nlp() method
        # Find the similarity number between that movie's description and the
        # description received as parameter
        # Append the similarity number to the list above
        title, movie_description = movie.split(":")
        similarity = nlp(movie_description).similarity(nlp_description)
        similarity_results.append(similarity)

    # Find the highest similarity/highest number in the list
    # The most similar movie will be the one at the same index as the max_score
    # index in the similarity_results list
    # The title of that movie is comprised of the first 7 characters
    max_score = max(similarity_results)
    most_similar_movie = movies_list[similarity_results.index(max_score)]
    most_similar_movie_title = most_similar_movie[:7]

    # return a string message that includes the desired movies' title
    return f"You should watch {most_similar_movie_title} next."


# Defining the description variable as a string
description = "Will he save their world or destroy it? When the Hulk becomes "\
              "too dangerous for the Earth, the Illuminati trick Hulk into a "\
              "shuttle and launch him into space to a planet where the Hulk " \
              "can live in peace. Unfortunately, Hulk land on the planet " \
              "Sakaar where he is sold into slavery and trained as a " \
              "gladiator. "

# Print the return of find_similar_movies() function that has the description
# sent as argument
print(find_similar_movie(description))
