# Blog Uygulaması

Bu proje, kullanıcıların blog yazıları ekleyebildiği, blogları kategorilere göre filtreleyebildiği ve yorum yapabildiği bir Django tabanlı blog uygulamasıdır.

## Özellikler

- Kullanıcı kaydı ve kullanıcı giriş işlemleri.
- Blog yazısı oluşturma, düzenleme ve onay gereksinimi.
- Admin panelinden blog ve kullanıcı yönetimi.
- Zengin metin düzenleme (CKEditor entegrasyonu).
- Blog kategorileriyle filtreleme.
- Yorum ekleme ve yorumların yönetimi.

### Gereksinimler

- Python 3.x
- Django 3.x veya üstü
- Diğer bağımlılıkları yüklemek için `requirements.txt` dosyasını kullanabilirsiniz.

## Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edin.

### Adımlar

1. **Projeyi Klonlayın:**

      ```bash
      git clone https://github.com/Ataberk696/django_blogapp
      cd blog-projesi
      ```
      
2. **Sanal Ortam Oluşturun ve Aktif Edin:**
   
     ```bash
     python -m venv venv
     source venv/bin/activate  # MacOS/Linux
     .\venv\Scripts\activate  # Windows,
     ```

3. **Bağımlılıkları Yükleyin ve Ortam Değişkenlerini Ayarlayın:**

     ```bash
     pip install -r requirements.txt
     cp .env.example .env
     ```

    Ardından, .env dosyasındaki SECRET_KEY değerini kendi ortamınıza uygun şekilde düzenleyin.

4. **Veritabanını Oluşturun ve Migrasyonları Çalıştırın:**

      ```bash
      python manage.py migrate
      ```

5. **Admin Paneli için Süper Kullanıcı Oluşturun:**

      ```bash
      python manage.py createsuperuser
      ```
 
6. **Uygulamayı Başlatın:**

     ```bash
      python manage.py runserver
      ```



Projeye katkıda bulunmak isteyenler, lütfen pull request gönderin veya issue açın. Katkılarınız için şimdiden teşekkürler. 


