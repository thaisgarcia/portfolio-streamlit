import streamlit as st
import streamlit_option_menu
from streamlit_timeline import timeline

st.set_page_config(
    page_title="Thais Garcia",
    page_icon="👋",
    layout='wide',
)

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.write("# Thais Garcia")
st.write("### Bem-vindo(a) ao meu Portfolio! 👋")

st.write("---")

with st.container():
    selected = streamlit_option_menu.option_menu(
        menu_title=None,
        options=['Sobre mim', 'Habilidades', 'Projetos'],
        icons=['person', 'rocket-takeoff', 'code-slash'],
        orientation='horizontal'
    )


if selected == 'Sobre mim':
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(
                """
                    <div style='display: flex; justify-content: center; align-items:center; height:32vh;'>
                        <img src='https://media.licdn.com/dms/image/D4D03AQGOp3exzAUoPQ/profile-displayphoto-shrink_400_400/0/1712425464854?e=1723680000&v=beta&t=LUe6aAAC08s7MY5Oo7dyZ_LnCIG16wYWFRTw_GQR_rc' style='width:180px; border-radius: 20px; display: flex;'/>
                    </div>
                """, unsafe_allow_html=True, )
        with col2:
            st.markdown(
                """
                <br>
                <div style="text-align: justify;">
                    <p>
                        Olá, sou a Thais Garcia, tenho 19 anos, e minha paixão pela tecnologia moldou meu 
                        percurso acadêmico e profissional. Graduei-me na Etec Jacinto Ferreira de Sá, obtendo 
                        qualificação como Administradora de Banco de Dados e tornando-me 
                        <strong>Técnica em Desenvolvimento de Sistemas</strong>. Atualmente, estou cursando o Tecnólogo 
                        em <strong>Ciência de Dados</strong> na <strong>Faculdade de Tecnologia de Ourinhos (FATEC)</strong>.
                        <br></br>
                        No âmbito profissional, integro ativamente a equipe do Núcleo Tecnológico de Educação Aberta (NTEA), 
                        Núcleo de Educação a Distância (NEAD), e equipe multidisciplinar
                        no Centro Universitário das Faculdades Integradas de Ourinhos (UNIFIO). Ofereço suporte técnico
                        a professores, coordenadores e estudantes no Ambiente Virtual de Aprendizagem (AVA). 
                        Além disso, sou responsável pela análise e produção de relatórios, bem como pela implementação
                        de novas tecnologias essenciais para a melhoria contínua desse ambiente.
                    </p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True, )

    st.write("#### Linha do Tempo:")
    with st.spinner(text="Building line"):
        with open('timeline.json', "r", encoding='utf-8') as f:
            data = f.read()
            timeline(data, height=600)

if selected == 'Habilidades':
    with st.container():
        option = st.selectbox(
            'Selecione uma opção:',
            ('Linguagens', 'Bibliotecas Python Para Data Science', 'Frameworks')
        )

        if option == 'Linguagens':
            st.write("")
            st.markdown(
                """
                BACK-END:

                ![PHP](https://img.shields.io/badge/PHP-000?style=for-the-badge&logo=php)
                ![C#](https://img.shields.io/badge/CSharp-000?style=for-the-badge&logo=csharp&logoColor=A020F0)
                ![C++](https://img.shields.io/badge/C++-000?style=for-the-badge&logo=cplusplus&logoColor=4169E1)
                ![Java](https://img.shields.io/badge/Java-000?style=for-the-badge&logo=java)
                ![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)
                ![MySql](https://img.shields.io/badge/MySql-000?style=for-the-badge&logo=mysql)

                <br>

                FRONT-END: 

                ![HTML5](https://img.shields.io/badge/HTML-000?style=for-the-badge&logo=html5)
                ![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=264CE4)
                """, unsafe_allow_html=True)

        elif option == 'Bibliotecas Python Para Data Science':
            st.write("")
            st.markdown(
                """
                MANIPULAÇÃO DE DADOS E ESTATÍSTICA:

                ![Pandas](https://img.shields.io/badge/Pandas-000?style=for-the-badge&logo=pandas)
                ![Numpy](https://img.shields.io/badge/Numpy-000?style=for-the-badge&logo=numpy)
                ![StatsModels](https://img.shields.io/badge/Statsmodels-000?style=for-the-badge&logo=statsmodels)

                <br>

                VISUALIZAÇÃO DE DADOS E DASHBOARDS: 

                ![Matplotlib](https://img.shields.io/badge/Matplotlib-000?style=for-the-badge&logo=matplotlib)
                ![Seaborn](https://img.shields.io/badge/Seaborn-000?style=for-the-badge&logo=seaborn)
                ![Plotly](https://img.shields.io/badge/Plotly-000?style=for-the-badge&logo=plotly)

                <br>

                MACHINE LEARNING:

                ![Scikit-learn](https://img.shields.io/badge/Scikitlearn-000?style=for-the-badge&logo=scikit-learn)

                <br>

                DEEP LEARNING: 

                ![TensorFlow](https://img.shields.io/badge/TensorFlow-000?style=for-the-badge&logo=tensorflow)
                ![PyTorch](https://img.shields.io/badge/PyTorch-000?style=for-the-badge&logo=pytorch)

                <br>

                DATA APP: 

                ![Streamlit](https://img.shields.io/badge/Streamlit-000?style=for-the-badge&logo=streamlit)
                """, unsafe_allow_html=True)

        elif option == 'Frameworks':
            st.write("")
            st.markdown(
                """
                    FRAMEWORKS PYTHON: 

                    ![Dash](https://img.shields.io/badge/Dash-000?style=for-the-badge&logo=dash)
                    ![Flask](https://img.shields.io/badge/Flask-000?style=for-the-badge&logo=flask)

                    <br>

                    FRAMEWORKS CSS:

                    ![Bootstrap](https://img.shields.io/badge/Bootstrap-000?style=for-the-badge&logo=bootstrap)
                    ![Tailwind](https://img.shields.io/badge/Tailwind-000?style=for-the-badge&logo=tailwind)
                """, unsafe_allow_html=True)


elif selected == 'Projetos':
    with st.container():
        st.markdown(
            """
            <div class="container">
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Caixeiro Viajante</p>
                        </div>
                        <div class="content">
                            <p>
                                Este projeto combina automação web com algoritmos de otimização de rotas para resolver o 
                                problema do caixeiro viajante, utilizando Python, Selenium e Google Maps.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/caixeiro-viajante" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Conversor de Arquivos</p>
                        </div>
                        <div class="content">
                            <p>
                                Este repositório contém scripts Python para processar dados destinados ao Censo do MEC, 
                                incluindo a leitura de um arquivo TXT, a geração de um arquivo Excel e a conversão desse 
                                arquivo Excel de volta para um formato de texto.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/convert-censo-file" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Chatbot Barbearia</p>
                        </div>
                        <div class="content">
                            <p>
                                Criação de um chatbot utilizando a biblioteca ChatterBot e o framework Flask.
                                <br><i>Projeto destinado a uma disciplina da faculdade, não deu tempo de finalizar.</i>
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/chatterbot-flask" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Definição de Imagens</p>
                        </div>
                        <div class="content">
                            <p>
                                Criação de um modelo de Inteligência Artificial capaz de prever 
                                se uma imagem pertence a uma das seguintes classes: camiseta/top, 
                                calça, pulôver, vestido, casaco, sandália, camisa, tênis, bolsa ou bota de cano curto.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/pytorch-image-definition" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Análise de Séries Temporais</p>
                        </div>
                        <div class="content">
                            <p>
                                Problema de Negócio: <br>
                                Usando dados históricos das vendas ao longo de 2023 
                                seria possível prever o total de vendas em Janeiro/2024?
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/series-temporais/tree/main" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Predição com Scikit-Learn</p>
                        </div>
                        <div class="content">
                            <p>
                                Problema de Negócio: <br>
                                Usando dados históricos é possível prever o salário de alguém 
                                com base no tempo dedicado aos estudos em horas por mês?
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/scikit-learn" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Análise Exploratória de Dados</p>
                        </div>
                        <div class="content">
                            <p>
                                Respondendo 10 perguntas de negócio a partir de 
                                um dataset sobre uma rede de varejo que comercializa 
                                diversos produtos em diversas cidades dos EUA.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/analise-exploratoria" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Análise Estatística com Statsmodels</p>
                        </div>
                        <div class="content">
                            <p>
                                Problema de Negócio: <br>
                                Existe alguma relação entre a área de imóveis (em metros quadrados) 
                                e o valor do aluguel em uma determinada cidade? 
                                Caso exista relação, como podemos mensurá-la?
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/statistical-analysis" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Análise de Dados com Pandas e SQLite</p>
                        </div>
                        <div class="content">
                            <p>
                                SQLite é um banco de dados incorporado, e Pandas é uma biblioteca em 
                                Python para manipulação de dados, sendo comum utilizar
                                o SQLite para armazenar e acessar dados manipulados pelo Pandas.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/python-sql-data-analysis" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Jogo da Forca em Python</p>
                        </div>
                        <div class="content">
                            <p>
                                Jogo da forca em Python usando loops e condicionais para desafiar 
                                os jogadores a adivinharem uma palavra secreta.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/jogo-da-forca" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Web Scraping com BeautifulSoup</p>
                        </div>
                        <div class="content">
                            <p>
                                O BeautifulSoup é uma biblioteca em Python que facilita a extração de informações 
                                de documentos HTML e XML, tornando mais fácil a navegação e manipulação desses 
                                dados durante o processo de web scraping.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/atividade-py" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Dashboard em Python</p>
                        </div>
                        <div class="content">
                            <p>
                                Dashboard produzido com informações abrangentes sobre a
                                distribuição e administração de doses de vacinas contra a 
                                COVID-19 nos Estados Unidos.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/dashboard-covid19" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Análise de Músicas Spotify</p>
                        </div>
                        <div class="content">
                            <p>
                                Análise e visualização de dados de uma Playlist do Spotify com Pandas e Matplotlib.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/music-analysis" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Exercícios em Python</p>
                        </div>
                        <div class="content">
                            <p>
                                Resolução de exercícios básicos em Python.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/lista_exercicios" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Sistema Bancário I em Pyhton</p>
                        </div>
                        <div class="content">
                            <p>
                                Sistema bancário com as operações: sacar, depositar e visualizar extrato.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/sistema-bancario-1" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading">Sistema Bancário II em Pyhton</p>
                        </div>
                        <div class="content">
                            <p>
                                Sistema bancário com as funções: sacar, depositar, 
                                visualizar extrato, cadastrar usuário (cliente) e cadastrar conta bancária.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/sistema-bancario-2" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading"> Jogo Simples do Mario Bros </p>
                        </div>
                        <div class="content">
                            <p>
                                Jogo simples usando apenas HTML, CSS e JavaScript. 
                                Onde é possível pular obstáculos e termina quando você colide com algum obstáculo.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/mario-bros" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading"> Campo Minado em React Native </p>
                        </div>
                        <div class="content">
                            <p>
                                Jogo "Campo Minado" desenvolvido com a linguagem JavaScript e o framework React Native.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/campo-minado" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading"> Sistema de Biblioteca Escolar em C# </p>
                        </div>
                        <div class="content">
                            <p>
                                Para o desenvolvimento do sistema foi utilizado a linguagem C# com a 
                                estrutura de interface Windows Forms no Visual Studio. O banco de dados foi 
                                realizado com MySQL.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/biblioteca-escolar" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading"> Sistema Gerenciador de Contatos da Empresa - Java Web </p>
                        </div>
                        <div class="content">
                            <p>
                                Sistema Gerenciador de Contatos da Empresa desenvolvido 
                                em Java Web com operações CRUD. Bancos de Dados feito em MySql.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/Sistema_Gerenciador" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading"> Sistema de Registro de Funcionários - Php </p>
                        </div>
                        <div class="content">
                            <p>
                                Sistema com operações CRUD para registro de funcionários desenvolvido em PHP.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/system-employees" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading"> Flexbox CSS </p>
                        </div>
                        <div class="content">
                            <p>
                                Página web com flexbox CSS.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/flexboxCSS" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
                <div class="card-container">
                    <div class="card">
                        <div class="front-content">
                            <p class="heading"> Exercício de Vetor em C# </p>
                        </div>
                        <div class="content">
                            <p>
                                Algoritmo em C# que calcula a média de 10 alunos a partir de duas notas.
                            </p>
                        </div>
                    </div>
                    <button class="cta">
                        <a href="https://github.com/thaisgarcia/Exercicio_vetor_CSharp" target="_blank">
                            <span class="hover-underline-animation"> Ver código </span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>
                            </svg>
                        </a>
                    </button>
                </div>
            </div>
            """, unsafe_allow_html=True)
