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


## 3. TEMPLATE INHERITANCE

#### 1. Membuat base template

        (venv312512) λ touch templates\base.html

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/main/about.html
        modified:   templates/main/index.html

#### 2. Menggunakan block super

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/main/about.html
        modified:   templates/main/index.html

        Note:
        https://dev.to/serhatteker/django-template-block-super-12o4

        It's basically the same concept for super in any OOP; you call the
        constructor of the parent class to include whatever code is in there, instead of just overriding it.


## 4. FILE STATIS DAN MEDIA

#### 1. Menggunakan file statis 'css'

        (venv312512) λ mkdir static\assets\css
        (venv312512) λ touch static\assets\css\test.css

        modified:   README.md
        new file:   static/assets/css/test.css
        modified:   templates/base.html
        modified:   templates/main/about.html
        modified:   templates/main/index.html

#### 2. Menggunakan file media 'images'

        modified:   README.md
        new file:   static/assets/images/test_image.png
        modified:   templates/main/index.html