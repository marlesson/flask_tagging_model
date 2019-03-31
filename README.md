## Deploy no Heroku

## Chamada de API

```
curl -s "http://localhost:3000/predict" -X POST --header 'Content-Type: application/json' -d '{
    "instances":[
        {"texto": "eu eu quero comprar um telefone"},
        {"texto": "eu solicitei a mudança de endereço mas está com o número trocado"}
    ]
}'
```