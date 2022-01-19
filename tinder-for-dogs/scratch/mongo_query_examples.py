from pprint import pprint
import pymongo

# Examples of queries once you docker-compose up.


class MongoDB_Example:
    def __init__(self):
        """Collection in ["dogs", "users"]."""
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["metadata"]

    def query(self, collection, q):
        return self.db[collection].find(q)


if __name__ == "__main__":
    db = MongoDB_Example()

    ## FOR ALL OF THESE, you can use "users" instead of "dogs"
    ## to get the associated test user data in the func at the bottom.
    ## Note neither one of these colls is in a final form.  This is
    ## only an example to iterate off of.

    # Get all dogs.
    q = {}

    # Get dogs who have Apartment_Friendly >= 3
    q = {"Apartment_Friendly": {"$gte": 3}}

    # Get dogs who have Apartment_Friendly >= 3 AND Cat_Friendly < 3
    q = {"Apartment_Friendly": {"$gte": 3}, "Cat_Friendly": {"$lt": 3}}

    # Get dogs who have (Apartment_Friendly >= 3 AND Cat_Friendly < 3) OR
    # Barking_Tendencies = 1
    q = {
        "$or": [
            {"Apartment_Friendly": {"$gte": 3}, "Cat_Friendly": {"$lt": 3}},
            {"Barking_Tendencies": 1},
        ]
    }

    # print a bit of the above responses.
    resp = db.query("dogs", q=q)
    pprint([i for i in resp][:3])
