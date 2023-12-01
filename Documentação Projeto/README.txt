1. Cliente (Agente)

a) Conexão com o Servidor:
- Utilização de sockets TCP para estabelecer a comunicação entre o cliente e o servidor.

b) Operações do Cliente:

i. Ao ser executado, o cliente informa ao servidor sobre sua presença, fornecendo o nome do HOST, IP e usuário logado no sistema.

ii. Execução em segundo plano para liberar o terminal ao usuário.

iii. Verificação periódica da disponibilidade do servidor quando este estiver offline.

iv. Prevenção contra múltiplas instâncias, garantindo que apenas uma instância do cliente esteja na memória.

v. Implementação de uma funcionalidade para remoção do cliente da memória.

vi. Resposta a requisições do servidor enquanto estiver em execução.

2. Servidor

a) Conexão com Múltiplos Clientes:
- Permitir múltiplas conexões de clientes simultaneamente utilizando sockets TCP.

b) Gerenciamento de Conexões:

i. Monitoramento das conexões ativas para detectar quando um cliente fica offline.

ii. Execução em segundo plano para liberar o terminal ao usuário.

iii. Prevenção contra múltiplas instâncias, garantindo que apenas uma instância do servidor esteja na memória.

iv. Implementação de uma funcionalidade para remoção do servidor da memória.

v. Implementação de um comando para solicitar informações de hardware dos agentes.

vi. Implementação de um comando para solicitar a lista de programas instalados nos agentes.

vii. Implementação de um comando para solicitar o histórico de navegação nos navegadores suportados pelos agentes.

viii. Implementação de um comando para solicitar informações detalhadas do usuário logado nos agentes.

ix. Implementação de um comando para listar os agentes online, trazendo informações como IP, nome do HOST, usuário logado e tempo online.

3. Integração com Telegram:
- Utilização de um bot no Telegram para chamar comandos no servidor e interagir com os agentes.

4. Observações Gerais:
- Não são permitidas bibliotecas de terceiros nos comandos que envolvem informações específicas do sistema operacional, como detalhes do usuário logado.
