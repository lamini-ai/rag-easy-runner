# Lamini RAG - Train an LLM using Lamini and Retrieval Augmented Generation (RAG)

RAG is an AI framework designed to extract factual information from external knowledge bases. It is used to provide large language models (LLMs) with context about your query by retrieving relevant information from your data.

We make it super easy and effective on any open-source model.

```python
from lamini import RetrievalAugmentedRunner

llm = RetrievalAugmentedRunner()
llm.load_data("data/")
llm.train()
```

Here's the response:
```
llm("Who won the case above about dana and wells fargo?")

>> The court ruled in favor of Dana and Linda Phillabaum, the defendants and appellees,
in the foreclosure action brought against them by Wells Fargo.
```

Run it yourself, change the query:
```bash
./example.sh --query "Who won the case above about dana and wells fargo?"
```

Change the model (any open source model, just use the HuggingFace path!)
```python
llm = RetrievalAugmentedRunner(model_name="meta-llama/Llama-2-13b-chat-hf")
```

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
./example.sh --query "Who represented the State of Louisiana in flowers vs rausch case?"
```

# What is Lamini doing under the hood with `RetrievalAugmentedRunner`?

Let's look inside `RetrievalAugmentedRunner`:
1. `llm.load_data` - Loads data using our directory-loader. It loads all the text readable files from the `data` repository and splits them into batches for faster indexing.
2. `llm.train` - Generates embeddings using Lamini and indexes the loaded data using Lamini Index powered by [faiss](https://faiss.ai). 
3. `llm("Who won the flowers vs rausch case?")` - Runs our query engine. Retrieves the top k documents for a given query, appends them to the query and runs inference on the LLM on the new query.

If you are interested in diving deeper into these tools, here's how we implement it in python:

```python
from lamini import DirectoryLoader, LaminiIndex, QueryEngine

loader = DirectoryLoader("data")
index = LaminiIndex(loader)
engine = QueryEngine(index)

response = engine.answer_question("Who won the case above about dana and wells fargo?")

```
This code is in `RAG/rag-deeper.py` script using the following command:

```bash
python RAG/rag-deeper.py
```

Thank you for choosing the Lamini's RAG, a powerful tool to enhance content generation and data retrieval to design a ChatGPT for your data.
