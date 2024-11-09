# Membuat Aplikasi Web 'TORANGBISAAPA' Menggunakan Django Versi 5


## 1. SETUP

#### 1. Mengklon starter proyek 'Halo Dunia'

        new file:   .env.example
        new file:   .gitignore
        new file:   README.md
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   requirements.txt


## 2. PAGES

#### 1. Membuat laman home

        # Membuat folder dan file
        (venv312512) λ mkdir templates\main
        (venv312512) λ touch templates\main\index.html

        modified:   README.md
        new file:   app/main/urls.py
        modified:   app/main/views.py
        modified:   config/urls.py
        new file:   templates/main/index.html

#### 2. Membuat laman about

        modified:   README.md
        modified:   app/main/urls.py
        modified:   app/main/views.py
        new file:   templates/main/about.html

#### 3. Membuat navigasi

        modified:   README.md
        modified:   app/main/urls.py
        modified:   templates/main/about.html
        modified:   templates/main/index.html