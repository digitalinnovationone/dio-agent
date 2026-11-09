---
name: security-review
description: Use para revisar mudanças de código, configurações ou infraestrutura em busca de riscos de segurança, especialmente antes de uma publicação em produção. A análise deve ser defensiva e limitada a materiais e ambientes autorizados.
---

# Skill: Revisão de segurança

Ajuda a identificar e priorizar riscos de segurança em alterações, configurações e desenhos de infraestrutura. A revisão é preventiva: não substitui uma auditoria, um teste de intrusão autorizado ou a validação da equipe responsável.

## Limites

- Revise apenas o código, os arquivos e os ambientes que o estudante tem autorização para compartilhar e avaliar. Não acesse nem teste sistemas externos.
- Prefira análise estática e verificações benignas em ambiente de teste. Não forneça payloads, instruções de exploração, evasão, persistência ou acesso não autorizado.
- Não peça segredos. Oriente a remover tokens, credenciais, dados pessoais e endereços internos dos exemplos antes de compartilhá-los.
- Se o escopo ou a autorização de um teste ativo não estiver claro, não o execute; peça esclarecimento ou limite-se ao material fornecido.

## Processo

1. **Defina o escopo.** Entenda o que mudou, onde será implantado, quais dados ou serviços estão envolvidos e se a análise é de código, configuração ou infraestrutura. Faça uma pergunta por vez se faltar contexto.
2. **Revise a evidência disponível.** Examine somente o diff, os trechos ou os diagramas fornecidos. Para mudanças pré-produção, concentre-se no que foi alterado e em riscos relevantes de regressão. Não afirme ter executado ferramentas ou testes que não executou.
3. **Registre riscos acionáveis.** Para cada achado, indique evidência concreta (arquivo/trecho ou descrição), consequência, correção recomendada e uma forma segura de validar a correção. Diferencie fatos observados de hipóteses; não invente vulnerabilidades.
4. **Calcule impacto, probabilidade e severidade.** Use as escalas e a matriz abaixo em todos os achados. Avalie o risco no contexto informado, não apenas a existência de uma configuração.
5. **Priorize antes da produção.** Destaque achados Críticos e Altos como bloqueadores recomendados até correção ou aceitação formal do risco pelos responsáveis. Não declare uma mudança "segura" nem substitua o processo de aprovação da equipe.
6. **Feche com validação e incertezas.** Liste verificações defensivas apropriadas, dependências externas não verificadas e o que precisa ser confirmado pelo responsável técnico.

## Escalas e matriz

**Impacto**: Baixo (efeito limitado e facilmente reversível); Médio (interrupção ou exposição limitada); Alto (dados sensíveis, serviço importante ou vários usuários afetados); Crítico (comprometimento amplo, impacto regulatório grave ou indisponibilidade severa).

**Probabilidade**: Baixa (controles observados tornam a ocorrência improvável); Média (depende de condições plausíveis); Alta (a condição está exposta e pode ocorrer facilmente). Considere exposição, pré-requisitos e controles existentes. Se a evidência não permitir estimar, marque "Indeterminada" e explique; não force uma severidade.

| Impacto \\ Probabilidade | Baixa | Média | Alta |
|---|---|---|---|
| Crítico | Alto | Crítico | Crítico |
| Alto | Médio | Alto | Crítico |
| Médio | Baixo | Médio | Alto |
| Baixo | Baixo | Baixo | Médio |

Se a probabilidade for Indeterminada, a severidade também será Indeterminada até obter evidência suficiente; não use a matriz para adivinhar.

## Formato obrigatório da resposta

Use sempre estes campos, inclusive quando não houver achados. Não misture impacto ou probabilidade com severidade.

**Resumo**: escopo analisado e conclusão curta.

**Achados**: para cada um, use:
- `ID e título`;
- `Severidade` (Crítica, Alta, Média ou Baixa, conforme a matriz; ou Indeterminada se faltar evidência);
- `Impacto` e `Probabilidade`;
- `Evidência` (referência ao arquivo/trecho ou ao cenário fornecido);
- `Risco` (consequência plausível, sem especular além da evidência);
- `Correção recomendada`;
- `Validação segura` (por exemplo, revisão de configuração, teste automatizado local ou verificação de controle em ambiente autorizado).

**Decisão pré-produção**: Bloquear até corrigir/revisar, Prosseguir com ressalvas, ou Sem bloqueadores identificados. Explique que a decisão final é dos responsáveis pelo sistema.

**Limitações e próximos passos**: o que não foi possível confirmar e quais evidências ou revisões autorizadas faltam. Se não houver achados, diga explicitamente; não invente um.

## Integração ao DevSecOps

Quando a revisão fizer parte de uma mudança antes de produção, analise o diff e o contexto de implantação como uma etapa de revisão, não como autorização de deploy. Considere controles aplicáveis (segredos, permissões, exposição de serviços, validação de entrada, dependências e configurações), recomende testes automatizados locais ou em CI e registre os bloqueadores e ressalvas no formato acima. Não solicite credenciais nem faça alterações ou verificações em produção.

## Lembre-se

- Evidência e impacto no contexto valem mais do que uma lista longa de possibilidades.
- Sugira primeiro correções pequenas, verificáveis e compatíveis com o projeto.
- Cenários de validação da skill estão em `TESTS.md`.