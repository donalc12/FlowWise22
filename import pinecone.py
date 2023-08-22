import pinecone      

pinecone.init(      
	api_key='82f6a76f-1b47-4699-bb2b-4c9f0d4c0eaa',      
	environment='us-west4-gcp-free'      
)      
index = pinecone.Index('indexfm')