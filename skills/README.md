# Skills do DIO Agent

## O que é uma skill

Uma **skill** é um guia passo a passo que ensina o agente a executar uma tarefa específica bem feita. Em vez de deixar o agente improvisar, a skill dá um processo claro a seguir.

Cada skill fica em uma pasta com um arquivo `SKILL.md`. Esse formato segue o padrão aberto de skills para agentes, então funciona em diferentes harnesses.

## Como o agente usa as skills

O estudante não precisa "chamar" a skill. Basta conversar de forma natural. O agente identifica a necessidade e aplica a skill certa por trás dos panos.

Por exemplo, se o estudante diz "não sei por onde começar", o agente usa a skill de plano de estudos.

## Skills disponíveis

| Skill | Para que serve | Exemplo de pedido do estudante |
|-------|----------------|--------------------------------|
| [study-plan](study-plan/SKILL.md) | Montar um plano de estudos organizado | "Quero ser dev back-end, por onde começo?" |
| [unblock-challenge](unblock-challenge/SKILL.md) | Destravar um desafio sem entregar a resposta | "Travei nesse desafio, me ajuda?" |
| [explain-concept](explain-concept/SKILL.md) | Explicar um conceito de forma didática | "Não entendi o que é uma API." |
| [web-search](web-search/SKILL.md) | Fundamentar respostas com busca atual e fontes citadas | "Qual a versão estável do Node hoje?" |

## Como criar uma nova skill

1. Crie uma pasta dentro de `skills/` com um nome curto em inglês.
2. Adicione um arquivo `SKILL.md` com o cabeçalho e o processo (siga o modelo das skills existentes).
3. Adicione a skill na tabela de `AGENTS.md` para o agente saber quando usá-la.
