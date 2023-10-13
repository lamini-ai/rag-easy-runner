from lamini import RetrievalAugmentedRunner

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, help="Query to run", default="Who  were the attorneys representing the state of luisiana?")
    args = parser.parse_args()

    llm = RetrievalAugmentedRunner(
        model_name = "meta-llama/Llama-2-13b-chat-hf",
    )
    llm.load_data("data")
    llm.train()
    response = llm(args.query)
    
    print("\nQuery: ", args.query)
    print("\nResponse: ", response)

main()