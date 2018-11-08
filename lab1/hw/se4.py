from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# Connect
client = MongoClient(uri)

# Get default database
db = client.get_database()

# Get collection
customers = db["customers"]

# Count
count_events = 0
count_ads = 0
count_wom = 0
customers = customers.find()
for cus in customers:
    if cus["ref"] == "events":
        count_events += 1
    elif cus["ref"] == "ads":
        count_ads += 1
    elif cus["ref"] == "wom":
        count_wom += 1
print("events:", count_events, "ads:", count_ads, "wom:", count_wom) 

# pyplot.pie(count, labels = ref, autopct="%.2f%%")
# pyplot.axis("equal")
# pyplot.title("Customers' references: ")
# pyplot.show()

# Close connection
client.close()