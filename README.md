# Observatório Brasil 2026 | Engenharia de dados e visualização interativa

Construí o **Observatório Brasil 2026** como um projeto pessoal de engenharia de dados, análise estatística e desenvolvimento web. Usei dados públicos das eleições presidenciais de 2022 e 2026 para trabalhar um problema que me interessa profissionalmente: **como transformar fontes diferentes, séries históricas incompletas e milhões de registros agregados em informação comparável, auditável e fácil de explorar**.

Meu objetivo aqui não é discutir preferência eleitoral. O processo de apuração foi o estudo de caso. O produto é uma ferramenta analítica: da coleta e organização dos dados à modelagem, visualização e publicação.

## Acesse o projeto

- **[Abrir dashboard interativo](https://pedromaintenance.github.io/analise-tse-22e26/)**
- **Versão offline:** no dashboard, use **“↓ Baixar versão offline”** para salvar um HTML autônomo, com visualizações e dados incorporados.
- **Código e dados:** este repositório é público; deixei as fontes e as limitações documentadas para quem quiser estudar ou reproduzir a análise.

## O que desenvolvi

- Integração de dados eleitorais publicados em fontes diferentes, preservando sua procedência.
- Modelagem de séries de apuração com diferentes frequências, formatos e precisões.
- Comparação dos dois turnos de 2022 e 2026 e análise territorial das 27 unidades da federação.
- Visualizações interativas de resultados finais, evolução da totalização, variações incrementais, comparecimento e votos inválidos.
- Dashboard HTML/JavaScript com Plotly e rotina Python para reconstruir o arquivo standalone.
- Experiência mobile com layout adaptativo e navegação por toque sem zoom acidental nos gráficos.

A principal dificuldade não foi desenhar gráficos. Foi **preservar o sentido dos dados ao compará-los**. Algumas séries têm votos absolutos conhecidos; outras têm percentuais arredondados; há intervalos sem registros. Optei por documentar essas diferenças, em vez de criar uma precisão que as fontes não oferecem.

## Como organizei o projeto

| Caminho | O que você encontra |
| --- | --- |
| `index.html` | Carregador do dashboard publicado no GitHub Pages, incluindo ajustes mobile e apresentação editorial |
| `payload/part-*.txt` | 18 partes do HTML completo, reunidas pelo carregador |
| `dados/observatorio_2026_estaduais_curvas_v3.json` | Base estruturada utilizada no estudo |
| `dados/apuracao_2026_1turno_serie_observada.csv` | Observações históricas do primeiro turno de 2026 |
| `tools/rebuild_standalone.py` | Reconstrução do arquivo HTML original, sem dependências externas de Python |
| `LICENSE` | Licença MIT do código autoral |

No navegador, o carregador reúne os módulos, aplica os ajustes editoriais e responsivos e permite baixar a versão standalone atualizada. O script Python de reconstrução local monta o HTML original dos módulos, sem esses ajustes aplicados pelo carregador.

## Critérios da análise

Trabalhei com **quatro pleitos** (primeiro e segundo turnos de 2022 e 2026). Para comparar situações diferentes, apresento separadamente:

- **Participação entre os dois principais candidatos:** `100 × votos_Lula / (votos_Lula + votos_adversário)`. No primeiro turno, isso não representa o percentual oficial sobre todos os votos válidos.
- **Participação sobre todos os votos válidos:** `100 × votos_Lula / total_votos_válidos`.
- **Variação incremental:** diferença dos votos acumulados entre duas observações com contagens absolutas. Os intervalos não têm tamanhos iguais.
- **Abstenção:** relação entre eleitores que não compareceram e eleitorado apto, respeitando a cobertura de cada fonte.

As curvas conectam **observações registradas**, não uma medição contínua de cada segundo da apuração. Também não utilizo resultados agregados para presumir transferência individual de voto, comportamento de eleitores ou causalidade política.

**Exemplo de leitura:** a participação de Lula na base restrita aos dois finalistas é 52,86% (1º turno de 2022), 50,90% (2º turno de 2022), 48,99% (1º turno de 2026) e 51,79% (2º turno de 2026). Os dois percentuais de primeiro turno são normalizações analíticas, não o resultado oficial entre todos os candidatos.

## Fontes utilizadas

- [TSE — divulgação de resultados de 2026](https://www.tse.jus.br/eleicoes/eleicoes-2026-content/arquivos/divulgacao-de-resultados)
- [TSE — evolução da totalização](https://evolucao-totalizacao.tse.jus.br/)
- [TSE — resultados de 2022](https://www.tse.jus.br/comunicacao/noticias/2022/Outubro/100-das-secoes-totalizadas-confira-como-ficou-o-quadro-eleitoral-apos-o-2o-turno/)
- [UOL — histórico da apuração de 2026](https://noticias.uol.com.br/eleicoes/2026/apuracao/)
- [Arquivo independente de snapshots EA20](https://github.com/gabrielandr/apuracao-2026)

Identifico limitações de precisão, diferenças de sincronização e cobertura das fontes no material do dashboard e na base JSON.

## Por que publiquei

Trabalho com engenharia de manutenção, indicadores, dados e sistemas. Tenho interesse em desenvolver soluções que aproximem o dado bruto de decisões e investigações concretas. Neste projeto, apliquei essa prática em outro domínio para explorar integração, estatística, engenharia de visualização e desenvolvimento de aplicações.

**Muda o conjunto de dados; permanece o trabalho de formular boas perguntas, construir indicadores consistentes e permitir que outras pessoas examinem os resultados.**

Sugestões técnicas e contribuições são bem-vindas.

---

Projeto pessoal e independente, **sem vínculo institucional com o TSE**. Código autoral sob licença MIT. Dados públicos e conteúdos de terceiros mantêm suas próprias condições de uso. O Plotly está incorporado ao artefato com sua licença.
