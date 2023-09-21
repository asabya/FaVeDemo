# FaVeDemo

## Introduction

FaVeDemo is a Python-based demo project designed to showcase the capabilities of the FaVe API. This repository contains various scripts that interact with FaVe, including data ingestion and GPT-related functionalities.

This is a Demo for [FaVe](https://github.com/fairDataSociety/FaVe) intigrating with langchain.
Ask questions to your documents. 100% private. You can ingest documents and ask questions.

Built with [LangChain](https://github.com/hwchase17/langchain) and [GPT4All](https://github.com/nomic-ai/gpt4all) and [LlamaCpp](https://github.com/ggerganov/llama.cpp)

<img width="902" alt="demo" src="https://user-images.githubusercontent.com/721666/236942256-985801c9-25b9-48ef-80be-3acbb4575164.png">


## Features

- FaVe API client for easy interaction
- Data ingestion script
- GPT-related functionalities
- Example environment configuration

## Prerequisites

- Python 3.x
- See `requirements.txt` for required Python packages

# Environment Setup

In order to set your environment up to run the code here, first install all requirements:
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/asabya/FaVeDemo.git
cd FaVeDemo
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Models
Then, download the 2 models and place them in a directory of your choice.
- LLM: default to [ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin). If you prefer a different GPT4All-J compatible model, just download it and reference it in your `.env` file.
- Embedding: default to [ggml-model-q4_0.bin](https://huggingface.co/Pi3141/alpaca-native-7B-ggml/resolve/397e872bf4c83f4c642317a5bf65ce84a105786e/ggml-model-q4_0.bin). If you prefer a different compatible Embeddings model, just download it and reference it in your `.env` file.

## Configurae environment variables
Copy `example.env` to `.env` and fill in the required configuration variables.

```
MODEL_TYPE: supports LlamaCpp or GPT4All
LLAMA_EMBEDDINGS_MODEL: (absolute) Path to your LlamaCpp supported embeddings model
MODEL_PATH: Path to your GPT4All or LlamaCpp supported LLM
MODEL_N_CTX: Maximum token limit for both embeddings and LLM models
```

Note: because of the way `langchain` loads the `LLAMMA` embeddings, you need to specify the absolute path of your embeddings model binary. This means it will not work if you use a home directory shortcut (eg. `~/` or `$HOME/`).

## Test dataset
This repo uses a [state of the union transcript](https://github.com/imartinez/privateGPT/blob/main/source_documents/state_of_the_union.txt) as an example.

## Instructions for ingesting your own dataset

Put any and all of your .txt, .pdf, or .csv files into the source_documents directory

Run the following command to ingest all the data.

```shell
python ingest.py
```

It will create a collection (document and kv store) in FairOS through FaVe. Will take time, depending on the size of your documents.
You can ingest as many documents as you want, and all will be accumulated in FaVe.

## Ask questions to your documents!
In order to ask a question, run a command like:

```shell
python privateGPT.py
```

And wait for the script to require your input. 

```shell
> Enter a query:
```

Hit enter. You'll need to wait 20-30 seconds (depending on your machine) while the LLM model consumes the prompt and prepares the answer. Once done, it will print the answer and the 4 sources it used as context from your documents; you can then ask another question without re-running the script, just wait for the prompt again. 

Note: you could turn off your internet connection, and the script inference would still work. No data gets out of your local environment.

Type `exit` to finish the script.

# How does it work?
Selecting the right local models and the power of `LangChain` you can run the entire pipeline locally, without any data leaving your environment, and with reasonable performance.

- `ingest.py` uses `LangChain` tools to parse the document and create embeddings locally using `LlamaCppEmbeddings`. It then stores the result in a distributed vector database using `FaVe` vector store. 
- `privateGPT.py` uses a local LLM based on `GPT4All-J` or `LlamaCpp` to understand questions and create answers. The context for the answers is extracted from `FaVe` using a similarity search to locate the right piece of context from the docs.
- `GPT4All-J` wrapper was introduced in LangChain 0.0.162.




## Troubleshooting

If you encounter issues, please check the following:

- Make sure all prerequisites are installed.
- Ensure you have the correct configuration in `.env`.

To report bugs or issues, please open an issue on GitHub.

## Contributing

We welcome contributions!

## Tests

Currently, there are no tests. Contributions in this area are welcome.

## Acknowledgments

- Thanks to all contributors and users of this project.

## Contact

For more information or for contributions, please contact us via repo issues.

# Disclaimer
This is a test project to validate the feasibility of a fully private solution for question answering using LLMs and Vector embeddings. It is not production ready, and it is not meant to be used in production. The models selection is not optimized for performance, but for privacy; but it is possible to use different models and vectorstores to improve performance.
