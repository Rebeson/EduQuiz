# EduQuiz - Sistema de Quiz Educacional
Projeto de avaliação da Disciplina de Programação Orientada a Objetos do curso de Tecnologia em Banco de Dados pela Universidade Federal do Cariri - UFCA. O sistema permite o gerenciamento de questões acadêmicas, a realização de testes com sorteio randômico e o acompanhamento de desempenho através de rankings.

## Integrantes da Equipe:
Ânderson Carlos de Sousa - Responsável pela interface (CLI)  
Ramon de Sousa Batista - Responsável por implementar o Banco de Dados (SQL)  
Rebeson Oliveira Vitalino - Responsável por implementar a Sistema do Quiz  
Victor de Araújo Nunes - Responsável por implementar a Sistema do Quiz e Controle de Qualidade (QA)  


## Funcionalidades:
Controle de Acesso: Diferenciação entre perfis de ADMIN (gestão de questões) e ALUNO (execução de testes).

Quiz Randômico: Seleção automática e aleatória de questões cadastradas no banco de dados.

Pontuação por Peso: Atribuição de pontos baseada na dificuldade configurada no cadastro da pergunta (Fácil = 1 ponto, Médio = 2 pontos, Difícil = 3 pontos).

Persistência SQL: Armazenamento de usuários, perguntas e histórico de tentativas em SQLite3.

Configuração via JSON: Regras de negócio (limite de tentativas e pesos) no arquivo settings.json.

## Estrutura do Projeto
main.py: Ponto de entrada da aplicação e gerenciador de menus.
settings.json: Arquivo de configuração das regras do sistema. O comportamento do quiz é regido por este arquivo. Caso queira alterar a dificuldade do sistema, basta editar os valores.

Classes/:

Usuario.py: Gerencia dados de login e o perfil do usuário.
Pergunta.py: Define a estrutura e as validações das questões.
Quiz.py: Agregador de perguntas para execução.
BancoDados.py: Camada de persistência e comandos SQL.
Configuracao.py: Interface de leitura das regras do JSON.
Perfil.py & Dificuldade.py: Definições de tipos constantes (Enums).
Excecoes.py: Tratamento de erros customizados.

## Como Executar
1. Certifique-se de ter o Python 3.10 ou superior instalado.
2. Mantenha a estrutura de pastas com a pasta Classes e os arquivos main.py, settings.json e quiz_banco.db.
3. Execute o sistema pelo terminal com o comando: python main.py
4. No primeiro acesso, crie uma conta como Administrador (opção 2) para poder cadastrar as perguntas que alimentarão o quiz.

Obs: Se o sistema apresentar erro de estrutura de colunas, delete o arquivo quiz_banco.db para que o banco de dados seja recriado com as tabelas atualizadas. (Importante: Será necessário cadastrar novas perguntas e usuários)

