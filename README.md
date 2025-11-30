# Indução Matemática e Recursividade: Algoritmos e Aplicações

Este repositório contém os códigos-fonte desenvolvidos como parte integrante do trabalho acadêmico **"Indução e Recursão: Definições, Propriedades e Aplicações Computacionais"**, apresentado ao curso de Sistemas de Informação do IFSULDEMINAS - Campus Machado.

👉 **[Ler Artigo Completo (PDF)](./INDUCAO_E_RECURSAO.pdf)**

## 📝 Sobre o Projeto

O objetivo deste projeto é demonstrar a conexão prática entre o **Princípio da Indução Matemática** e a construção de **Algoritmos Recursivos**. Os scripts aqui presentes ilustram como a lógica de *Caso Base* e *Passo Indutivo* se traduz em código funcional, além de abordar conceitos de complexidade e gerenciamento de memória (Pilha de Execução).

**Autor:** Gustavo Martins de Lima  
**Disciplina:** Matemática Discreta  
**Professor:** Dr. Peterson Pereira de Oliveira  
**Instituição:** IFSULDEMINAS - Campus Machado  
**Ano:** 2025

## 📂 Estrutura dos Arquivos
Os códigos estão escritos em **Python 3** e organizados conforme a sequência lógica do artigo:

* `1-fatorial.py`: Implementação recursiva do cálculo de fatorial com prova de corretude.
* `2-pilha_chamada.py`: Demonstração didática do funcionamento da *Call Stack* (exemplo das saudações).
* `3.1-stack_overflow.py`: Exemplo proposital de recursão infinita para demonstrar o estouro de pilha.
* `3.2-correcao_stack_overflow.py`: Correção do algoritmo anterior com a definição do Caso Base.
* `4-celula_bonacci.py`: Solução recursiva para o problema das "Células Bonacci" (variação da Sequência de Fibonacci).
* `5-somatorio_simples.py`: Comparação de desempenho entre laço de repetição (for) e fórmula fechada (Gauss).

## 🚀 Como Executar

Certifique-se de ter o [Python 3](https://www.python.org/) instalado em sua máquina.

1.  Clone este repositório:
    ```bash
    git clone https://github.com/gustavo-gml/Algoritmos-Inducao-Recursao.git

    ```
2.  Acesse a pasta do projeto:
    ```bash
    cd Algoritmos-Inducao-Recursao

    ```
3.  Execute o arquivo desejado. Exemplo:
    ```bash
    python3 4-celula_bonacci.py
    ```

## 📚 Conceitos Abordados

* **Indução Matemática:** A base lógica para provar que um algoritmo funciona para qualquer entrada n.
* **Recursividade:** A técnica de dividir um problema em subproblemas menores (instâncias).
* **Pilha de Execução (Call Stack):** Gerenciamento de memória LIFO (*Last In, First Out*).
* **Complexidade:** Comparação entre soluções O(n) (Iterativas) vs O(1) (Fórmulas Fechadas).

## 📄 Licença

Este projeto é destinado a fins acadêmicos e educacionais. Sinta-se à vontade para estudar e modificar os códigos.

---
*Desenvolvido por Gustavo Martins de Lima.*

