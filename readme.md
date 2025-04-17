# 🛰️ Aventura em uma Galáxia Distante

## 🚀 Objetivo

Consolidar e expandir o conhecimento sobre os loops `for` e `while` (adaptado aqui para `for`) utilizando a linguagem **C#** e **Python**, através de um desafio temático de decodificação de mensagens.

---

## 🧠 Cenário

## Atividade 1 - Decifrando Mensagens Estelares com for
Você é um(a) **criptoanalista espacial** e interceptou uma série de mensagens codificadas vindas de diferentes planetas. Essas mensagens contêm letras **maiúsculas**, **minúsculas**, **números** e **símbolos**. Seu trabalho é **decifrá-las** para entender as intenções dos alienígenas.

## Atividade 2 - Navegação Segura em um Campo de Asteroides com while
Você é um(a) piloto espacial e precisa navegar sua nave por um campo de asteroides perigoso. Você tem um sensor que detecta a distância do asteroide mais próximo.

---

## 🛠️ Tecnologias Utilizadas

<p align="center"> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" height="40" alt="csharp logo"/>
<img width="12" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/2048px-Python.svg.png" alt="Python" width="50" height="40"/> &nbsp;&nbsp; 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" alt="Visual Studio Code" width="50" height="40"/>

---

## 📝 Tarefa

### ✅ Etapas da atividade:

## Atividade 1: Decifrando Mensagens Estrelares com for
1. Crie uma lista contendo pelo menos **3 mensagens codificadas** inseridas pelo usuário.
2. Use um loop `for` para coletar essas mensagens via input.
3. Em seguida, utilize outro loop `foreach` para percorrer cada mensagem e:
   - Crie uma string vazia para armazenar a **mensagem decifrada**.
   - Use um loop `for` interno (aninhado) para iterar sobre cada caractere.
   - Aplique as seguintes regras:
     - Se o caractere for uma **letra minúscula**, adicione-o diretamente à mensagem decifrada.
     - Se for uma **letra maiúscula**, **converta para minúscula** e adicione à mensagem decifrada.
     - **Ignore números e símbolos**.
4. Imprima a mensagem original e a mensagem decifrada.
   
## Atividade 2: Navegação Segura em um campo de Asteroides com while
1. Dena uma distância inicial segura (um número inteiro positivo).
2. Utilize um loop while para simular a navegação. O loop deve continuar enquanto a
distância do asteroide mais próximo for menor que a distância segura.
3. Dentro do loop:
   - Gere uma distância aleatória para o asteroide mais próximo (um número
   inteiro entre 1 e 10).
   - Imprima a distância do asteroide.
   - Se a distância for menor que 3, imprima uma mensagem de "PERIGO!" e
   encerre o loop usando break.
   - Se a distância for menor que a metade da distância segura, imprima um aviso
   de "Aproximando-se de asteroide!".
    - Aumente a distância segura em um valor xo (por exemplo, 2) para simular o
   piloto se afastando dos asteroides.
4. Se o loop terminar sem ser interrompido por break, imprima uma mensagem de
"Navegação concluída com segurança!".

---

## 📚 Aprendizados

- Manipulação de strings em C#
- Uso de loops aninhados
- Verificação e conversão de caracteres com `char.IsLower`, `char.IsUpper`, `char.ToLower`
- Filtragem de conteúdo em uma string
- Entrada e saída de dados no console
- Simulação de cenários com while e geração de números aleatórios em Python
- Lógica condicional para controle de fluxo em tempo real

---

## 🚀 Como Utilizar o Repositório ?

Siga os passos abaixo para compilar e executar o projeto no seu computador:

### 1. **Clone o repositório**

```bash
git clone https://github.com/RaphaelLins6/AtividadeUnidade3.git
cd AtividadeUnidade3
```
Ou, simplesmente copie os arquivos .cs para uma pasta local.

### 2. **Compile o código**
Se estiver usando o .NET SDK:
```bash
dotnet new console -o AtividadeUnidade3
cd AtividadeUnidade3
```
### 3. **Execute o programa**
```bash
dotnet run --project AtividadeUnidade3
```
### 4. **Digite as mensagens no console**
Siga as instruções no terminal para inserir as mensagens codificadas.
O programa exibirá a versão decifrada automaticamente.

### 5. **Execute o código Python
Se desejar rodar a simulação espacial (Atividade2)
```bash
python atividade2.py
```
---

## 👥 Autores

**Turma de ciência da computação - UDF**
- [@RaphaelLins6](https://www.github.com/RaphaelLins6) - Raphael Lins (RGM:27797660)
- [@jotape99](https://www.github.com/jotape99) - João Pedro (RGM:28167333)
- [@joaogkt](https://www.github.com/joaogkt) - João Gabriel (RGM:28017188)

---

## 📜 Licença

Este projeto é livre para uso e modificação. Contribuições são bem-vindas! 😊

---
