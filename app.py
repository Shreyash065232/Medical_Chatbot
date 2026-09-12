from flask import Flask, render_template, jsonify, request, session
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)
app.secret_key = "medical-chatbot-secret-key"

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

if not PINECONE_API_KEY or not GROQ_API_KEY:
    raise RuntimeError(
        "Missing PINECONE_API_KEY or GROQ_API_KEY. "
        "Create a .env file in the project root with both values set."
    )

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot" 
# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)




retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

chatModel = ChatGroq(model="openai/gpt-oss-120b", temperature=0.4)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]

    if "history" not in session:
        session["history"] = []

    history = session["history"]

    response = rag_chain.invoke({
        "input": msg
    })

    answer = response["answer"]

    history.append({
        "user": msg,
        "bot": answer
    })

    session["history"] = history

    print("User:", msg)
    print("Bot:", answer)

    return str(answer)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)