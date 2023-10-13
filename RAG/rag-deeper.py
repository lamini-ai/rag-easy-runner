from lamini import DirectoryLoader, LaminiIndex, QueryEngine

loader = DirectoryLoader("data")
index = LaminiIndex(loader)
engine = QueryEngine(index)

response = engine.answer_question("Who won the case above about dana and wells fargo?")
print("\nResponse: ", response)