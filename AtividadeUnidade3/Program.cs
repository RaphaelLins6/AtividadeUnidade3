using System;
using System.Collections.Generic;

// 1 - Lista de mensagens codificadas - Lista vazia
List<string> mensagensCodificadas = new List<string>();

// 2 - Peça ao usuário para informar quantas mensagens ele vai digitar
Console.Write("Quantas mensagens deseja digitar? ");
int quantidade = int.Parse(Console.ReadLine());

// 3 -  Use um loop for para receber cada mensagem via Console.ReadLine()
for (int i = 0; i < quantidade; i++)
{
    Console.Write($"Digite a mensagem codificada #{i + 1}: ");
    string? mensagem = Console.ReadLine();
    mensagensCodificadas.Add(mensagem);
}

Console.WriteLine("Decodificando mensagens...\n");

// Loop para cada mensagem codificada
foreach (string codificada in mensagensCodificadas)
{
    string decifrada = "";

    // Loop para cada caractere da mensagem
    for (int i = 0; i < codificada.Length; i++)
    {
        char c = codificada[i];

        // Se for letra minúscula, adiciona como está
        if (char.IsLower(c))
        {
            decifrada += c;
        }
        // Se for letra maiúscula, converte para minúscula e adiciona
        else if (char.IsUpper(c))
        {
            decifrada += char.ToLower(c);
        }
        // Números e símbolos são ignorados
    }

    // Exibir os resultados
    Console.WriteLine($"Mensagem codificada: {codificada}");
    Console.WriteLine($"Mensagem decifrada : {decifrada}\n");
}