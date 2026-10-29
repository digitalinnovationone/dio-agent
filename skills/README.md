# Skills do DIO Agent

## O que é uma skill

Uma **skill** é um guia passo a passo que ensina o agente a executar uma tarefa específica bem feita. Em vez de deixar o agente improvisar, a skill dá um processo claro a seguir.

Cada skill fica em uma pasta com um arquivo `SKILL.md`, no formato do padrão aberto de skills para agentes. O que faz o DIO Agent usar a skill é o registro dela no `AGENTS.md`.

## Como o agente usa as skills

O estudante não precisa "chamar" a skill. Basta conversar de forma natural. O agente identifica a necessidade e aplica a skill certa por trás dos panos.

Por exemplo, se o estudante diz "não sei por onde começar", o agente usa a skill de plano de estudos.

A lista oficial de skills, com quando usar cada uma, fica na seção **Skills** do [`AGENTS.md`](../AGENTS.md).

## Como criar uma nova skill

1. Crie uma pasta dentro de `skills/` com um nome curto em inglês (ex.: `study-plan`).
2. Adicione um arquivo `SKILL.md` com o cabeçalho (`name`, igual ao nome da pasta, e `description`, que diz quando usar a skill) e o processo passo a passo. Use as skills existentes como modelo.
3. Registre a skill em dois lugares: na tabela da seção **Skills** do `AGENTS.md`, para o agente saber quando usá-la, e na tabela de skills do `README.md`, para o estudante saber que ela existe.

Mantenha a skill curta e direta. Ela é lida pelo agente a cada uso, então cada linha a mais custa tokens.
