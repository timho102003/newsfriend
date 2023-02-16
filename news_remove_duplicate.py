import yaml

from database import ArticleCollection

db_cfg = yaml.safe_load(open("./database/db_cfg.yaml"))

news_api_db = ArticleCollection(
    ip_address=db_cfg["mongodb"]["ip_address"],
    database_name=db_cfg["mongodb"]["database_name"],
    collection_name=db_cfg["mongodb"]["news_collection_name"],
)

# Define the pipeline to group by title and isDuplicate
pipeline = [
    {"$match": {"isDuplicate": True}},
    {
        "$group": {
            "_id": {"title": "$title", "isDuplicate": "$isDuplicate"},
            "docs": {"$push": "$$ROOT"},
        }
    },
]

# Execute the pipeline and select the first document in each group
for group in news_api_db.collection.aggregate(pipeline):
    keep_doc = group["docs"][0]
    # Delete all other documents in the group
    for doc in group["docs"][1:]:
        news_api_db.collection.delete_one({"_id": doc["_id"]})
    # Set isDuplicate to false on the remaining document
    news_api_db.collection.update_one(
        {"_id": keep_doc["_id"]}, {"$set": {"isDuplicate": False}}
    )
