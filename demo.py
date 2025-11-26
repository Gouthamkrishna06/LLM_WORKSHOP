from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3:8b")
question = input("What's your Question?")
if question:
    response = llm.invoke(question)
    print(response)