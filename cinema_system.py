## The cinema system


movies = {
    "batman" : 15.49,
    "avatar" : 12.29,
    "spiderman" : 13.00
}

spiderman_movie = movies["spiderman"]
print(f"Price of Spiderman movie: {spiderman_movie}")


movies["terrifier"] = 33.49

movies["spiderman"] = 19.99

print(movies)


random_movie = input("Which movie are you searching?: ").lower()

if random_movie in movies:
    movie = movies[random_movie]
    print(movie)
else:
    print(f"Sorry, {random_movie} is not in stock!")
