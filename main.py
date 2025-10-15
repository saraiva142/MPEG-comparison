import streamlit as st
import pandas as pd
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Comparação de Padrões MPEG",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🎬 Comparação de Padrões MPEG")
st.markdown("### Análise e comparação de padrões de compressão de vídeo")

# Sidebar com navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio(
    "Escolha uma opção:",
    ["Tabela Comparativa", "Sobre os Padrões"]
)

# Dados da tabela comparativa
dados_tabela = {
    "Padrão": ["MPEG-1", "MPEG-2", "MPEG-4", "MPEG-7", "MPEG-21", "H.264 (AVC)"],
    "Ano": [1991, 1996, 1998, 2001, 2001, 2003],
    "Tipo": [
        "Vídeo e Áudio",
        "Vídeo e Áudio",
        "Vídeo, Áudio e Multimídia",
        "Metadados Multimídia",
        "Framework Multimídia",
        "Vídeo"
    ],
    "Qualidade": [
        "VHS",
        "Transmissão TV",
        "Alta (Internet a Blu-ray)",
        "N/A (descrição)",
        "N/A (gerenciamento)",
        "Excelente (SD a HD)"
    ],
    "Taxa de Bits": [
        "~1.5 Mbit/s",
        "3-15 Mbit/s",
        "Kbps a dezenas de Mbps",
        "N/A",
        "N/A",
        "Muito flexível"
    ],
    "Aplicações": [
        "VCD, MP3, TV a cabo",
        "TV digital, DVD",
        "Internet, streaming, móveis",
        "Bibliotecas digitais, busca",
        "DRM, e-commerce",
        "Blu-ray, streaming, videoconferência"
    ]
}

# Página: Tabela Comparativa
if pagina == "Tabela Comparativa":
    st.header("📊 Tabela Comparativa de Padrões MPEG")
    
    st.markdown("""
    Esta tabela apresenta uma comparação entre os principais padrões MPEG e H.264, destacando suas 
    características, qualidade, taxa de bits e aplicações comuns.
    """)
    
    df = pd.DataFrame(dados_tabela)
    
    # Exibir tabela com estilo
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    # Gráfico de comparação de anos
    st.subheader("Linha do Tempo dos Padrões")
    st.bar_chart(df.set_index("Padrão")["Ano"])
    
    # Informações adicionais
    st.markdown("---")
    st.subheader("Principais Diferenças")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🎥 Padrões de Compressão")
        st.markdown("""
        - **MPEG-1**: Primeiro padrão, qualidade VHS
        - **MPEG-2**: TV digital e DVD
        - **MPEG-4**: Internet e streaming
        - **H.264**: Alta eficiência, HD
        """)
    
    with col2:
        st.markdown("#### 📝 Padrões de Metadados")
        st.markdown("""
        - **MPEG-7**: Descrição de conteúdo multimídia
        - Usa XML para metadados
        - Busca e recuperação eficientes
        - Não é codec de compressão
        """)
    
    with col3:
        st.markdown("#### 🔧 Framework")
        st.markdown("""
        - **MPEG-21**: Framework multimídia
        - Gerenciamento de direitos digitais
        - Interoperabilidade
        - Comércio eletrônico de mídia
        """)

# Página: Sobre os Padrões
elif pagina == "Sobre os Padrões":
    st.header("📚 Sobre os Padrões MPEG")
    
    st.markdown("""
    O **Moving Picture Experts Group (MPEG)** é um grupo de trabalho da ISO/IEC que desenvolve 
    padrões para compressão de áudio e vídeo digital, além de outros aspectos relacionados à multimídia.
    """)
    
    # MPEG-1
    with st.expander("🎥 MPEG-1 (1991)"):
        st.markdown("""
        **MPEG-1** é o primeiro padrão de compressão de vídeo e áudio desenvolvido pelo grupo MPEG.
        
        **Características:**
        - Compressão com perdas usando DCT e compensação de movimento
        - Qualidade comparável ao VHS
        - Taxa de bits de aproximadamente 1.5 Mbit/s
        - Compressão de 26:1 para vídeo e 6:1 para áudio
        
        **Aplicações:**
        - Video CD (VCD)
        - MP3 (áudio)
        - TV a cabo e satélite (sistemas antigos)
        - CD-i
        """)
    
    # MPEG-2
    with st.expander("📺 MPEG-2 (1996)"):
        st.markdown("""
        **MPEG-2** é o sucessor do MPEG-1, projetado para maior qualidade e flexibilidade.
        
        **Características:**
        - Suporte a vídeo entrelaçado
        - Qualidade de transmissão de TV
        - Taxa de bits variável de 3 a 15 Mbit/s
        - Compatível com MPEG-1
        
        **Aplicações:**
        - Televisão digital (DVB, ATSC)
        - DVD-Vídeo
        - Blu-ray (para compatibilidade)
        - HDV
        """)
    
    # MPEG-4
    with st.expander("🌐 MPEG-4 (1998)"):
        st.markdown("""
        **MPEG-4** é um grupo de padrões para compressão de áudio, vídeo e multimídia.
        
        **Características:**
        - Melhor eficiência que MPEG-2
        - Suporte a mídia mista (vídeo, áudio, fala)
        - Resiliência a erros
        - Perfis e níveis para diferentes aplicações
        - Inclui H.264/AVC (Parte 10)
        
        **Aplicações:**
        - Vídeo na Internet
        - Streaming de vídeo
        - Dispositivos móveis
        - Blu-ray Disc (com H.264/AVC)
        """)
    
    # MPEG-7
    with st.expander("🔍 MPEG-7 (2001)"):
        st.markdown("""
        **MPEG-7** é um padrão para descrição de conteúdo multimídia, não para compressão.
        
        **Características:**
        - Usa XML para armazenar metadados
        - Permite busca e recuperação eficientes
        - Descrição de características visuais e de áudio
        - Não é um codec de compressão
        
        **Aplicações:**
        - Bibliotecas digitais
        - Serviços de diretório multimídia
        - Edição de multimídia
        - Aplicações educacionais e biomédicas
        """)
    
    # MPEG-21
    with st.expander("🔧 MPEG-21 (2001)"):
        st.markdown("""
        **MPEG-21** é um framework para aplicações multimídia.
        
        **Características:**
        - Define "Itens Digitais" como unidades de distribuição
        - Gerenciamento de direitos digitais (DRM)
        - Identificação de itens digitais
        - Interoperabilidade entre aplicações
        
        **Aplicações:**
        - Gerenciamento de direitos digitais
        - Comércio eletrônico de mídia
        - Distribuição de conteúdo digital
        """)
    
    # H.264
    with st.expander("🎬 H.264 / MPEG-4 AVC (2003)"):
        st.markdown("""
        **H.264** (também conhecido como MPEG-4 Parte 10 ou AVC) é um padrão de compressão de vídeo altamente eficiente.
        
        **Características:**
        - Altamente eficiente (redução significativa na taxa de bits)
        - Excelente qualidade de vídeo
        - Flexível (baixas a altas taxas de bits)
        - Múltiplos quadros de referência
        - Pode ser otimizado para baixa latência
        
        **Aplicações:**
        - Blu-ray Disc
        - Streaming de vídeo (YouTube, Netflix)
        - Videoconferência
        - Transmissão de TV digital
        - Câmeras de segurança
        """)
    
    st.markdown("---")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Desenvolvido para comparação de padrões MPEG | N1 02 – Comparação de padrões MPEG</p>
</div>
""", unsafe_allow_html=True)

