import os
import gradio as gr
from crewai import Task, Agent, LLM
from xhtml2pdf import pisa
from youtube import pesquisar_videos_youtube

GROQ_API_KEY_01 = os.environ.get("GROQ_API_KEY_01")
groqllm = LLM(
    model="groq/llama-3.3-70b-versatile",
    #model="groq/deepseek-r1-distill-llama-70b",
    api_key=GROQ_API_KEY_01
)
GROQ_API_KEY_02 = os.environ.get("GROQ_API_KEY_02")
groqllm2 = LLM(
    model="groq/llama-3.3-70b-versatile",
    #model="groq/deepseek-r1-distill-llama-70b",
    api_key=GROQ_API_KEY_02
)

def processar_topicos(topicos_str):
    """ Converte uma string de tópicos separada por vírgulas em uma lista tratada. """
    return [t.strip() for t in topicos_str.split(',') if t.strip()]

def executar_equipe_interface(disciplina, assunto, topicos_str, horas, dias):
    
    topicos = processar_topicos(topicos_str)

    solicitacao = f"Disciplina: {disciplina}\nAssunto: {assunto}\nTópicos: {topicos}\n"

    # Chamada API do YouTube
    entradaYoutube = pesquisar_videos_youtube(solicitacao)

    # Agente Motivador
    agentMotivador = Agent(
        role='Motivador',
        goal='Escrever uma mensagem motivacional para o estudante.',
        backstory='Você é um coach motivacional com experiência em ajudar estudantes a manterem o foco.',
        llm=groqllm,
        verbose=True
    )

    taskMotivador = Task(
        description='Escrever uma mensagem motivacional para o estudante.',
        agent=agentMotivador,
        expected_output='Dois parágrafos com uma mensagem motivacional em markdown.'
    )

    # Agente Guia de Estudos
    agentGuia = Agent(
        role="Especialista em Guia de Estudos",
        goal="Criar um guia de estudos estruturado, explicativo e didático sobre um determinado assunto.",
        backstory="Você é um especialista em educação, com experiência na criação de guias de estudo detalhados.",
        llm=groqllm,
        verbose=True
    )

    taskGuia = Task(
        description=(
            f"Crie um Guia de Estudos para {disciplina}, abordando {assunto} e os tópicos {topicos}. "
            "O guia deve conter:\n"
            "1. Introdução ao tema\n"
            "2. Conceitos fundamentais com exemplos\n"
            "3. Aplicações práticas\n"
            "4. Técnicas de aprendizado e dificuldades comuns\n"
            "5. Indicação de materiais gratuitos (livros, vídeos, artigos)\n"
            "Deve ser didático e acessível para alunos do ensino médio."
        ),
        agent=agentGuia,
        expected_output='Guia de estudos em markdown'
    )

    # Agente Plano de Estudos
    agentPlano = Agent(
        role="Especialista em Plano de Estudos",
        goal="Criar um plano de estudos eficiente para que o aluno aprenda de maneira organizada.",
        backstory="Você é um planejador educacional especialista em cronogramas de estudo eficientes.",
        llm=groqllm2,
        verbose=True
    )

    taskPlano = Task(
        description=(
            f"Crie um Plano de Estudos para {disciplina}, cobrindo {assunto} e {topicos}. "
            f"O aluno tem {horas} horas por dia e {dias} dias para estudar.\n"
            "O plano deve incluir:\n"
            "1. Distribuição equilibrada dos tópicos\n"
            "2. Técnicas ativas (resumos, flashcards, mapas mentais, exercícios)\n"
            "3. Revisões programadas\n"
            "4. Monitoramento do progresso\n"
            "5. Sugestões para pausas e evitar sobrecarga mental"
        ),
        agent=agentPlano,
        expected_output='Plano de estudos estruturado em markdown'
    )

    # Agente Curador de Vídeos Educacionais
    agentYoutube = Agent(
        role='Especialista em Curadoria de Vídeos Educacionais',
        goal='Organizar e formatar vídeos educacionais encontrados no YouTube para aprendizado eficiente.',
        backstory=(
            'Você é um especialista em curadoria de materiais educacionais, com ampla experiência '
            'na seleção e organização de vídeos do YouTube para fins de ensino. '
            'Seu objetivo é filtrar, organizar e formatar esses vídeos de forma clara e acessível.'
        ),
        llm=groqllm2,
        verbose=True
    )

    taskYoutube = Task(
        description=(
            f"Lista do Youtube: {entradaYoutube}"
            "Você receberá uma lista de vídeos extraída da API do YouTube. Sua tarefa é classificar e organizar os vídeos "
            "por categorias, formatando-os em Markdown. As categorias devem ser baseadas no título do vídeo."
            "O formato de saída deve ser exataente esse:\n\n"
            f"## Vídeos sobre {assunto}\n\n"
            "caso tenha mais de um vídeo repetir a seguinte configuração:"
            "**[Título](URL)**\n\n _Descrição_\n\n"
            "e se algum vídeo não tiver descrição, substitua por '(Sem descrição disponível)'."
        ),
        agent=agentYoutube,
        expected_output="Lista de vídeos organizados em Markdown."
    )

    # Execução sequencial dos agentes
    saidaMotivador = agentMotivador.execute_task(taskMotivador)
    saidaGuia = agentGuia.execute_task(taskGuia)
    saidaPlano = agentPlano.execute_task(taskPlano)
    saidaYoutube = agentYoutube.execute_task(taskYoutube)
    
    saidaCompleta = f"{saidaMotivador}\n\n{saidaGuia}\n\n{saidaPlano}\n\n{saidaYoutube}"

    return saidaCompleta

# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Gerador de Material de Estudos")
    with gr.Row():
        with gr.Column():
            disciplina = gr.Textbox(label="Disciplina", value="Matemática")
            assunto = gr.Textbox(label="Assunto", value="Funções")
            topicos_str = gr.Textbox(label="Tópicos", value="Função quadrática, Função exponencial, Função logarítmica")
            horas = gr.Textbox(label="Tempo diário", value="2 horas")
            dias = gr.Textbox(label="Quantos dias", value="5 dias")
            gerar_button = gr.Button("Gerar Material")
        with gr.Column():
            resultado = gr.Markdown(label="Material Completo (Markdown)")
    
    gerar_button.click(fn=executar_equipe_interface,
                       inputs=[disciplina, assunto, topicos_str, horas, dias],
                       outputs=resultado)

demo.launch()
