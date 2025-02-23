
# The Unstructured Server for ANGEL-NTU

This project was derived from [Tiangong-AI Unstructure Serve](https://github.com/linancn/TianGong-AI-Unstructure-Serve). 
The following changes were made separately from the other relevant projects.

## Quick start

To quickly kick off the project, we highly recommend running the following tutorial and the server in a Linux-based environment.

For the test at 23 Feb 2025, we use ubuntu 20.04 (aarch64).

1. In order to make the Linux sys ready for deployment, install the following dependencies:

```bash
sudo apt update

sudo apt install -y libmagic-dev
sudo apt install -y poppler-utils
sudo apt install -y libreoffice
sudo apt install -y pandoc
sudo apt install -y graphicsmagick
```

2. Prepare your Python interpreter (3.12 recommended) with `pipenv`:

```bash
# use `pipenv` to manage the dependencies, and you may install `pipenv` using pip or conda
pip install pipenv
```

Make sure you're at the root path of the project, and run the codes:
```bash
pipenv install  # till you see the `Pipfile` and `Pipfile.lock` are successfully generated
pipenv shell    # you may use the command `shell` to activate the virtualenv with pipenv, which is only visible for the project
```

If you'd like to use GPU for parsing, test CUDA (optional):

```bash
watch -n 1 nvidia-smi
```

3. Start the service with `uvicorn`:

```bash
# `uvicorn` in ENV VARIABLE is only accessible after executing `pipenv shell`
uvicorn src.main:app --host 0.0.0.0 --port 7770  # ... run this with console output or,
nohup uvicorn src.main:app --host 0.0.0.0 --port 7770 > uvicorn.log 2>&1 &  # ... run it in daemon

# to enable CUDA for the service: run the following codes explicitly,
CUDA_VISIBLE_DEVICES=0 uvicorn src.main:app --host 0.0.0.0 --port 7770
CUDA_VISIBLE_DEVICES=1 uvicorn src.main:app --host 0.0.0.0 --port 7771
CUDA_VISIBLE_DEVICES=2 uvicorn src.main:app --host 0.0.0.0 --port 7772

# ... or in daemon
nohup env CUDA_VISIBLE_DEVICES=0 uvicorn src.main:app --host 0.0.0.0 --port 7770 > uvicorn.log 2>&1 &
nohup env CUDA_VISIBLE_DEVICES=1 uvicorn src.main:app --host 0.0.0.0 --port 7771 > uvicorn.log 2>&1 &
nohup env CUDA_VISIBLE_DEVICES=2 uvicorn src.main:app --host 0.0.0.0 --port 7772 > uvicorn.log 2>&1 &
```
