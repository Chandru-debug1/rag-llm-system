from langchain_community.document_loaders import TextLoader

def load_documents(path="data/raw"):
    docs = []
    import os
    
    for file in os.listdir(path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(path, file))
            docs.extend(loader.load())
    
    return docs