from pymongo import MongoClient

uri = "mongodb://testdata1:huy260396@ds249873.mlab.com:49873/c4e23blog"

#1 Connect
client = MongoClient(uri)

#2 Get default database
db = client.get_default_database()

#3 Get collection
posts = db["posts"] #lazy loading
movies = db["movies"]

#4 Create data
new_post = {
    "title": "Hom nay troi dep",
    "content": "Toi o nha code",
}

new_movies = {
    "title": "oscar",
    "rating": 9.0,
}

#5 Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movies)

# 5 Read data
post_list = posts.find()
# p = post_list[1]
for p in post_list:
    print(p["title"])
    print(p["content"])
    print()

#6 Close connection
client.close()