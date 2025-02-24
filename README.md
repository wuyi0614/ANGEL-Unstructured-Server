
# The Unstructured Server for ANGEL-NTU

This project was derived from [Tiangong-AI Unstructure Serve](https://github.com/linancn/TianGong-AI-Unstructure-Serve). 
The following changes were made separately from the other relevant projects.

## Quick start

To quickly kick off the project, we highly recommend running the following tutorial and the server in a Linux-based environment.

For the test at 23 Feb 2025, we use ubuntu 20.04 (aarch64).

**First**, in order to make the Linux sys ready for deployment, install the following dependencies:

```bash
sudo apt update

sudo apt install -y libmagic-dev
sudo apt install -y poppler-utils
sudo apt install -y libreoffice
sudo apt install -y pandoc
sudo apt install -y graphicsmagick
sudo apt install -y tesseract-ocr
```

Then, download lang data for `tesseract` from the repo on GitHub: 

```bash
curl -o t410.tar.gz -L https://github.com/tesseract-ocr/tessdata/archive/refs/tags/4.1.0.tar.gz
sudo tar -zxvf t410.tar.gz -C /usr/share/tesseract-ocr/4.00/tessdata  # note: the directory may change!
share/tesseract-ocr/4.00/tessdata/ --strip-components 1 --exclude=tesseract-4.1.0/configs --exclude=tesseract-4.1.0/tessconfigs --exclude="README.md"
```

**Second**, prepare your Python interpreter (3.12 recommended) with `pipenv`:

```bash
# use `pipenv` to manage the dependencies, and you may install `pipenv` using pip or conda
pip install pipenv
```

Make sure you're at the root path of the project, and run the codes:
```bash
# run `install` till you see the `Pipfile` and `Pipfile.lock` are successfully generated
pipenv install

# you may use the command `shell` to activate the virtualenv with pipenv, which is only visible for the project
pipenv shell
```

**Third**, configure your customised config files at: `src/config/`. Use `secrets-local.toml` instead of `secrets.toml` 
for locally execution. Configure the following params in `secrets.toml`:

```toml
[FASTAPI]
AUTH="***"
BEARER_TOKEN="***"
MIDDLEWARE_SECRECT_KEY="***"

[OPENAI]
API_KEY="***"
```

If you'd like to use GPU for parsing, test CUDA (optional):

```bash
watch -n 1 nvidia-smi
```

**Fourth**, run `pytest` before launching:

```bash
# customise your `pytest.ini` if the filenames or dirnames were changed
python -m pytest
```

**Note**: if you're running the server on instances located within China Mainland, configure the following params before running:
```bash
# make sure you have `huggingface_hub` in your Pipfile and executed `pipenv install`
# make sure you're at the project dir and switch into the venv
pipenv shell 
export HF_ENDPOINT="https://hf-mirror.com"
```

**Fifth**, start the service with `uvicorn`:

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

## TODO
- [ ] create & execute full tests for routers and the top-level services
- [x] the PDF rounter is down `[detected on 23 Feb 2025]`
  - [x] error msg `"detail": "An error happened while trying to locate the file on the Hub and we cannot find the requested files in the local cache. Please check your connection and try again or make sure your Internet connection is on."`
  - [x] add `hf-mirror` to the huggingface's hub or local entryfolders to `unstructured` package
  - [x] add the missing config to `tesseract`
