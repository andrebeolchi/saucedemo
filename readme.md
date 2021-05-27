# Testes Automatizados - Python
> Utilizando Selenium e chromedriver.exe\
> Teste realizado no site [Saucedemo](https://www.saucedemo.com/)

## Usuários

- Usuário Padrão (standard_user)
- Usuário Bloqueado (locked_out_user)
- Usuário com Problema (problem_user)
- Usuário com Falha (performance_glitch_user)

## Funcionalidades do Site

- Login
- Adicionar ao carrinho
- Remover do carrinho
- Abrir carrinho
- Comprar
- Listar dados (A-Z / Z-A / Low-High / High-Low)

> **Usuário Padrão (standard_user)**\
> Realiza todas as funcionalidades de forma correta

> **Usuário Bloqueado (locked_out_user)**\
>  Não consegue entrar na aplicação

> **Usuário com Problema (problem_user)**
> 1. Consegue entrar na aplicação
> 2. Imagem dos produtos errada
> 3. Item Not Found e Preço errado ($√-1)
> 4. Não consegue listar
> 5. Não consegue adicionar *todos* os produtos no carrinho
> 6. Consegue remover do carrinho
> 7. Não consegue realizar a compra (Last Name altera o campo de First Name)

> **Usuário com Falha (performance_glitch_user)**
> Realiza todas as funções, com tempo muito maior de execução
