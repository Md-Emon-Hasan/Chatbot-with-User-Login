from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# Dictionary to store memory for each user
user_memories = {}

def get_user_memory(username):
    if username not in user_memories:
        user_memories[username] = ConversationBufferMemory(
            memory_key="history",  # ✅ FIXED from 'chat_history' to 'history'
            return_messages=True
        )
    return user_memories[username]

def ask_gemini(user_input, memory):
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    return conversation.run(user_input)
