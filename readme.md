# N1 02 – Comparação de Padrões MPEG

## Descrição do Projeto

Este projeto tem como objetivo comparar os principais **padrões da família MPEG (Moving Picture Experts Group)** e o padrão **H.264 (AVC)**.  
A aplicação foi desenvolvida em **Python com Streamlit**, permitindo visualizar de forma interativa as características, diferenças e aplicações de cada padrão de compressão de vídeo e multimídia.

O trabalho atende aos requisitos da atividade **“N1 02 – Comparação de padrões MPEG”**, que solicita a criação de uma **tabela comparativa** e uma **análise contextualizada** sobre os principais padrões de compressão digital.

---

## Funcionalidades

- Exibição de **tabela comparativa** dos padrões MPEG e H.264  
- Visualização da **linha do tempo** (bar chart) mostrando o ano de criação de cada padrão  
- Expansores com **detalhes técnicos e aplicações** de cada padrão  
- Interface interativa e responsiva feita com **Streamlit**

---

## Padrões Analisados

| Padrão | Ano | Tipo | Qualidade | Taxa de Bits | Aplicações |
|:-------|:----:|:-----|:-----------|:--------------|:------------|
| MPEG-1 | 1991 | Vídeo e Áudio | VHS | ~1.5 Mbit/s | VCD, MP3, TV a cabo |
| MPEG-2 | 1996 | Vídeo e Áudio | Transmissão TV | 3–15 Mbit/s | TV digital, DVD |
| MPEG-4 | 1998 | Vídeo, Áudio e Multimídia | Alta (Internet a Blu-ray) | kbps a dezenas de Mbps | Streaming, dispositivos móveis |
| MPEG-7 | 2001 | Metadados Multimídia | N/A (descrição) | N/A | Bibliotecas digitais, busca |
| MPEG-21 | 2001 | Framework Multimídia | N/A (gerenciamento) | N/A | DRM, e-commerce |
| H.264 (AVC) | 2003 | Vídeo | Excelente (SD a HD) | Muito flexível | Blu-ray, streaming, videoconferência |

---

## Tecnologias Utilizadas

- **Python 3**
- **Streamlit**
- **Pandas**
- **Pathlib**

---

## Contextualização

O **MPEG** é um grupo de trabalho da ISO/IEC responsável por desenvolver padrões internacionais para **compressão, transmissão e representação de áudio e vídeo digital**.  

Os principais avanços entre os padrões se relacionam a:
- **Compressão:** aumento da eficiência e redução da taxa de bits.  
- **Qualidade:** melhoria significativa da imagem e do som.  
- **Latência:** menor atraso em transmissões e videoconferências.  
- **Aplicações:** expansão para streaming, Blu-ray, TV digital e sistemas de metadados.

---

## Análise

- **MPEG-1** introduziu a compressão digital de vídeo e áudio (base para o MP3).  
- **MPEG-2** trouxe qualidade de transmissão e suporte a TV digital.  
- **MPEG-4** adicionou suporte a multimídia interativa e maior compressão.  
- **MPEG-7** e **MPEG-21** estenderam o escopo para metadados e gestão de direitos digitais.  
- **H.264 (AVC)** revolucionou o vídeo digital com alta eficiência e ampla adoção em streaming e Blu-ray.

---

## Execução do Projeto

Para executar a aplicação:

```bash
# Instalar dependências
pip install streamlit pandas

# Executar o aplicativo
streamlit run main.py
