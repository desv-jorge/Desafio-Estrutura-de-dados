
# 💼 Hierarquia de Funcionários - Estrutura em Árvores (Desafio 5)

Este repositório contém a solução do **Desafio 5** da disciplina de Estruturas de Dados em Python. O desafio propõe modelar uma estrutura organizacional de uma empresa utilizando **árvores genéricas (N'árias)**, onde cada funcionário pode ter múltiplos subordinados.

## 📚 Descrição

A árvore representa a hierarquia de cargos em uma empresa, com o **CEO como nó raiz** e os demais funcionários como filhos e descendentes. A estrutura permite:

- Inserção de subordinados
- Impressão hierárquica com indentação
- Busca por funcionário
- Listagem de subordinados
- Contagem de subordinados
- Verificação de existência
- Remoção de funcionário
- Percursos: pré-ordem, pós-ordem e em nível (BFS)

## 📌 Estrutura de Dados Utilizada

A **árvore N'ária** foi escolhida por ser a mais adequada para representar relações de hierarquia com múltiplos níveis e filhos por nó. Cada funcionário é um nó com uma lista de subordinados.

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/hierarquia-funcionarios-arvore.git
   cd hierarquia-funcionarios-arvore
   ```

2. Execute o script Python:
   ```bash
   python solucao.py
   ```

O programa irá imprimir uma hierarquia organizacional de exemplo e demonstrar todas as funcionalidades implementadas.

## 📂 Arquivos

- `solucao.py` – Código principal com a classe `Funcionario` e exemplos de uso no bloco `if __name__ == "__main__"`.

## ✅ Exemplo de Hierarquia Simulada

```
CEO
  Diretor de Tecnologia
    Gerente de TI
      Analista de TI
      Administrador de banco de dados
    Gerente de Desenvolvimento
      Dev Frontend
      Dev Backend
        Estagiário Dev
  Diretor Financeiro
    Gerente de RH
      Analista Financeiro
  Diretor de Marketing
    Assistente de Marketing
```

## 👨‍💻 Autor

- Nathanael Jorge dos Santos
