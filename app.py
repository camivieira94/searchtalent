
import streamlit as st
from job_matcher import gerar_match_score

st.set_page_config(page_title="Matcher Recrutamento", layout="centered")

st.title("🤖 Matcher de Candidatos")
st.write("Cole o link do LinkedIn e a descrição da vaga para ver o match:")

linkedin_url = st.text_area("🔗 Link do LinkedIn (ou cole o conteúdo do perfil)")
descricao_vaga = st.text_area("📄 Descrição da Vaga")

if st.button("Analisar"):
    with st.spinner("Analisando compatibilidade..."):
        resultado = gerar_match_score(linkedin_url, descricao_vaga)
        st.success("Análise concluída!")
        st.markdown(resultado)
