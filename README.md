# EDUC.AI
##Sistema educacional com recomendação de conteudo

Este repositório contém uma aplicação baseada em agentes inteligentes utilizando a plataforma CREWAI. O projeto desenvolve cinco agentes que auxiliam alunos no processo de aprendizado, fornecendo planos de estudo personalizados, guias de estudo detalhados, curadoria de conteúdos relevantes, mensagens motivacionais e integração com APIs externas para enriquecimento educacional.

## 📌 Objetivos do Projeto

O projeto explora a construção de agentes inteligentes que operam de forma autônoma para otimizar a experiência de estudo dos alunos, oferecendo suporte personalizado, organização eficiente e materiais de alta qualidade.

### 🧠 Agentes Inteligentes Desenvolvidos

1. **Coach Motivador**  
   💡 **Responsável por**: Enviar mensagens motivacionais em formato Markdown, incentivando foco, disciplina e engajamento dos alunos durante os estudos.

2. **Coordenador Especialista em Guia de Estudos**  
   📚 **Responsável por**: Criar guias de estudo personalizados, com introdução, conceitos fundamentais, aplicações práticas, técnicas de aprendizado e sugestões de materiais gratuitos, formatados em Markdown.

3. **Coordenador Especialista em Plano de Estudos**  
   📅 **Responsável por**: Desenvolver planos de estudo com cronogramas, distribuição equilibrada de tópicos, técnicas ativas de aprendizado, revisões programadas e sugestões para pausas, adaptados ao tempo disponível do aluno.

4. **Coordenador Especialista em Curadoria de Vídeos**  
   🎥 **Responsável por**: Pesquisar e organizar vídeos educacionais do YouTube, filtrando conteúdos relevantes e formatando-os em Markdown com títulos, URLs e descrições.

5. **Coordenador Especialista em Curadoria de Artigos**  
   📜 **Responsável por**: Selecionar e organizar artigos da Wikipedia em português, formatando-os em Markdown com títulos, URLs e trechos explicativos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11.0**  
- **CREWAI** (Plataforma para criação de agentes inteligentes)  
- **YouTube API** (Para busca de vídeos educativos)  
- **Wikipedia API** (Para busca de artigos educacionais)  
- **Gradio** (Interface web interativa)  
- **ReportLab** (Geração de PDFs)  
- **Ambiente virtual (.venv)**  
- **Gerenciamento de pacotes com PIP**

---

## 📌 Instalação e Configuração

Siga os passos abaixo para configurar o ambiente e executar o projeto.

### Passo 1: Verificando a versão do Python

O projeto requer **Python 3.11.0**. Verifique a versão instalada:

```sh
python --version
```

Caso necessário, baixe a versão correta em: [Python Downloads](https://www.python.org/downloads/).

### Passo 2: Atualizando o PIP

Atualize o **PIP** para garantir a instalação correta das dependências:

```sh
python -m pip install --upgrade pip
```

### Passo 3: Criando e Ativando o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências:

#### Criando o ambiente virtual:
```sh
python -m venv .venv
```

#### Ativando o ambiente virtual:
- **Windows**:
  ```sh
  .venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```sh
  source .venv/bin/activate
  ```

### Passo 4: Instalando Dependências

Instale as bibliotecas listadas no `requirements.txt`:

```sh
pip install -r requirements.txt
```

O arquivo `requirements.txt` inclui:
```
crewai==0.67.1
google-api-python-client==2.149.0
gradio==4.44.0
reportlab==4.2.2
requests==2.32.3
```

### Passo 5: Configurando Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione as chaves de API necessárias:

```
YOUTUBE_API_KEY=sua-chave-da-api-do-youtube
GROQ_API_KEY_01=sua-chave-groq-01
GROQ_API_KEY_02=sua-chave-groq-02
```

Obtenha as chaves:
- **YouTube API**: [Google Cloud Console](https://console.cloud.google.com/)
- **GROQ API**: Consulte a documentação do provedor para obter as chaves.

---

## 📖 Como Funciona o Projeto

1. O **Aluno** insere informações via interface Gradio (disciplina, assunto, tópicos, horas diárias e dias disponíveis).
2. O **Coach Motivador** gera uma mensagem motivacional em Markdown.
3. O **Coordenador de Guia de Estudos** cria um guia detalhado com conceitos, aplicações e materiais.
4. O **Coordenador de Plano de Estudos** elabora um cronograma personalizado.
5. O **Coordenador de Curadoria de Vídeos** pesquisa vídeos no YouTube e os organiza.
6. O **Coordenador de Curadoria de Artigos** seleciona artigos relevantes da Wikipedia.
7. O sistema gera um arquivo Markdown e um PDF com todos os conteúdos, disponíveis para download.

A interface Gradio exibe o progresso em tempo real e permite baixar os arquivos gerados.

---

## 🚀 Executando o Projeto

1. Ative o ambiente virtual (veja Passo 3).
2. Execute o arquivo principal:

```sh
python app.py
```

3. Acesse a interface Gradio no navegador (o link será exibido no terminal).
4. Preencha os campos (disciplina, assunto, tópicos, etc.) e clique em "Gerar Material".

---

## 📌 Como Contribuir

Para contribuir com o projeto:

1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua funcionalidade (`git checkout -b minha-feature`).
3. Faça o **commit** das alterações (`git commit -m 'Adiciona nova feature'`).
4. Envie a branch para o repositório remoto (`git push origin minha-feature`).
5. Abra um **Pull Request**.

---

## 📝 Notas Adicionais

- Certifique-se de que as chaves de API estão configuradas corretamente para evitar erros.
- O projeto suporta caracteres UTF-8 e emojis em PDFs, graças ao `ReportLab`.
- A curadoria de vídeos exclui YouTube Shorts para garantir qualidade educacional.
- Para suporte ou dúvidas, abra uma **issue** no repositório.
