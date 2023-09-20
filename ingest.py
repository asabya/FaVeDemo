import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader, PDFMinerLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import LlamaCppEmbeddings
from fave_client import FaVeClient
load_dotenv()

def main():
    llama_embeddings_model = os.environ.get('LLAMA_EMBEDDINGS_MODEL')
    model_n_ctx = os.environ.get('MODEL_N_CTX')
    # Load document and split in chunks
    for root, dirs, files in os.walk("source_documents"):
        for file in files:
            if file.endswith(".txt"):
                loader = TextLoader(os.path.join(root, file), encoding="utf8")
            elif file.endswith(".pdf"):
                loader = PDFMinerLoader(os.path.join(root, file))
            elif file.endswith(".csv"):
                loader = CSVLoader(os.path.join(root, file))
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    llama = LlamaCppEmbeddings(model_path=llama_embeddings_model, n_ctx=model_n_ctx)
    db = FaVeClient("state_three", "text", "http://localhost:1234", llama)
    try:
        db.add_documents(texts)
    except Exception as e:
        raise Exception("%s\n" % e)
    
    db = None

if __name__ == "__main__":
    main()
