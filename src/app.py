import warnings

warnings.filterwarnings('ignore')

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOllama(model='llama3.2', temperature=0)
chroma_local = Chroma(persist_directory="./database", embedding_function=HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2'))
    

def prompt(texto):
    system_prompt = (
    texto+
    "\n\n"
    "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ])
    return prompt


def respuesta(pregunta, llm, chroma_db, prompt):
    retriever = chroma_db.as_retriever()

    chain = create_stuff_documents_chain(llm, prompt)
    rag = create_retrieval_chain(retriever, chain)
    
    results = rag.invoke({"input": pregunta})
    return results



texto = """Eres un asistente legal experto en responder preguntas de legalidad. "
    "Usa los siguientes fragmentos de contexto recuperado para proporcionar respuestas precisas, "
    "fundamentadas en principios legales, normativas aplicables o jurisprudencia relevante. "
    "Si no sabes la respuesta, indica que no puedes ofrecer una respuesta definitiva. "
    "Sé claro, directo y profesional, utilizando un máximo de tres oraciones."""
    
    

if __name__ == '__main__':
    #print(f"🤖: {respuesta(input('🤔 Ingresa tu pregunta... '), llm, chroma_local, prompt(texto))['answer']}")
    print(respuesta(input('Ingresa tu pregunta... '), llm, chroma_local, prompt(texto))['answer'])
