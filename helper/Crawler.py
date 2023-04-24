from bs4 import BeautifulSoup
import pandas as pd
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Crawler:
    #define the keys
    titlejobs = []
    linkJobs = []
    jobTypes = []
    proposals = []
    skills = []
    budgets = []

    def runCrawler(self,pageSource):
        soup = BeautifulSoup(pageSource, 'lxml')
        jobs = soup.findAll('section', {'data-test': 'JobTile'})
        for job in jobs:
            self.titlejobs.append(job.find("h3", {'class': 'job-tile-title'}).find('a').text)
            self.linkJobs.append('https://www.upwork.com' + job.find("h3", {'class': 'job-tile-title'}).find('a').get('href'))
            jobType = job.find('strong', {'data-test': 'job-type'}).text

            self.proposals.append(job.find('strong', {'data-test': 'proposals'}).text)
            skillset = [skill.text for skill in job.findAll('a', {'data-test': 'attr-item'})]
            if (jobType == 'Fixed-price'):
                self.jobTypes.append(jobType)
                self.budgets.append(job.find('span', {'data-test': 'budget'}).text)
            elif (jobType == 'Hourly'):
                self.jobTypes.append(jobType)
                self.budgets.append("unknown")
            else:
                self.jobTypes.append(jobType.split(": ")[0])
                self.budgets.append(jobType.split(": ")[1])

            self.skills.append(skillset)


    def storeToDataFrame(self):
        df_upwork = pd.DataFrame({'title': self.titlejobs, 'linkJobs': self.linkJobs, 'jobType': self.jobTypes, 'proposals': self.proposals, 'skillset': self.skills,
            'budget': self.budgets})
        print(df_upwork)
        df_csv = df_upwork.to_csv('jobupwork.csv', index=True)
        return df_csv
    
    def storeToMonggoDb(self):
        uri = "mongodb+srv://mongooGbikk:s3m3nt4r4#@cluster0.6vvfy.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            db = client["upworkjobs"]

            collection = db["jobs"]
            unique_fields = ["linkJobs"]

            df = pd.DataFrame({'title': self.titlejobs, 'linkJobs': self.linkJobs, 'jobType': self.jobTypes, 'proposals': self.proposals, 'skillset': self.skills,
                'budget': self.budgets})
            print(df)

    # Loop over new data and update or insert documents in MongoDB
            for index, row in df.iterrows():
                # Query MongoDB for existing document with same unique identifier
                query = {field: row[field] for field in unique_fields}
                existing_doc = collection.find_one(query)
        
                if existing_doc:
            # If document already exists, update it with new data
                    update = {"$set": {field: row[field] for field in row.index}}
                    collection.update_one(query, update)
                else:
            # If document does not exist, insert new document into MongoDB
                    new_doc = {field: row[field] for field in row.index}
                    collection.insert_one(new_doc)
                    print("new one")
                    print("index = " , index,"row = ",row)

        except Exception as e:
            print(e)
       
          




        





