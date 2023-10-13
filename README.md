# Lamini RAG - Train an LLM using Lamini and Retrieval Augmented Generation (RAG)

RAG is an AI framework designed to extract factual information from external knowledge bases. It is used to provide large language models (LLMs) with context about your query by retrieving relevant information from your data.

## Overview

RAG, short for "Retrieval Augmented Generation," is designed to seamlessly integrate data retrieval and content generation. It operates in three key components:

1. Indexer: The indexer component is responsible for indexing a user's data, making it easily accessible for the LLM pipeline.
2. Retriever: The retriever module fetches pertinent information from the indexed user data in response to user queries.
3. Generator: The generator then leverages the retrieved information to produce contextually relevant and coherent text, enriching the content generation process.

## Lamini Integration

This implementation makes use of the Lamini framework, which streamlines the integration of the RAG system into your AI projects. Lamini simplifies setup, training, and deployment of AI models, including RAG.


# Getting Started
1. Install Lamini
```bash
pip install lamini
```

2. Clone the repository
```bash
git clone git@github.com:lamini-ai/RAG.git
```

3. cd into the repository
```bash
cd RAG
```
4. Add your data in the data folder. A sample data has been added for you.

5. Run an example on a question you want to ask about your data

```bash
./example.sh --query "Who won the case above?"
```

# Answer questions using a Lamini and RAG

## Python

```python
from lamini import RetrievalAugmentedRunner

llm = RetrievalAugmentedRunner(
    model_name = "meta-llama/Llama-2-13b-chat-hf",
)
llm.load_data("data")
llm.train()
response = llm("Who won the case above about dana and wells fargo?")

```

Rag-Model Response:
```
The court ruled in favor of Dana and Linda Phillabaum, the defendants and appellees,
in the foreclosure action brought against them by Wells Fargo.
```

This code is also preset in `rag.py`. You can run it using 
```bash
python rag.py
```

# Use command line tools

To ask a new question to the RAG-backed LLM, you can run the following command:

```bash
./example.sh --query "Who won the case above?"
```

Thank you for choosing the Lamini's RAG, a powerful tool to enhance content generation and data retrieval to design a ChatGPT for your data.
