# Teste Devops

Para executar o parser primeiro deve ter instalado no seu computador o Docker e Dockercompose

O Parser é feito em python:

Existem 2 funções dentro do codigo python que executa o json.log e file.log separadamente, escolhi fazer em um unico arquivo para ser mais limpo e não precisar de 2 ou mais dockercompose.

Implementei algumas correções que removeram alguns caracteres especiais afim de facilitar mais a leitura do CSV como por exemplo "delimiter =',', quotechar='"', escapechar='\\'".

Caso não tenha dado permissões para o docker será necessário executar essa linha "sudo chown $USER:docker /var/run/docker.sock" antes de executar o docker-compose up.
Baixando os arquivos para seu computador ja podemos executar o "docker-compose up"

No dockercompose.yml foi criado um volume O volume do compose faz um espelho entre a sua pasta local e a pasta app de dentro do container como mostra no exemplo abaixo

        volumes:
            - .:/app
            
Issso é necessário para a coleta do CSV que é gerado no parser.
