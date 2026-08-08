# Research Copilot

An AI-powered scientific paper assistant built with FastAPI, Transformers, PEFT, and DPO.

## Features

- Scientific paper summarization
- Question answering
- SFT fine-tuning
- DPO alignment
- FastAPI backend
- Docker deployment

## Tech Stack

- Python=3.11
- FastAPI
- Hugging Face
- Transformers
- PEFT
- Docker

## Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n research-copilot python=3.11
```
3) Activate the environment:
```bash
$ conda activate research-copilot
```

### (Optional) Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 9000
```
