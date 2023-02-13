import spacy

nlp = spacy.load('en_core_web_md')

# We will store the Hulk description as a control variable. Then we will loop through each line in movies.txt and
# append to movie descriptions list, which we will compare to the control variable later.

control_sentence = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, ' \
                   'the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can ' \
                   'live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and ' \
                   'trained as a gladiator.'
movie_descriptions = []
with open('movies.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        movie_descriptions.append(line)


# We will define the watch next function to take a movie description as an input. We will then loop through each
# description in the movie description list and use the spacy similarity method to compare the two descriptions. We will
# then add each movie to a dictionary, with the description as the key and the similarity as the value. At the end of
# the loop, the key with the highest value will be put forward as the recommendation.

def watch_next(description):
    recommendation = ''
    movie_evaluations = {}
    model_sentence = nlp(description)
    for movie in movie_descriptions:
        similarity = nlp(movie).similarity(model_sentence)
        movie_evaluations[movie] = similarity
    max_similarity = max(movie_evaluations.values())
    for key, value in movie_evaluations.items():
        if value == max_similarity:
            recommendation += str(key)
    final_recommendation = recommendation[:7]
    return final_recommendation


# Call and print watch next function with control sentence as an input.

print(watch_next(control_sentence))
