import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

ping = r.ping()
print("Connected to Redis!" if ping else "Connection failed.")

def count_actors_with_lastname_p(r):
    count = 0
    for key in r.scan_iter("actor:*"):
        last_name = r.hget(key, "last_name")
        if last_name and last_name.startswith("P"):
            count += 1
    return count

print("Actors with last name starting with 'P':", count_actors_with_lastname_p(r))

def movies_after_2010_with_votes(r, min_votes=100000):
    results = []
    for key in r.scan_iter("movie:*"):
        release_year = r.hget(key, "release_year")
        votes = r.hget(key, "votes")
        if release_year and votes:
            try:
                if int(release_year) > 2010 and int(votes) > min_votes:
                    title = r.hget(key, "title")
                    results.append((title, release_year, votes))
            except ValueError:
                continue
    return results

movies = movies_after_2010_with_votes(r)
for m in movies:
    print(f"{m[0]} ({m[1]}) - {m[2]} votes")


def create_top_movies_by_genre(r):
    best_movies = {}

    for key in r.scan_iter("movie:*"):
        genre = r.hget(key, "genre")
        rating = r.hget(key, "rating")
        title = r.hget(key, "title")
        if genre and rating and title:
            try:
                rating = float(rating)
                if genre not in best_movies or rating > best_movies[genre][1]:
                    best_movies[genre] = (title, rating)
            except ValueError:
                continue

    # Store to Redis
    for genre, (title, rating) in best_movies.items():
        hash_key = f"top_movies_by_genre:{genre}"
        r.hset(hash_key, mapping={"title": title, "rating": rating})

create_top_movies_by_genre(r)

print("Top Action Movie:", r.hgetall("top_movies_by_genre:Action"))

