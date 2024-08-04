<h1 align="center"> kabarakNLP - Advancing our African NLP</h1>

[![Release Notes](https://img.shields.io/github/release/kabarakNLP/kabarakNLP/)](https://github.com/kabarakNLP/kabarakNLP/releases)
[![Discord](https://img.shields.io/discord/1087698854775881778?label=Discord&logo=discord)](https://discord.gg/)
[![Twitter Follow](https://img.shields.io/twitter/follow/kabarakNLP/?style=social)](https://twitter.com/kabarakNLP/)
[![GitHub star chart](https://img.shields.io/github/stars/kabarakNLP/kabarakNLP/?style=social)](https://star-history.com/#kabarakNLP/kabarakNLP/)
[![GitHub fork](https://img.shields.io/github/forks/kabarakNLP/kabarakNLP/?style=social)](https://github.com/kabarakNLP/kabarakNLP/fork)

English | [中文](./i18n/README-ZH.md) |  Swahili(./i18n/README-SW.md)


![image](https://github.com/user-attachments/assets/e4791a1d-ac55-404a-a304-470f8898b95a)

<h3> KabarakNLP is an initiative at Kabarak University dedicated to exploring Natural Language Processing (NLP). We aim to create a vibrant community for those interested in learning about NLP, collaborating on projects, and staying updated on the latest advancements in the field</h3>

<p align="left"> <img src="https://komarev.com/ghpvc/?username=KabarakNLP&label=Profile%20views&color=0e75b6&style=flat" alt="kabarakNLP" /> </p>

<p align="left"> <a href="https://twitter.com/kabarakNLP" target="blank"><img src="https://img.shields.io/twitter/follow/kabarakNLP" alt="kabarakNLP" /></a> </p>


## ⚡Quick Start

Download and Install [Pyton](https://python.org) >= 3.10

1. Clone the repository

    ```bash
    git clone https://github.com/kabarakNLP/kabarakNLP.git
    ```

2. Go into repository folder

    ```bash
    cd kabarakNLP
    ```
3. Create virtual environment
    ```bash
    python -m venv venv

    ```
4. Activate Virtual Environment
    Ubuntu
   
    ```bash
     source venv/bin/activate
    
    ```

    Windows

    ```bash
    source venv/lib/activate
    ```

5. Install requirementst. In the project root directory, locate the 'requirements.txt' file.

   ```bash
   pip install -r requirements.txt
   
   ```
   
6. Create a '.env' file and add your variables.

    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=your@gmail.com
    EMAIL_HOST_PASSWORD=*** sethostpassword ***
    EMAIL_USE_TLS=True

7. Makemigrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
8. Run Server

   ```
   python manage.py runserver
   
   ```
   
9. Open [http://localhost:8000](http://localhost:8000) or [http://127.0.0.1:8000](http://127.0.0.1:8000)

