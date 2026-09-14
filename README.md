# Projeto Python + Docker

Projeto simples para atividade acadêmica de GitHub, GitHub Actions e Docker.

## Executar localmente

```bash
pip install -r requirements.txt
python app.py
```

Acesse http://localhost:5000

## Executar com Docker

```bash
docker build -t projeto-python .
docker run -d -p 5000:5000 --name projeto-python-container projeto-python
docker ps
```

Acesse http://localhost:5000
