from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS
from main import TriggerCrawling

app=Flask(__name__)
cors =CORS(app)
@app.route('/api/jobs', methods = ['GET','POST'])

def get_jobs():
    uri = "mongodb+srv://mongooGbikk:s3m3nt4r4#@cluster0.6vvfy.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["upworkjobs"]
    collection = db["jobs"]
    jobs = collection.find()
    job_list = []
    for job in jobs:
        job_list.append({
            'title': job['title'],
            'proposals': job['proposals'],
            'jobType': job['jobType'],
            'budget': job['budget'],
            'linkJobs': job['linkJobs'],
            'skillset':job['skillset']
        })

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return jsonify(job_list)
    except Exception as e:
        print(e)

@app.route('/api/trigger/<int:isTrigger>',methods=['POST'])
def Crawling(isTrigger):

    return isTrigger
if __name__ == '__main__':
    app.run(debug=True)
