from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# Connect
client = MongoClient(uri)

# Get default database
db = client.get_default_database()

# Get collection
posts = db["posts"]

# Create new posts
new_post1 = {
    "title": "Minimising cost",
    "author": "Me",
    "content": "I knew I couldnt make it in time. So in the last hours I went out and played poker. Now, at least, I can afford another course, and a drink."
}


# Insert new data
posts.insert_one(new_post1)

# # Read data
# post_list = posts.find()
# for p in post_list:
#     if (p["title"]) == "Minimising cost":
#         print(p["content"])
#         print("-----------------------")
 
# Close connection
client.close()