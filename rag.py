from lamini import RetrievalAugmentedRunner

llm = RetrievalAugmentedRunner(
    model_name = "meta-llama/Llama-2-13b-chat-hf",
)

llm.load_data("data")
llm.train()
response = llm("Who won the case above about dana and wells fargo?")
print("\nResponse: ", response)

# Interactive LLM
while True:
    user_input = input("\nEnter a question: ")
    response = llm(user_input)
    print("\nResponse: ", response)