# API de Validação de CPF

[![Status](https://img.shields.io/badge/status-on-brightgreen)](https://api-cpf.vercel.app/)
[![GitHub license](https://img.shields.io/github/license/piedro404/cpf-validation-api)](https://github.com/piedro404/cpf-validation-api/blob/main/LICENSE)

Esta é uma API de validação de CPF. Ela permite que você verifique se um CPF é válido e também gere CPFs válidos aleatórios. Hospedada em [https://api-cpf.vercel.app/](https://api-cpf.vercel.app/).

OBS: A validação é feita matematicamente, ou seja, usando apenas uma fórmula matemática demonstrada na seção [Recursos]

### Validar CPF
![2023-07-03_17h58_19](https://github.com/piedro404/cpf-validation-api/assets/88720549/125f96d4-ecd9-4a8d-9c61-605b5bf2823e)

### Gerar CPF's
![image](https://github.com/piedro404/cpf-validation-api/assets/88720549/9d4e1c6b-8bd0-4566-a754-a1e5bf4d1159)

## Recursos
- Validação de CPF: Verifica se um número de CPF é válido ou inválido.
- Geração de CPFs: Gera uma lista de CPFs válidos.

Se baseia em uma fórmula matemática disponível em [calculadorafacil](https://www.calculadorafacil.com.br/computacao/validar-cpf#:~:text=Passos%20para%20validar%20CPF%201%20Calcular%20o%20primeiro,aos%20d%C3%ADgitos%20fornecidos%2C%20ent%C3%A3o%20o%20CPF%20%C3%A9%20v%C3%A1lido) para aprofundamento, e a fórmula é a seguinte:
- Estrutura do CPF

![cpf_formato](https://github.com/piedro404/cpf-validation-api/assets/88720549/b7626be2-74dd-4e6e-a93a-af29944d8f33)
- Formula base
  
![cpf_digito_verificador_1](https://github.com/piedro404/cpf-validation-api/assets/88720549/c31d9b3e-7b7b-4d5a-8172-60c71d5bea7b)

## Documentação

Acesse a [documentação da API](https://api-cpf.vercel.app/docs) para obter informações detalhadas sobre os endpoints, parâmetros e testes de requisições.

### Como usar
1. Rota principal ("/"): Retorna um JSON com uma descrição da API. <br>(https://api-cpf.vercel.app/)

```bash
{
  "Status":true,
  "Description":"Api de validação CPF ON!"
}
```
2. Rota de validação de CPF ("/cpf/valid/{cpf}"): Recebe um CPF e retorna um JSON com o resultado da validação. <br>(https://api-cpf.vercel.app/cpf/valid/{cpf})

```bash
{
  "Valid": true,
  "CPF": "02511560364",
  "Status": "CPF valid!"
}
```
3. Rota de geração de CPFs ("/cpf/generator/{qtd}"): Recebe a quantidade de CPFs a serem gerados e retorna uma lista de CPFs. <br>(https://api-cpf.vercel.app/cpf/generator/{qtd})

```bash
{
  "944.455.117-22",
  "792.645.105-32",
  "252.035.413-53",
  "846.698.742-84",
  "587.367.725-50",
  "929.245.290-85",
  "246.988.777-17",
  "382.068.474-30",
  "563.825.185-57",
  "999.223.946-85"
}
```

## Instalação
### Pré-requisitos

Certifique-se de ter o Python 3 instalado. Você também pode criar um ambiente virtual para isolar as dependências do projeto.

1. Clone este repositório:
   
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Instale as dependências:
   
   ```bash
   pip install -r requirements.txt
   ```

### Executando a API

1. Execute o seguinte comando para iniciar a API:

   ```bash
   python Main.py
   ```
2. A API será executada localmente em http://localhost:8000.

## Licença
Este projeto está licenciado sob a Licença MIT. Por favor, inclua a seguinte referência no seu trabalho derivado:
<br>
- API de Validação de CPF - desenvolvida por [Piedro404](https://github.com/piedro404) sob a Licença MIT.


Obrigado a todos, desejo otimos estudos, caso queira, entre em contato em pedro.henrique.martins404@gmail.com.
