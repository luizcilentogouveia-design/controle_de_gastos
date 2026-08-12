Um sistema interativo em linha de comando desenvolvido em Python para cadastro e controle de gastos diários de forma simples e organizada.

## 📌 Visão Geral

Este projeto foi desenvolvido com o objetivo de praticar os pilares da **Programação Orientada a Objetos (POO)** e estruturação de código em Python. A aplicação roda diretamente no terminal, permitindo registrar despesas com descrição, categoria e valor, além de listar todos os itens já cadastrados com formatação amigável.


## ✨ Funcionalidades

- 📝 **Cadastro de Despesas:** Registre descrição, categoria e valor numérico.
- 📋 **Listagem Organizada:** Visualize todos os gastos numerados e com valores formatados em Reais (R$).
- 🛡️ **Validação de Dados:** Tratamento de exceções para impedir que o sistema feche ao receber entradas numéricas inválidas.
- 🔄 **Menu Interativo:** Navegação fluida em loop até que o usuário decida encerrar o programa.

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3 *(100% nativo, sem bibliotecas externas)*.
- **Programação Orientada a Objetos (POO):**
  - Classe `Despesa`: Modelo de dados para representar cada gasto individual.
  - Classe `ControleDespesas`: Gerenciadora da lógica de acúmulo e exibição.
- **Tratamento de Exceções:** Uso de `try / except` (`ValueError`) para tratar entradas do usuário.
- **Estruturas de Dados e Controle:** Listas nativas, navegação com `enumerate`, loops `while` e condicionais `if/elif/else`.
