from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
import shutil


class DocumentProcessor:
    def __init__(self, chunk_size=600, chunk_overlap=40):
        self.file_path = r'tempfiles\transcription.pdf'
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.default_persist_directory = r'./chatdb/'

    def load_doc(self):
        # Open the text file in read mode with cp1252 encoding
        loader = PyPDFLoader(self.file_path)
        pages = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap)
        doc_splits = text_splitter.split_documents(pages)
        # print(doc_splits)
        return doc_splits
    
    def create_db(self, splits):
        embedding = HuggingFaceEmbeddings()
        vectordb = Chroma.from_documents(
            documents=splits,
            embedding=embedding,
            persist_directory=self.default_persist_directory

        )
        return vectordb
    
    def process_document(self):
        try:
            doc_splits = self.load_doc()
            updated_vector = self.create_db(doc_splits)
            return updated_vector
        except Exception as e:
            print(e)

# if __name__ == "__main__":
#     # Instantiate the DocumentProcessor class
#     document_processor = DocumentProcessor()
    
#     # Call the process_document method
#     document_processor.process_document()
