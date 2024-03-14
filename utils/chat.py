from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory

class Chatbot:
    def __init__(self,vector_db,llm_model="mistralai/Mistral-7B-Instruct-v0.1", temperature=0.7, max_tokens=1024, top_k_samples=3):
        self.llm_model = llm_model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_k_samples = top_k_samples
        self.vector_db = vector_db

    def initialize_llmchain(self, vector_db):
        llm = HuggingFaceHub(
            repo_id=self.llm_model,
            model_kwargs={"temperature": self.temperature, "max_new_tokens": self.max_tokens,
                          "top_k": self.top_k_samples}
        )
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            output_key='answer',
            return_messages=True
        )
        retriever = vector_db.as_retriever()

        qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=retriever,
            chain_type="stuff",
            memory=memory,
            return_source_documents=True,
        )
        return qa_chain

    def format_chat_history(self, message, chat_history):
        formatted_chat_history = []
        for user_message, bot_message in chat_history:
            formatted_chat_history.append(f"User: {user_message}")
            formatted_chat_history.append(f"Assistant: {bot_message}")
        return formatted_chat_history

    def get_response(self, qa_chain, message, formatted_chat_history):
        response = qa_chain({"question": message, "chat_history": formatted_chat_history})
        response_answer = response["answer"]
        return response_answer

    def chat(self,message):
        try:

            qa_chain = self.initialize_llmchain(self.vector_db)
            history = []
            formatted_chat_history = self.format_chat_history(message, history)
            response_answer= self.get_response(qa_chain, message,formatted_chat_history)
            new_history = history + [(message, response_answer)]

            return response_answer

        except Exception as e:
            print(e)
