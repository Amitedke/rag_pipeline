from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

app = FastAPI(
    title="LangServe",
    description="A simeple api server",
    version="1.0.0",
)
model = ChatOpenAI()
llm = Ollama(model="llama2")

add_routes(
            app,
           ChatOpenAI(),
           path="/openai")


promt1 = ChatPromptTemplate.from_template("write a essay about {topic} in 100 words")
promt2 = ChatPromptTemplate.from_template("write a poem about {topic} in 100 words")


add_routes(
    app,
    promt1|model,
    path="/essay")


add_routes(
    app,
    promt1|llm,
    path="/poem")



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
