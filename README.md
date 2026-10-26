# Observatório Brasil 2026 — Eleições Presidenciais 2022–2026

Painel interativo e estudo exploratório de **dados eleitorais públicos**: curvas de apuração, resultados por unidade da federação, abstenção, votos brancos e nulos, e comparação entre os primeiros e segundos turnos de 2022 e 2026.

> Projeto independente, **não vinculado ao TSE**. O painel descreve resultados observados e não atribui causalidade eleitoral a fatores políticos sem evidência adicional.

## Abrir o observatório

- **Navegador / GitHub Pages:** abra `index.html` pelo endereço do GitHub Pages após ativar Pages na branch `main` (pasta raiz).
- **Versão offline:** no site, clique em **“↓ Baixar versão offline”**. Será produzido um único HTML, com gráficos, dados e imagem embutidos, que funciona sem internet.
- **Reconstrução local:** `python tools/rebuild_standalone.py`. Também funciona offline depois do clone, sem dependências Python.

O HTML integral foi dividido em 18 módulos em `payload/` para possibilitar a publicação confiável no GitHub. **Essa divisão não muda os dados nem o código do painel**: o loader concatena os arquivos na ordem original e permite baixar o HTML standalone íntegro.

## Conteúdo

- **Quatro pleitos:** 2022 primeiro turno, 2022 segundo turno, 2026 primeiro turno, 2026 segundo turno.
- **Curvas nacionais:** participação de Lula normalizada entre dois finalistas, por proporção de seções totalizadas — não por tempo.
- **Evolução 2026 primeiro turno:** 76 registros históricos do UOL, com percentuais arredondados; último ponto calculado a partir dos votos finais do TSE.
- **Evolução 2026 segundo turno:** capturas próprias da apuração, registros recuperados no UOL e arquivos EA20 arquivados.
- **27 UFs:** resultados finais, ganhos entre turnos, abstenção, brancos e nulos.
- **Votos incrementais:** somente intervalos com votos absolutos conhecidos. Intervalos de comprimentos diferentes não são diretamente equivalentes.
- **Comparação de bases:** resultados sobre todos os votos válidos e sobre somente os dois principais candidatos são medidas distintas.

## Definições metodológicas

- **Participação na dupla:** `100 × votos_Lula / (votos_Lula + votos_adversário)`. No primeiro turno, exclui os demais candidatos e *não* representa a porcentagem oficial de Lula entre todos os votos válidos.
- **Participação oficial:** `100 × votos_Lula / todos_votos_válidos`.
- **Votos incrementais:** `votos_candidato(t2) - votos_candidato(t1)` para dois snapshots de votos absolutos efetivamente registrados; lotes são de tamanho variável.
- **Abstenção:** calculada usando eleitores aptos e comparecimento conforme a base disponibilizada no conjunto de dados; diferenças de universo eleitoral são documentadas.
- **Curvas:** unem observações reais; *a linha entre dois pontos é apenas conexão visual*, não uma medição minuto a minuto.
- **Fontes:** dados de terceiros podem conter arredondamento ou diferenças de sincronização; compare a documentação e o marcador de origem de cada ponto.

## Resultados nacionais no arquivo

| Pleito | Lula na base dos dois finalistas |
| --- | ---: |
| 2022 · 1º turno (vs. Jair) | 52,86% |
| 2022 · 2º turno (vs. Jair) | 50,90% |
| 2026 · 1º turno (vs. Flávio) | 48,99% |
| 2026 · 2º turno (vs. Flávio) | 51,79% |

Esses percentuais não devem ser interpretados como aprovação popular, nem permitem inferir transferências individuais de voto a partir de totais agregados.

## Arquivos do repositório

- `index.html`: carregador web do painel.
- `payload/part-*.txt`: os 18 segmentos exatos do HTML standalone.
- `dados/observatorio_2026_estaduais_curvas_v3.json`: base completa usada nas análises.
- `dados/apuracao_2026_1turno_serie_observada.csv`: observações publicadas do primeiro turno.
- `tools/rebuild_standalone.py`: reconstrução local do HTML autônomo.
- `.nojekyll`: compatibilidade com GitHub Pages.

## Fontes e auditoria

- [TSE — Divulgação de resultados 2026](https://www.tse.jus.br/eleicoes/eleicoes-2026-content/arquivos/divulgacao-de-resultados)
- [TSE — Histórico da totalização](https://evolucao-totalizacao.tse.jus.br/)
- [TSE — Resultados de 2022](https://www.tse.jus.br/comunicacao/noticias/2022/Outubro/100-das-secoes-totalizadas-confira-como-ficou-o-quadro-eleitoral-apos-o-2o-turno/)
- [UOL — Apuração 2026](https://noticias.uol.com.br/eleicoes/2026/apuracao/)
- [Arquivo de snapshots EA20](https://github.com/gabrielandr/apuracao-2026)

A base JSON identifica origens, precisão e metadados das séries. O projeto usa Plotly, cuja licença está incorporada ao artefato original.

## Licença

MIT para o código autoral, conforme `LICENSE`. Dados oficiais e conteúdo obtido de terceiros permanecem sujeitos a suas respectivas condições de uso.
