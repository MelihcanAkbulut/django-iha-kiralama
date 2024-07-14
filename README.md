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