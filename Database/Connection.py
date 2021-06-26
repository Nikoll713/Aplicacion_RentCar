import pymongo

def connection():
    client = pymongo.MongoClient("mongodb+srv://root:123@cluster0.xjtfc.mongodb.net/RentCar?retryWrites=true&w=majority")
    db = client['RentCar']
    return db
