import requests
import json
import sys

if len(sys.argv) > 1:
    namee = " ".join(sys.argv[1:])
else:
    print("Zəhmət olmasa film adı qeyd et.")
    exit()

url = f"https://www.omdbapi.com/?apikey=a12a5664&t={namee}"
response = requests.get(url)

if response.status_code != 200:
    print("""
This film is not found.

-----------------------
Request is failed.

    """)
    exit()

movie_data = json.loads(response.text)

if movie_data["Response"] == "False":
    print("""
------------------
This film is not found.
------------------
    """)
    exit()

title = movie_data["Title"]
year = movie_data["Year"]
Released = movie_data["Released"]
Genre = movie_data["Genre"]
director = movie_data["Director"]
actors = movie_data["Actors"]
Country = movie_data["Country"]
imdbRating = movie_data["imdbRating"]

print(f"\n----------------------")
print(f"Title: {title}")
print(f"Year: {year}")
print(f"Released: {Released}")
print(f"Genre: {Genre}")
print(f"Director: {director}")
print(f"Actors: {actors}")
print(f"Country: {Country}")
print(f"IMDB: {imdbRating}")
print("""
----------------------
Request is seccessful.
----------------------
""")
