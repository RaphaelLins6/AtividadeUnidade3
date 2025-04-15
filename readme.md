# 🛰️ Decifrando Mensagens Estelares com C#

## 🚀 Objetivo

Consolidar e expandir o conhecimento sobre os loops `for` e `while` (adaptado aqui para `for`) utilizando a linguagem **C#**, através de um desafio temático de decodificação de mensagens.

---

## 🧠 Cenário

Você é um(a) **criptoanalista espacial** e interceptou uma série de mensagens codificadas vindas de diferentes planetas. Essas mensagens contêm letras **maiúsculas**, **minúsculas**, **números** e **símbolos**. Seu trabalho é **decifrá-las** para entender as intenções dos alienígenas.

---

## 🛠️ Tecnologias Utilizadas

<p align="center"> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" height="40" alt="csharp logo"/>
<img width="12" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" alt="Visual Studio Code" width="50" height="40"/> 

---

## 📝 Tarefa

### ✅ Etapas da atividade:

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

---

## 📚 Aprendizados

- Manipulação de strings em C#
- Uso de loops aninhados
- Verificação e conversão de caracteres com `char.IsLower`, `char.IsUpper`, `char.ToLower`
- Filtragem de conteúdo em uma string
- Entrada e saída de dados no console

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
dotnet run
```
### 4. **Digite as mensagens no console**
Siga as instruções no terminal para inserir as mensagens codificadas.
O programa exibirá a versão decifrada automaticamente.

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