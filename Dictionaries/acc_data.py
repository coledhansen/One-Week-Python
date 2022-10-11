movie = {
    "title": "Amadeus",
    "imdb_score": 8.3
}

print(movie["title"]) # Amadeus
print(movie["imdb_score"]) # 8.3

# print(movie[1]) # error!

movie["imdb_score"] += 0.5
print(movie)

movie["rating"] = "r"
print(movie) # add pair rating and set equal to r

movie['is_great'] = True
print(movie)

# keys HAVE TO be unique
# single title, rating, etc.
# values can all be the same

second_movie = {
    'title': 'I, Tonya'
}
print(second_movie)
