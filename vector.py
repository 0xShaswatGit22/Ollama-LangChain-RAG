from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document   # ← Fixed import
import os
import pandas as pd

# Load the CSV
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Embedding model (tinyllama is perfect for low RAM)
embeddings = OllamaEmbeddings(model="tinyllama")

# Where to save/load the vector database
db_location = "./chroma_langchain_db"

# Check if DB already exists
add_documents = not os.path.exists(db_location)

# Create the vector DB (only first time)
if add_documents:
    documents = []          # ← list of Document objects
    ids = []                # ← list of IDs

    for i, row in df.iterrows():
        # Create a proper Document object
        doc = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]}
        )
        documents.append(doc)
        ids.append(str(i))   # unique ID for each review


        vector_store=Chroma(
            collection_name="restaurant_reviews",
            persist_directory=db_location,
            embedding_function=embeddings
             )
        
        if add_documents:
            vector_store.add_documents(documents=documents,ids=ids)

            retriever=vector_store.as_retriever(
                search_kwargs={"k":5}

            )