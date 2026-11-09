# Laboratório didático — SQL Injection

Este laboratório contém duas versões da mesma função para estudo defensivo:

- `vulnerable_app.py`: exemplo intencionalmente vulnerável, para análise estática.
- `fixed_app.py`: versão com consulta parametrizada.
- `test_fixed_app.py`: testes automatizados da versão corrigida.

## Executar os testes

Requer Python 3.10 ou superior. Não há dependências externas; o exemplo usa SQLite e unittest da biblioteca padrão.

No terminal, entre nesta pasta e execute:

```bash
python -m unittest -v
```

Os testes verificam:
1. autenticação com dados válidos;
2. rejeição de senha incorreta;
3. rejeição de entrada com caracteres SQL maliciosos.

## Aviso

O arquivo vulnerável é somente material didático e não deve ser colocado em produção nem exposto como serviço. A versão corrigida demonstra a parametrização SQL, mas ainda usa senha em texto claro para manter o exemplo focado na SQL Injection. Um sistema real deve armazenar hashes de senha com algoritmo apropriado, como Argon2id, scrypt ou bcrypt, e implementar controles adicionais de autenticação.
