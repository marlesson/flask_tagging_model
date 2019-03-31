# API com Flask

Código simples de uma API em Flask para servir modelos de Machine Learning. O Projeto já está configurado para ser utilizando no Heroku - https://dashboard.heroku.com/ como deploy.

## Modelo

O modelo utilizado é de tagueamento de texto. A base utilizada para o treinamento foi de textos de chat do SAC, onde o objetivo é identificar o setor responsável pela chamada.

[TEXTO] -> [Classe]

```\model\model.joblib```

### Dataset

* https://www.kaggle.com/samuelhei/dataset-for-text-tagging-phone-company-ptbr

## Como começar?

### Instalação 

```
pip install -r requirements.txt 
```

### Execução do Server

```
python main.py
```

### Exemplo de Utilização da API

Chamada HTTP - POST usando o CURL:

```
curl -s "http://localhost:3000/predict" -X POST --header 'Content-Type: application/json' -d '{
    "instances":[
        {"texto": "eu eu quero comprar um telefone"},
        {"texto": "eu solicitei a mudança de endereço mas está com o número trocado"}
    ]
}'
```

## Deploy utilizando o Heroku

Após o ```git commit``` o código pode ser enviado para o heroku. Inscruções de instalação do **console do heroku** podem ser encontrados em https://devcenter.heroku.com/categories/command-line

```
$ heroku create
```

```
$ git push heroku master
```