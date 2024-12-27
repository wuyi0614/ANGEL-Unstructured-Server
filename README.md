
# TianGong AI Unstructure Serve

## Env Preparing

Setup `venv`:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install requirements:

```bash
python.exe -m pip install --upgrade pip

pip install --upgrade pip

pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```

```bash
sudo apt update

sudo apt install -y libmagic-dev
sudo apt install -y poppler-utils
sudo apt install -y libreoffice
sudo apt install -y pandoc
```

Test Cuda (optional):

```bash
watch -n 1 nvidia-smi
```

Start Server:

```bash
uvicorn src.main:app --port 7770

CUDA_VISIBLE_DEVICES=0 uvicorn src.main:app --port 7770
CUDA_VISIBLE_DEVICES=1 uvicorn src.main:app --port 7771
CUDA_VISIBLE_DEVICES=2 uvicorn src.main:app --port 7772

# run in background
nohup uvicorn src.main:app --port 7770 > uvicorn.log 2>&1 &

nohup CUDA_VISIBLE_DEVICES=0 uvicorn src.main:app --port 7770 > uvicorn.log 2>&1 &
nohup CUDA_VISIBLE_DEVICES=1 uvicorn src.main:app --port 7771 > uvicorn.log 2>&1 &
nohup CUDA_VISIBLE_DEVICES=2 uvicorn src.main:app --port 7772 > uvicorn.log 2>&1 &

```
