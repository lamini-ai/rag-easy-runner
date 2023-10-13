# RAG - Train an LLM using Lamini and Retrieval Augmented Generation (RAG)


# Pre-requisites

```bash
pip install lamini
```

```bash
git clone git@github.com:lamini-ai/RAG.git
```

```bash
cd RAG
```

# Answer questions using a Lamini Index and RAG

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
