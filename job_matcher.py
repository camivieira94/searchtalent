
import openai

# Configure sua API Key aqui ou via variável de ambiente
openai.api_key = "SUA_API_KEY"

def gerar_match_score(perfil_linkedin: str, descricao_vaga: str) -> str:
    prompt = f"""
    Você é um recrutador especializado. Compare o perfil do LinkedIn abaixo com a descrição da vaga e gere:
    - Uma porcentagem de compatibilidade (0 a 100%)
    - Pontos fortes do candidato
    - Pontos de atenção ou faltantes

    Perfil do LinkedIn:
    {perfil_linkedin}

    Descrição da vaga:
    {descricao_vaga}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    return response['choices'][0]['message']['content']
