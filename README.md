# LP3 IFSP

Repositório para organizar os códigos da disciplina Linguagem de Programação 3.

## Instruções Lab de informática

Ao chegar no laboratório:

1-configurar o usuário local do git

```bash

git config --global user.name "seu nome"
git config --global user.email "seuemail@gmail.com"

```
2-fazer o clone do seu repositório no Github
```bash

git clone https://github.com/SEU_USUARIO/lp3-ifsp.git

```

3-brir o repo no VScode

```bash
code lp3-ifsp
```

4-Criar um token para realizar o pushs

Settings --> Developer settings --> Personal access tokens -->Tokens (classic)
Generate new token, selecionar a opção Generate new token classic, marcar a opção scope repo

### Antes de sair do Laboratório

```bash
git config --global --unset user.name
git config --global --unset user.email
```

Deletar o token no Github
Deslogar do Github