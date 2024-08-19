Telegram Group Message Sender
Este script utiliza a biblioteca Telethon para automatizar o envio de mensagens em grupos do Telegram. O script busca automaticamente os grupos em que o usuário participa e envia uma mensagem personalizada para cada um deles.

Pré-requisitos
Antes de usar este script, você precisa ter:

Python 3.7 ou superior instalado em seu sistema.

Como usar
pip install telethon
1. Obtenha as Credenciais do Telegram
Você precisará das credenciais de API fornecidas pelo Telegram. Siga os passos abaixo:

Vá até my.telegram.org.
Faça login com seu número de telefone.
Vá até a seção API Development Tools.
Anote o api_id e o api_hash que serão gerados.
2. Modifique o Script

No código fornecido, substitua as seguintes variáveis com suas próprias credenciais:

api_id = 'SEU_API_ID'
api_hash = 'SEU_API_HASH'
phone_number = 'SEU_NUMERO_TELEFONE'
Preencha também a mensagem que deseja enviar nos grupos:

message = "Sua mensagem aqui"
3. Execute o Script
Após ajustar as variáveis, você pode executar o script com o seguinte comando:

python nome_do_arquivo.py

O script irá:

Conectar-se à sua conta do Telegram.
Buscar todos os grupos dos quais você participa.
Enviar a mensagem definida para cada grupo.
Exemplo de Execução
Ao executar o script, você verá no terminal a lista de grupos e o status de envio das mensagens:

Group name: Grupo 1, Group ID: 123456789
Group name: Grupo 2, Group ID: 987654321
Mensagem enviada para o grupo 123456789
Mensagem enviada para o grupo 987654321

Erros Comuns
Erro de autenticação: Certifique-se de que o api_id, api_hash e phone_number estejam corretos.
Timeout ou erro ao enviar mensagem: Certifique-se de ter uma conexão estável com a internet. O script faz uma pausa de 2 segundos entre o envio das mensagens para evitar problemas de spam.
Contribuição
Se você tiver sugestões ou encontrar problemas, sinta-se à vontade para abrir uma issue ou fazer um fork e enviar um pull request.

Licença
Este projeto é licenciado sob os termos da licença MIT. Para mais detalhes, veja o arquivo LICENSE.
