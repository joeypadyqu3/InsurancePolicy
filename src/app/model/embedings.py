from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document



def buildEmbeddings():

    embedding_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    )

    docs = []
    
    docs.extend(
            Document(page_content=chunk, metadata={"source": pdf_name})
            for chunk in chunks)
    
    for pdf_name, text in pdf_texts.items():
        chunks = text_splitter.split_text(text)
        for chunk in chunks:
            docs.append(Document(page_content=chunk, metadata={"source": pdf_name}))

    texts = [doc.page_content for doc in docs]
    embeddings = embedding_model.encode(texts)

    ### 2nd AM
    vector_db = FAISS.from_embeddings(
        [(doc.page_content, emb) for doc, emb in zip(docs, embeddings)],
        embedding_model
    )

    vector_db.save_local("insurance_policies_db")

    print("✅ Embeddings generated and stored in FAISS.")