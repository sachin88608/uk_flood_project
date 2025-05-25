# Project overview, instructions, etc.

To install any library in the virtual env uk_flood - USE CMD (C:\Users\gupta.sachin\OneDrive - HIPPOSTORES TECHNOLOGY PRIVATE LIMITED\Documents\uk_flood_project\uk_flood\Scripts>activate.bat)
After this do - pip freeze > requirements.txt - to save the requirements in the requirements.txt file as well.
To check the data present in the qdrant : >python src/view_qdrant_data.py

**Step 1-----**

First Part includes files:
1. api_client.py
2. preprocessing.py
3. vector_store.py
4. "Pipeline completed successfully!"

STEPS for part 1 - **Pull the data from an API and store in the Qdrant via Docker**
1. Run the docker desktop 
2. Run this command on the cmd : docker run -d -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant
3. Run python main.py

Scheduling is left as of now :----------------- 

These are enhancements, not blockers:- **Will do it after 2nd part**
1. Automate fetch every 30 minutes: Use a cron job, APScheduler, or Dockerized scheduler.
2. Avoid duplicate inserts: You may want to deduplicate based on id or timeRaised.
3. Handle Qdrant updates: If a flood alert already exists, update its vector if message content changes.
4. Use logging instead of print.

**Step 2-----**

Next, you can move on to Task 2, which is about:

1. Taking user queries from the UI,
2. Embedding the query,
3. Searching Qdrant for the closest flood data,
4. Sending that to an LLM for a generated answer,
5. Returning the answer to the UI.
