# EduQuiz
Projeto de avaliação da Disciplina de Programação Orientada a Objetos do curso de Tecnologia em Banco de Dados pela Universidade Federal do Cariri - UFCA

## Integrantes da Equipe:
Ânderson Carlos de Sousa - Responsável pela interface (CLI)
Ramon de Sousa Batista - Responsável por implementar o Banco de Dados (SQL)
Rebeson Oliveira Vitalino - Responsável por implementar a Sistema do Quiz
Victor de Araújo Nunes - Responsável por implementar a Sistema do Quiz e Controle de Qualidade (QA)


## Principais Classes do Projeto

Class: Pergunta
Atributos: enunciado, alternativas, tema, dificuldade, resposta_certa

Class: BancoDados
Atributos: nome_banco
Métodos: _criar_tabela

Class: SistemaQuiz
Atributos: id, nome, email, pergunta, tema
Métodos: cadastrar_usuario, cadastrar_pergunta, executar_quiz
