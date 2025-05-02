import os

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata


class ChatPdf:
    vector_store = None
    retriever = None
    chain = None

    def __init__(self):
        self.model = ChatOllama(model="assistant:latest")
        print("Loading embedding")
        self.embedding = FastEmbedEmbeddings()
        print("Done")

        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
        self.prompt = PromptTemplate.from_template(
            """
            <s> [INST] You are an assistant for question-answering tasks. Use the following pieces of retrieved context
            to answer the question. If you don't know the answer, just say that you don't know. Use three sentences
             maximum and keep the answer concise. [/INST] </s>
            [INST] Question: {input}
            Context: {context}
            Answer: [/INST]
            """
        )

    def ingest(self, pdf_path, chroma_path):
        print("Loading PDF")
        docs = PyPDFLoader(pdf_path).load()
        chunks = self.text_splitter.split_documents(docs)
        print("Done.")

        print("Creating vector store")
        vector_store = Chroma.from_documents(documents=chunks, embedding=self.embedding, persist_directory=chroma_path)
        print("Done.")

    def load(self, path):
        print("Loading vector store")
        vector_store = Chroma(persist_directory=path, embedding_function=self.embedding)
        print("Done.")

        print("Creating chain")
        self.retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5,
            },
        )

        document_chain = create_stuff_documents_chain(self.model, self.prompt)
        self.chain = create_retrieval_chain(self.retriever, document_chain)

        print("Done.")

    def ask(self, query: str):
        if not self.chain:
            self.load()

        result = self.chain.invoke({"input": query})

        print(result["answer"])
        for doc in result["context"]:
            print("Source: ", doc.metadata["source"], doc.metadata["page"])


def main(pdf_path):
    name = os.path.basename(pdf_path).split(".")[0]
    chroma_path = f"/Users/wesflo/tmp/chroma_{name}"

    app = ChatPdf()
    if not os.path.isdir(chroma_path):
        app.ingest(pdf_path, chroma_path)

    app.load(chroma_path)

    while True:
        query = input(">>> ")

        if len(query) == 0:
            continue

        if query == "/exit":
            break

        app.ask(query)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Chat with given pdf document", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("pdf_path")

    args = vars(parser.parse_args())
    main(**args)
