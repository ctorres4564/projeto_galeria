# 🖼️ Projeto Galeria

Este é um projeto desenvolvido com Django que simula uma **galeria de imagens**, com o objetivo de praticar os conceitos fundamentais de back-end, templates, rotas, views e estrutura de aplicações web em Python.

---

## 🚀 Funcionalidades

- Listagem de imagens cadastradas
- Organização por templates com Django
- Navegação simples com base em views
- Estrutura de projeto com app modularizado (`galeria`)

---

## 🛠️ Tecnologias utilizadas

- Python 3.11+
- Django 4.x
- HTML5 + Django Templates
- SQLite3 (banco de dados padrão do Django)

---

## 📂 Estrutura do Projeto

```

projeto\_galeria/
├── galeria/               # App principal
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── galeria/
│   │       └── home.html
│   └── urls.py
├── projeto\_galeria/       # Configurações globais
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md

````

---

## 📦 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/ctorres4564/projeto_galeria.git
cd projeto_galeria
````

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> **Observação:** se você ainda não criou o `requirements.txt`, rode:
>
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Aplique as migrações

```bash
python manage.py migrate
```

### 5. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` no navegador para visualizar a galeria.

---

## 🔗 Possível Deploy com PythonAnywhere ou Render

Você pode publicar o projeto gratuitamente em plataformas como:

* [PythonAnywhere](https://www.pythonanywhere.com/)
* [Render](https://render.com/)

---

## 📸 Captura de Tela *(opcional)*

> Adicione aqui uma imagem da galeria funcionando.

```markdown
![Preview do projeto](screenshot.png)
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por Cláudio Torres
GitHub: [@ctorres4564](https://github.com/ctorres4564)


