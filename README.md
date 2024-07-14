# İHA KİRALAMA

## Giriş
Bu proje, kullanıcıların öncelikle üyelik ve giriş işlemlerini yapmasına, yeni iha(product) oluşturma, listeleme, silme, güncelleme, kiralama işlemlerini yapmalarını sağlamak için geliştirilmiştir. 

## Özellikler
- Kullanıcı kayıt ve giriş sistemi
- Ürün listeleme ve arama, yeni ürün oluşturma
- Ürün kiralama ve listelenmesi

## Kullanılan Teknolojiler
- Django
- PostgreSQL
- Docker
- DRF
- Boostrap


## Kurulum

### Gereksinimler
- Python 3.8+
- Docker
- Django
- Diğer geereksinimler requirements.txt içerisinde belirtilmiştir

### Adım Adım Kurulum
1. Depoyu klonlayın:
   ```sh
   git clone https://github.com/kullanici/proje.git
   cd proje

2. Sanal ortamı oluşturun ve bağımlılıkları yükleyin:
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

3. Veritabanını oluşturun ve migrate işlemini gerçekleştirin:
python manage.py migrate

4. Geliştirme sunucusunu başlatın:
python manage.py runserver

5. Projeyi 2,3,4 adımlarını atlayarak Docker üzerinden ayağa kaldırabilirsiniz. Migration işlemleri docker üzerinde yapılmaktadır.
docker-compose up --build

## Proje Ekran Görüntüleri
### Kayıt Ol
![register](https://github.com/user-attachments/assets/ac8516fb-62d4-4814-a93d-75cbcf135103)
### Giriş Yap
![login](https://github.com/user-attachments/assets/8f2c1491-5982-4e89-8f45-0af0bf0606f3)
### Ana Sayfa
![dashboard](https://github.com/user-attachments/assets/ace24946-2808-47ce-8311-3ff7fc063a77)
### IHA Ekleme
![addProduct](https://github.com/user-attachments/assets/c78c2418-f857-4144-af90-2abb6fcda5ab)
### IHA Listeleme
![productList](https://github.com/user-attachments/assets/60d34729-cc70-4e50-adab-4dcc21c0ecb0)
### IHA Güncelleme
![productUpdate](https://github.com/user-attachments/assets/16a0192d-0741-49f6-b47f-7f6c609f427d)
### Kiralama Listeleme
![rentList](https://github.com/user-attachments/assets/6c6a04ca-582a-4fa0-9af5-0239b343d5c3)
### Kiralama Güncelleme
![rentUpdate](https://github.com/user-attachments/assets/38d443c8-a0c7-4c27-ad86-986d5d9b4e36)
