﻿# GeneraFted by Django 4.1.2 on 2023-04-29 03:39

from django.db import migrations

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from datetime import datetime, timedelta
import time

def beginning(apps, schema_editor):
    
    # Суперпользователь id-1
    user = User.objects.create_superuser(username='root',
    email='travel_alem_pvl@mail.ru',
    password='SsNn5678+-@', 
    last_login=datetime.now())
    print("Суперпользователь создан")
    
    # Группа менеджеров
    managers = Group.objects.get_or_create(name = 'Managers')
    managers = Group.objects.get(name='Managers')
    print("Группа менеджеров создана")
    
    # Пользователь с ролью менеджера id2
    user = User.objects.create_user(username='manager', password='Ss0066+-', email='manager@mail.ru', first_name='Менеджер', last_name='', last_login=datetime.now())
    managers.user_set.add(user)
    print("Менеджер добавлен в группу менеджеров")

    # Простые пользователи (заявители) id3-27
    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Дина', last_name='Мусина', last_login=datetime.now())
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Адия', last_name='Жунусова', last_login=datetime.now())
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Айнура', last_name='Кенина', last_login=datetime.now())
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Рустем', last_name='Какимов', last_login=datetime.now())
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Алишер', last_name='Кабдуалиев', last_login=datetime.now())
    user = User.objects.create_user(username='user6', password='Uu0066+-', email='user6@mail.ru', first_name='Бауржан', last_name='Арыкбаев', last_login=datetime.now())
    user = User.objects.create_user(username='user7', password='Uu0066+-', email='user7@mail.ru', first_name='Алишер', last_name='Танатаров', last_login=datetime.now())
    user = User.objects.create_user(username='user8', password='Uu0066+-', email='user8@mail.ru', first_name='Мерует', last_name='Искакова', last_login=datetime.now())
    user = User.objects.create_user(username='user9', password='Uu0066+-', email='user9@mail.ru', first_name='Ольга', last_name='Муравьева', last_login=datetime.now())
    user = User.objects.create_user(username='user10', password='Uu0066+-', email='user10@mail.ru', first_name='Ақжарқын', last_name='Сансызбаева', last_login=datetime.now())
    user = User.objects.create_user(username='user11', password='Uu0066+-', email='user11@mail.ru', first_name='Арайлым', last_name='Алматова', last_login=datetime.now())
    user = User.objects.create_user(username='user12', password='Uu0066+-', email='user12@mail.ru', first_name='Айгерім', last_name='Дүйсенбиева', last_login=datetime.now())
    user = User.objects.create_user(username='user13', password='Uu0066+-', email='user13@mail.ru', first_name='Салтанат', last_name='Зиноллаева', last_login=datetime.now())
    user = User.objects.create_user(username='user14', password='Uu0066+-', email='user14@mail.ru', first_name='Сейтқасым', last_name='Болат', last_login=datetime.now())
    user = User.objects.create_user(username='user15', password='Uu0066+-', email='user15@mail.ru', first_name='Сара', last_name='Фазилова', last_login=datetime.now())
    user = User.objects.create_user(username='user16', password='Uu0066+-', email='user16@mail.ru', first_name='Бектас', last_name='Ерсейіт', last_login=datetime.now())
    user = User.objects.create_user(username='user17', password='Uu0066+-', email='user17@mail.ru', first_name='Диас', last_name='Мырзаш', last_login=datetime.now())
    user = User.objects.create_user(username='user18', password='Uu0066+-', email='user18@mail.ru', first_name='Нұржан', last_name='Жүрсінбек', last_login=datetime.now())
    user = User.objects.create_user(username='user19', password='Uu0066+-', email='user19@mail.ru', first_name='Дина', last_name='Жағыпар', last_login=datetime.now())
    user = User.objects.create_user(username='user20', password='Uu0066+-', email='user20@mail.ru', first_name='Жастілек', last_name='Жасталап', last_login=datetime.now())
    user = User.objects.create_user(username='user21', password='Uu0066+-', email='user21@mail.ru', first_name='Еркебұлан', last_name='Қадыхан', last_login=datetime.now())
    user = User.objects.create_user(username='user22', password='Uu0066+-', email='user22@mail.ru', first_name='Молдир', last_name='Бутабекова', last_login=datetime.now())
    user = User.objects.create_user(username='user23', password='Uu0066+-', email='user23@mail.ru', first_name='Аружан', last_name='Таурбекова', last_login=datetime.now())
    user = User.objects.create_user(username='user24', password='Uu0066+-', email='user24@mail.ru', first_name='Алтынай', last_name='Қожанова', last_login=datetime.now())
    user = User.objects.create_user(username='user25', password='Uu0066+-', email='user25@mail.ru', first_name='Эльнара', last_name='Иминова', last_login=datetime.now())
    print("Созданы простые пользователи")

    ###### Страны / регионы / отели / заявки / отзывы #####

    Country = apps.get_model("kaz", "Country")
    Region = apps.get_model("kaz", "Region")
    Hotel = apps.get_model("kaz", "Hotel")
    Claim = apps.get_model("kaz", "Claim") 
    Reviews = apps.get_model("kaz", "Reviews") 

    country = Country()
    country.title = 'Турция'   
    country.details = 'Турция - это страна, соединяющая Европу с Ближним Востоком. Достаточно не простая роль в истории выпала на долю Турции. На этой земле проходило большое число войн, что сопровождалось сменой местного населения. На территории Турции распологается более двух тыс. древних поселений. Примерно 10 тыс. лет назад началась история народов Турции. Немаловажную роль сыграли греки, которые заняли эту землю в XIV-XII веках до н.э., самым главным их вкладом было развитие торговли и мореплавания. Позже на земле Турции существовало множество колоний, а в VIII веке до н. э. сюда пришли фригийцы и ливийцы. Начина с VI века до н. э., после множественных набегов, стали править персы. Сегодня же отдых в Турции занимает лидирующую позицию среди туристических направлений…'   
    country.photo = 'images/country1.jpg' 
    country.save()

    region = Region()
    region.country=country;
    region.title = 'Анталия' 
    region.details = 'Анталия – крупный исторический и культурный центр Турции. Отдых в Анталии - один из самых лучших выборов для тех, кто любит солнце, море и веселье! Здесь прекрасные пляжи и уютные отели. Городу есть, что предложить пытливому туристу. Анталия ждет Вас!'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'BODENSEE HOTEL 3*' 
    hotel.details ='Отель Bodensee расположен в 3 км от центра г. Анталия, в р-не Коньяалты, в 80 м от берега Средиземного моря. Этот по-домашнему уютный пятиэтажный отель, построенный в 1994 г и реконструированный в 2004 г, обеспечивает туристам хороший расслабляющий отдых.'
    hotel.photo  = 'images/hotel1.jpg'
    hotel.price = 371278
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=45)
    claim.user_id = 3
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=45);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 4
    reviews.details = 'Были вдвоём с мужем 2 недели в августе 2021 по переброни тура из-за ковида. Брали завтраки. Тур обошёлся в 70 т.р. За такие деньги мы остались довольны. Море рядом, чистейшее, променад-набережная-кафе все рядом. В номерах нет чайника, чашек, холодильника и фена. ТВ и кондей работали без претензий. Мыльные только при заезде. Берите с собой! Бумага туалетная была всегда. Меняли и постель, и полотенца, но не ежедневно. Мусор тоже выносили, но иногда мы сами забирали и выкидывали по пути на пляж в контейнер. Убирались норм. Завтраки турецкие, однообразные. '
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=45);
    claim.user_id = 10
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=45);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Тихий красивый семейный отель, с бассейном, балконом, завтраки,2 минуты до моря, лучшее расположение относительно общественного транспора и в целом набережной, кафе и тд. Балкон напомнил заставку к сериалу Санта барбара))) Соотношение цена -качество данный отель для нас оказался на первом месте (были в трех). Отдельное спасибо персоналу за отзывчивость и помощь в решении всех вопросов, жаль, что не удалось вернуться в ходе этого путешествия, надеюсь в следующем'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'CITRUS PARK HOTEL 4**' 
    hotel.details ='Отель Citrus Park расположен в городе Анталья, в 2,5 км от пляжа Коньяалты. К услугам гостей сад, бесплатная частная парковка, общий лаундж и терраса. Отель находится в 1,5 км от торгового центра 5M Migros и в 1,2 км от океанариума Антальи. При отеле работают ресторан и бар. В числе прочих удобств — круглосуточная стойка регистрации и пункт обмена валюты.'
    hotel.photo  = 'images/hotel2.jpg'
    hotel.price = 460334
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=45);
    claim.user_id = 11
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=45);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Очень понравился отель.В начале ноября прилетели в Анталью,по совету знакомых поселились в городской,небольшой отель Цитрус. Были приятно удивлены чистотой,стильным интерьером,тишиной.Девушка русскоговорящая на ресепшен очень приветливая,всегда поможет,расскажет и покажет.Просто умница,спасибо ей огромное.Пляж в 2 минутах ходьбы,вокруг много кафе,баров,ресторанов.Такси можно вызывать с ресепшен,там кнопка.2 минуты и подъезжает машина.Расположение у отеля очень хорошее,все в шаговой доступности.С погодой повезло,накупались ,назагорались.Мы теперь обязательно будем постоянными гостями этого небольшого,но очень полюбившегося нам отельчика'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'OZKAYMAK FALEZ HOTEL 5*' 
    hotel.details ='К услугам гостей отеля Ozkaymak Falez 2 открытых бассейна, детский бассейн, крытый бассейн и водная горка. В отеле есть спа-центр и 4 теннисных корта. В 200 метрах находится частный пляж отеля Ozkaymak, до которого предоставляется трансфер.В номерах отеля Ozkaymak Falez имеется телевизор с плоским экраном и спутниковыми каналами, кондиционер и мини-бар. Во всех номерах есть балкон или терраса с видом на город, сад, пейзажи или бассейн. Кроме того, из некоторых номеров открывается вид на море.'
    hotel.photo  = 'images/hotel3.jpg'
    hotel.price = 533324
    hotel.save()
    
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=40);
    claim.user_id = 12
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=40);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish ;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 4
    reviews.details = 'Отель был хорошей 5-ой лет 30 назад( хотя ему 24 года 😀) . За это время он конечно устал. Отель Для путешественников или по делам с ночевкой на 1-2 ночи соотношение цена/качество это самое ТО-5 баллов: Есть большая собственная парковка, Локация хорошая, голодным не останешься . Вай фай 4 балла. НО для ОТДЫХА мне бы точно не подошло! Питание сильно хромает 3 балла. Г'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    region = Region()
    region.country=country;
    region.title = 'Белек' 
    region.details = 'Всего в 40 км от Анталии расположен курорт Белек - Турция, он считается одним из самых часто посещаемых мест туристами разных национальностей. Дорога от аэропорта до Белека занимает всего 45 минут. В Белеке на территории огромного просторного пляжа находятся уютные, наполненные зеленью отели и гостиничные комплексы, в основном с уровнем 5 звезд.'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'PRENSES SEALINE BEACH HOTEL 4*' 
    hotel.details ='Отель Prenses Sealine Beach расположен в городе Серик. К услугам гостей бар, ресторан, сад и сезонный открытый бассейн. Гости могут посетить сауну и взять напрокат велосипед. В отеле работает хаммам и круглосуточная стойка регистрации.Каждое утро в отеле сервируют завтрак «шведский стол».'
    hotel.photo  = 'images/hotel4.jpg'
    hotel.price = 422174
    hotel.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'DIONISUS HOTEL (EX. WHITE ANGEL HOTEL) 4*' 
    hotel.details ='Отель Dionisus Belek расположен в городе Белек, в 1,3 км от парка аттракционов «Земля легенд». К услугам гостей — ресторан, бесплатная частная парковка, открытый бассейн и бар. Он находится в 23 км от амфитеатра Аспендос и в 27 км от водопада и природного парка Куршунлу. К услугам гостей — сад и частная пляжная зона. Стойка регистрации работает круглосуточно. Осуществляется доставка еды и напитков в номер. Гости могут обменять валюту на месте.'
    hotel.photo  = 'images/hotel5.jpg'
    hotel.price = 428582
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=40);
    claim.user_id = 4
    claim.hotel = hotel
    claim.start  = datetime.now() - timedelta(days=25);
    claim.finish  = datetime.now() - timedelta(days=18);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=40);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Очень гостеприимно приняли. Персонал очень вежливый! По любому Вопросу помогали, подскакивали как правильно доехать , куда лучше сходить! Хозяин гостиницы очень приятный человек!!! В рицепшене молодые ребята приятные, дружеские! управляющий Юсуф очень хорошо владеет Руский языком. Гостили неделю . В номерах чисто! Постельное бельё чистое. В ванной чисто, все туалетные принадлежности на месте. Очень довольные . 10баллов! Рекамендую!!!'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()
        
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=40);
    claim.user_id = 13
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=40);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 4
    reviews.details = 'Отель в целом нормально, но больше не поедем. Есть большой бассейн и маленький для детей, номера, как повезёт. Еды хватает, из алкоголя только пиво, водка и сухое вино. Сладостей почти нет. Из фруктов арбузы вкусные, сливы, иногда дыня, но не вкусная.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'GREENMAX HOTEL 5*' 
    hotel.details ='Отель находится в курортном поселке Кадрие, в 7 км от центра г.Белек и в 25 км от международного аэропорта г.Анталия.'
    hotel.photo  = 'images/hotel6.jpg'
    hotel.price = 453988
    hotel.save()
        
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=35);
    claim.user_id = 14
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=35);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Хороший отель, питание разнообразное, отзывчивый персонал. Пляж хороший, лежаков много. Отдыхали в последнюю неделю октября - погода отличная, купаться можно, солнце не жарит.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    region = Region()
    region.country=country;
    region.title = 'Алания' 
    region.details = 'Алания – входит в число самых популярных курортов в Турции среди туристов. Если вы желаете провести свое свободное время во время отпуска с пользой для здоровья, обращайтесь к нам, и мы поможем вам воплотить вашу мечту в реальность в самые сжатые сроки. Потому что забота о клиентах нашей туристической организации стоит на первом месте, в связи с чем, обратившись к нам, вы полностью лишаете себя переживаний по предстоящему отпуску, так как все нюансы оформления и формирования туристического маршрута мы берем на себя.'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'SEMT LUNA BEACH 3*' 
    hotel.details ='Отель расположен в районе Тосмур, в 6 км от центра г.Алания. Аэропорт г.Анталия находится в 120 км от отеля, аэропорт Газипаша в 30 км. Рядом стоящие отели: Saritas, Club Bayar.'
    hotel.photo  = 'images/hotel7.jpg'
    hotel.price = 366850
    hotel.save()
    
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=35);
    claim.user_id = 14
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=35);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish ;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 3
    reviews.details = 'Плохое питание,дают одни сосиски на завтрак напичканные соей,нет ни рыбы,ни мяса,никакого разнообразия напитков в баре,нет даже пива'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'BIN BILLA HOTEL 4*' 
    hotel.details ='Отель BIN BILLA расположен в Алании. К услугам гостей ресторан, бар, сезонный открытый бассейн и общий лаундж. Из всех номеров этого 3-звездочного отеля открывается вид на сад. Гости могут погулять в саду и позагорать на частном пляже. В числе прочих удобств — круглосуточная стойка регистрации и пункт обмена валюты. Осуществляется доставка еды и напитков в номер.'
    hotel.photo  = 'images/hotel8.jpg'
    hotel.price = 385560
    hotel.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'KLAS MORE BEACH HOTEL 5*' 
    hotel.details ='Расположение: на берегу моря, недалеко от поселка Мамутлар, в 100 км от аэропорта Анталья.'
    hotel.photo  = 'images/hotel9.jpg'
    hotel.price = 385560
    hotel.save()
    
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=35);
    claim.user_id = 5
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=35);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 3
    reviews.details = 'Я останавливался на две ночи в этом отеле, они взяли оплату дважды. первый раз заплатила 60$ за сутки при бронировании, после дня проживания потребовали заплатить 100€ за сутки и сразу взяли на двое суток. на ресепшн девушка просто нахамила, когда я заплатила 8 евро за вай-фай, а интернета не было вообще. пляж через дорогу, но никто не купается, можно только загорать, под водой у берега лежат каменные плиты, можно ноги сломать, а пальцы все травмированы от этих плит. Туалет и душ были просто сломаны и не работали. не рекомендую, пустая трата денег.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=35);
    claim.user_id = 15
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=35);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Большой плюс .что отель находится в центре города и с одной стороны вы ходил на улицу Барборосса.а с другой на море. Прилетели утром .мы усрели на завтрак.а потом море..заселение в 2 часа.не давали ни каких чаевых нас заселили в номер.в главном корпусе.номер чистый.вме работало.постель меняли..мы брали в соседнем магазинчике пледы для моря и вам советуем.пока купаетесь онт почти высыхают. По еде.Ребята если вам нужны лангусты то это не сюда и не за эту цену.А так то вы голодными не будете.мясо.рыба.гарниры.много фруктов.выпечка...нам всего хватало(и я в Турции была даже не в 10 раз и была в разных отелях).'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    country = Country()
    country.title = 'Египет'   
    country.details = 'Египет – это удивительная страна, окутанная тайнами древнего мира. Вряд ли найдётся человек, который увидев загадочные пирамиды или прекрасные коралловые сады Красного моря, не будет восхищён. Отправившись в путешествие по Египту, Вы сможете собственными руками прикоснуться к тысячелетним гробницам фараонов, правивших Верхним и Нижним Египтом, посетить титанические руины, храмы Корнака и Луксора, а также прикупить древние и необычные вещицы.'   
    country.photo = 'images/country2.jpg' 
    country.save()
    
    region = Region()
    region.country=country;
    region.title = 'Шарм Эль Шейх' 
    region.details = 'Туры в Египет на курорт Шарм Эль Шейх сегодня пользуются популярностью благодаря сравнительно недорогой цене. Вместо обычного города здесь находятся множество хороших отелей. В Шарм Эль Шейх предоставляют все виды туристических услуг, можно даже найти горящие туры. Большое количество ресторанов предлагают самую разнообразную кухню.'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'UNI SHARM AQUA PARK 3*' 
    hotel.details ='Отель расположен в живописной части Синайского полуострова, с пустынным ландшафтом с одной стороны, и с морем, полным кораллов с другой.'
    hotel.photo  = 'images/hotel10.jpg'
    hotel.price = 535147
    hotel.save()
    
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 6
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 4
    reviews.details = 'Недавно я имел удовольствие остановиться в замечательном отеле, и я не могу рекомендовать его достаточно высоко! Сам отель был красивым и ухоженным, но что действительно выделялось, так это ежедневное предложение местной выпечки - она была очень вкусной и стала настоящей изюминкой моего пребывания. Хотя было немного неудобно, что в номерах не было Wi-Fi, дружелюбный и гостеприимный персонал более чем компенсировал это своим исключительным обслуживанием. В целом, у меня было невероятно приятное впечатление, и я очень рекомендую этот отель всем, кто ищет незабываемый и комфортный отдых. Спасибо персоналу за то, что сделали мое пребывание таким приятным!'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 16
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 4
    reviews.details = 'Хороший отель для спокойного отдыха. Свои заезды отрабатывает. Удобное расположение: хотя и вторая линия, но до пляжа можно дойти пешком за 40 минут, рядом пешеходная улица, отличный спа-салон (работают девочки из Белоруссии), в 15 минутах - старый город, а там рынок. В самом отеле тоже есть массажист, имя не помню, за 50$ сделали 8 раз по часу. Довольны! Но в спа-салоне брали программу за 40$ , понравилось больше. Белье белое, полотенца каждый день в номере меняют, у бассейна - хоть 3 раза в день. Из фруктов, правда, апельсины только, но мы были в октябре, может, в другое время по-другому'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'OLD VIC RESORT SHARM 4*' 
    hotel.details ='Курортный отель Old Vic Sharm расположен в Шарм-эль-Шейхе, в 5 км от залива Нима-Бей. К услугам гостей открытый бассейн, работающий круглый год, принадлежности для барбекю, терраса, спа-центр, ресторан, бесплатный Wi-Fi и бесплатная частная парковка на территории. Все номера оснащены кондиционером и телевизором с плоским экраном и спутниковыми каналами. В некоторых из них есть гостиная зона. В числе удобств — чайник. В собственной ванной комнате каждого номера установлена ванна или душ. Предоставляются халаты, тапочки и фен. Стойка регистрации открыта круглосуточно. В отеле работают магазины.'
    hotel.photo  = 'images/hotel11.jpg'
    hotel.price = 536061
    hotel.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'PARROTEL LAGOON RESORT 5*' 
    hotel.details ='Курортный отель Parrotel Lagoon расположен в городе Шарм-эш-Шейх. К услугам гостей фитнес-центр, бар, сад и собственный пляж. Стойка регистрации открыта круглосуточно. На территории работает ресторан и аквапарк, оборудован открытый бассейн. В числе удобств сауна. По вечерам организуется развлекательная программа. Гости могут воспользоваться услугой доставки еды и напитков в номер.'
    hotel.photo  = 'images/hotel12.jpg'
    hotel.price = 552513
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 17
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Отличный отель, огромная зелёная и ухоженная территория, чистые бассейны. Очень услужливый и вежливый персонал, вкусная и разнообразная еда. Хорошая анимация. Номера убирают ежедневно, но без чаевых только для видимости), но за несколько долларов вам наведут восхитительную красоту и осыпят цветами! Выезд из отеля стандартно в 12:00, но при позднее вылете можно бесплатно продлить до 15:00. Номера огромные, чистые и комфортные.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()
    
    region = Region()
    region.country=country;
    region.title = 'Хургада' 
    region.details = 'Многие туристы выбирают для отдыха египетский курорт - Хургаду. Расположен этот туристический центр в 500 километрах от Каира на побережье Красного моря. В любое время года можно с комфортом отдохнуть на Хургаде. Здесь есть все, что нужно: яркое солнце, горы и бесконечные пляжи, прозрачная вода в лагунах, сильный ветер для серфинга.'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'SUN & SEA HURGHADA HOTEL 3*' 
    hotel.details ='В этом 4-звездочном курортном отеле с собственным пляжем на берегу Красного моря гостям предлагаются номера с кондиционером и телевизором со спутниковыми каналами. В числе удобств 2 открытых бассейна. На территории можно заняться водными видами спорта. Все номера курортного отеля Mercure Hurghada оснащены сейфом и мини-холодильником. В распоряжении гостей балкон или терраса с видом на Красное море или сад.'
    hotel.photo  = 'images/hotel13.jpg'
    hotel.price = 656314
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 18
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Уютный отель с видом на море. Через дорогу небольшой пляж. Отличное расположение. Приветливый персонал. Большой ресторан со шведским столом. Рядом с отелем магазины, аптека. Все есть для хорошего отдыха. Очень понравилось. Рекомендую для непритязательных путешественников. Единственное неудобство: слабый интернет и только на ресепшене. Но и без него неплохо'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'KING TUT AQUA PARK BEACH RESORT 4*' 
    hotel.details ='Курортный отель «все включено» King Tut находится всего в 5 км от аэропорта Хургады. К услугам гостей бесплатный Wi-Fi, большой бассейн и прямой выход к пляжу. Номера располагают отдельным балконом с видом на коралловые рифы.'
    hotel.photo  = 'images/hotel14.jpg'
    hotel.price = 613294
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=35);
    claim.user_id = 7
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Все понравилось, уютно, душевно, детям понравился виндсерфинг с инструктором, отличные работники ресепшена! Еда понравилась! Аквапарк! Отдельное спасибо Олесе, всегда помогала в различных ситуациях!!! Море и детям есть где поплавать и взрослым!'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 19
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Понравилось отношение персонала, с любым вопросом мы обращались к менеджеру. Огромное спасибо ему за радушие, помощь. Весь персонал прекрасно выполняет свою работу. Отличное расположение. Всё супер! Большая зелёная ухоженная территория, много цветов. У отеля свой пляж тут же с рифом, всегда в любое время много свободных лежаков, зонтов, выдают пляжные полотенца, работают спасатели. Вода теплая, прозрачная. На пляже есть бары, чтоб взять напитки, закуски. Есть магазинчики, чтоб купить и масла, и купальные принадлежности, одежду и т.д. Предлагают много интересных экскурсий.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'ZAHABIA HOTEL & BEACH RESORT 5*' 
    hotel.details ='Курортный отель Zahabia Hotel & Beach расположен в Хургаде. К услугам гостей — открытый бассейн, сад, терраса и ресторан. Расстояние до пляжа Парадайз — 1,6 км, а до пляжа Эль Саваки — 2,7 км. В распоряжении гостей частная пляжная зона и бар. В отеле осуществляется доставка еды и напитков в номер. Стойка регистрации работает круглосуточно.'
    hotel.photo  = 'images/hotel15.jpg'
    hotel.price = 600955
    hotel.save()

    country = Country()
    country.title = 'Тайланд'   
    country.details = 'Тайланд – это красивейшее место с экзотическими растениями и животными! Если Вы ещё не путешествовали по этой стране, обязательно обратите на неё внимание. Такие замечательные курорты как Паттайя, Пхукет, Нанг, Кванг и другие уже не первый год восхищают туристов со всего мира. Здесь проходят самые зажигательные тусовки и вечеринки в Азии. В Тайланд едут, чтобы повеселиться в современных ночных клубах, увидеть необычные храмы и посетить интересные экскурсии, заняться шопингом, отведать оригинальную кухню и узнать культуру тайского народа. Комфортабельные отели всегда рады предложить туристам отличный сервис и множество развлечений.'   
    country.photo = 'images/country3.jpg' 
    country.save()
    
    region = Region()
    region.country=country;
    region.title = 'Паттайя' 
    region.details = 'Паттайя - крупнейший и известный курорт Тайланда. Он располагается на берегу Сиамского залива, где -то в 140 км к юго-востоку от Банкока. Дорога от Паттайи до столицы Тайланда занимает 3 часа. Из аэропорта У-Тапао добраться до курорта можно всего за 40 минут.'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'JARDIN HOTEL 3*' 
    hotel.details ='Отель Jardin расположен в 50 метрах от пляжа в городе Паттайя Юг. К услугам гостей комфортабельные номера с кондиционером и бесплатным Wi-Fi. В каждом номере в распоряжении гостей балкон, телевизор, сейф, холодильник и электрический чайник. В собственной ванной комнате с душем предоставляются фен и бесплатные туалетно-косметические принадлежности.'
    hotel.photo  = 'images/hotel16.jpg'
    hotel.price = 503342
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=25);
    claim.user_id = 20
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=25);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 4
    reviews.details = 'Отдыхали в этой гостинице, удачное расположение минут 7 до моря магазины, рынок все рядом, тут же у них есть кафе там очень вкусно 😋 как русская так и тайская кухня можно заказать и в номер, номера не плохие, все уютно, единственное персонал убирается плохо как папало за 10 дней ни разу не поменяли постельное белье даже 👎 но каждый день приносят по бутылочки воды. Полностью соответствие цена качество.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'BESTON PATTAYA 4*' 
    hotel.details ='Отель Beston Pattaya расположен в нескольких минутах ходьбы от главной улицы Саут-Паттайя-роуд. К услугам гостей открытый бассейн и бесплатный Wi-Fi. Ближайший пляж и знаменитые ночные клубы на улице Уокинг-стрит находятся в 1,5 км от отеля. На общественном транспорте гости могут легко добраться до любого района города и близлежащих достопримечательностей. Поездка до Бангкока и международного аэропорта Суварнабхуми занимает примерно 1,5 часа.'
    hotel.photo  = 'images/hotel17.jpg'
    hotel.price = 524868
    hotel.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'DUSIT THANI PATTAYA 5*' 
    hotel.details ='Отель Dusit Thani Pattaya расположен у спокойного пляжа на берегу Сиамского залива. С территории открывается великолепный вид на море. В отеле работают 3 ресторана и 2 плавательных бассейна. Автомобиль можно оставить на бесплатной парковке. Отель Dusit Thani Pattaya находится в 7 км от Деревни слонов и в 9,5 км от плавучего рынка. Поездка на автомобиле до Бангкока занимает 1,5 часа. Номера Dusit Thani оформлены в современном тайском стиле. В числе удобств бесплатный Wi-Fi и телевизор с кабельными каналами. Из окон открывается вид на сад или море.'
    hotel.photo  = 'images/hotel18.jpg'
    hotel.price = 918113
    hotel.save()
    
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=25);
    claim.user_id = 8
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=25);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Прекрасный отель. Прекрасно всё: расположение -2 минуты и ты в центре. персонал, завтраки, пляж, большая ухоженная территория. Можно сказать, что отель чуть «подустал», но это в мелочах, а в целом, всё работает, полотенца ежедн меняют, персонал старается. Нам бесплатно сделали поздний выезд. мы очень довольны.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=25);
    claim.user_id = 21
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=25);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Данный отель один из лучших в Патиае. Причина- расположение. Через дорогу самый большой ТЦ . До центра пешком 10 минут и при этом полная тишина. Огромная территория с собственными 2 пляжами- где можно купаться!!!! Отличное питание- свежевыжатые соки, рыба, местная кухня и т.д. импортный алкоголь бесплатно 2 часа в день- безлимитный доступ для Лубного лаунджа. Не дёшево- но оно того стоит!!! А ещё рядом супер ресторан для ужина,'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    region = Region()
    region.country=country;
    region.title = 'Пхукет' 
    region.details = 'Пхукет - самый большой по территории остров Тайланда. Общая площадь острова — 543 кв.км, население составляет около триста тысяч человек. С материком Пхукет соединяется мостом-дамбой Сарасин. Раньше Пхукет славился добычей олова, потом — каучуковыми плантациями. Кроме того остров очень долгое время служил пристанью для различных судов, которые проходили по торговому пути между Китаем и Индией.'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = '7Q BANGLA HOTEL 3*' 
    hotel.details ='Отель 7Q Bangla с сертификатом SHA расположен на пляже Патонг. К услугам гостей открытый бассейн, общий лаундж, терраса и бар. В каждом номере этого 3-звездочного отеля с видом на город установлена гидромассажная ванна и телевизор с плоским экраном и спутниковыми каналами. К услугам гостей экскурсионное бюро, круглосуточная стойка регистрации, трансфер от/до аэропорта. На всей территории отеля действует бесплатный Wi-Fi.'
    hotel.photo  = 'images/hotel19.jpg'
    hotel.price = 485480
    hotel.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'FORTY WINKS PHUKET 4*' 
    hotel.details ='Отель Forty Winks Phuket располагается в 500 метрах от торгового центра Jungceylon. К услугам гостей номера с кондиционером и бесплатным Wi-Fi, открытый бассейн, круглосуточная стойка регистрации и туристическое бюро.'
    hotel.photo  = 'images/hotel20.jpg'
    hotel.price = 486854
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=25);
    claim.user_id = 22
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=25);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Номер очень хороший, чистый, стильный и вполне просторный. Завтраки средние, но пойдет. До пляжа минут 15-20, но зато мимо практически всех инфраструктурных мест Патонга. Бассейн небольшой, но в тему, чтобы окунуться, Вообще отель такой свеженький и уютный, в стиле лофт. Персонал милый.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'ANGSANA LAGUNA PHUKET 5*' 
    hotel.details ='Современный стильный тропический отель Angsana Laguna Phuket находится в живописном заливе Банг-Тао. К услугам гостей 323-метровый бассейн. Гости могут воспользоваться бесплатным трансфером на лодке до торгового комплекса Canal Village Boutiques & Galleries. В просторных номерах с неограниченным бесплатным Wi-Fi представлены абстрактные произведения искусства. Номера оформлены в современном тайском стиле. Во всех номерах имеются 40-дюймовый телевизор с плоским экраном, удобная кровать Sealy и роскошный выбор подушек. Гостям предоставляется бесплатная вода в бутылках.'
    hotel.photo  = 'images/hotel21.jpg'
    hotel.price = 684252
    hotel.save()

    country = Country()
    country.title = 'ОАЭ'   
    country.details = 'ОАЭ – это пустыни с цветущими садами, тёплые воды Персидского залива, шикарные отели и множество товаров в магазинах. Объединённые Арабские Эмираты – это возможность окунуться в восточную экзотику, увидеть живописные пейзажи, узнать культурные и национальные особенности интересной страны. Во времена кочевых племён богатства этих место заключалось лишь в золотых песках и лазурных водах. С приходом цивилизации и технического прогресса выяснилось, что на дне океана вблизи ОАЭ есть «чёрное золото» - нефть, которая гораздо ценнее золотых барханов. Благодаря обнаружению нефти, эта страна стала очень быстро развиваться и сегодня уже очень много туристов стремятся попасть в Арабские Эмираты.'   
    country.photo = 'images/country4.jpg' 
    country.save()
    
    region = Region()
    region.country=country;
    region.title = 'Дубаи' 
    region.details = 'Дубаи — самый элитный, роскошный и самый дорогой отдых. Местные отели построены и функционируют по самым высоким мировым стандартам. Отдых на этом побережье можно порекомендовать взыскательным клиентам, приоритетное значение для которых имеет уровень сервиса.'
    region.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'IBIS STYLES DUBAI AIRPORT 3*' 
    hotel.details ='Отель ibis Styles Dubai Airport расположен в Дубае, в 7,6 км от Большой мечети. К услугам гостей ресторан, бесплатная частная парковка и сад. В этом 3-звездочном отеле работает экскурсионное бюро и предлагаются услуги консьержа. Стойка регистрации открыта круглосуточно. Осуществляется доставка еды и напитков в номер. На всей территории предоставляется бесплатный Wi-Fi. Возможен трансфер от/до аэропорта.'
    hotel.photo  = 'images/hotel22.jpg'
    hotel.price = 354175
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=25);
    claim.user_id = 23
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=25);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'отель приличный. все достопримечательности на метро можно объехать. по еде- брала только завтраки : зелень 5-6 видов, овощи свежие, маринованные, на пару. Оливки, маслины и прочее. творог, йогурты , сметана, рассольные сыры, твердые сыры- очень неплохие, кстати! есть еще какие-то сырные шарики из индийской кухни, они острые. Есть хлеб, лаваши, лепешки, круассаны и слойки с джемом, сэндвичный хлеб. Естественно, жареные и вареные яйца. Из мяса- соевое мясо, колбаски (тоже соевые- не очень), печень и субпродукты. Фруктов маловато, это да. Ну и всякие джемы, мало и прочее...'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'GOLDEN TULIP AL BARSHA 4*' 
    hotel.details ='Четырехзвездочный отель Golden Tulip Al Barsha расположен в Дубае, в 1,4 км от торгового центра Mall of the Emirates. К услугам гостей открытый бассейн, бесплатная частная парковка, фитнес-центр, ресторан, детский клуб и бесплатный Wi-Fi. Осуществляется доставка еды и напитков в номер. Предоставляется бесплатный трансфер, а также услуги консьержа. Кроме того, гости могут обменять валюту.'
    hotel.photo  = 'images/hotel23.jpg'
    hotel.price = 364229
    hotel.save()
    
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=20);
    claim.user_id = 9
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=20);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Метро в 5 минутах ходьбы - что очень и очень удобно для передвижения. Рядом продуктовые хорошие магазины и несколько реторанов разной кухни - турецкая / азиатская / европейская.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()
        
    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=20);
    claim.user_id = 25
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=20);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()

    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Хороший отель, не свежий, но чисто в номерах и обслуживание на уровне, клиентоориентированность есть, были месяц назад ещё в другом отеле на букву N, где world trade улица, вот там вообще не было клиентоориентированности! Я Golden tulip полностью довольна и вернусь когда в Дубай буду жить именно в этом отеле)'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    hotel = Hotel()
    hotel.region=region;
    hotel.title = 'FAIRMONT HOTEL DUBAI 5*' 
    hotel.details ='Знаменитый отель Fairmont Dubai удобно расположен на шоссе Шейха Зайда в самом центре Дубая, напротив Всемирного торгового центра Дубая и всего в 10 минутах езды на автомобиле или метро от торгового центра Dubai Mall, небоскреба «Бурдж-Халифа» и фонтанов. К услугам гостей роскошный спа-центр, открытые бассейны, а также 13 ресторанов и развлекательных заведений. На всей территории работает бесплатный Wi-Fi.'
    hotel.photo  = 'images/hotel24.jpg'
    hotel.price = 499501
    hotel.save()

    claim = Claim()
    claim.datec = datetime.now() - timedelta(days=20);
    claim.user_id = 24
    claim.hotel = hotel
    claim.start  = claim.datec + timedelta(days=10)
    claim.finish  = claim.start + timedelta(days=7);
    claim.details = ''
    claim.save()
    claim.datec = datetime.now() - timedelta(days=20);    
    claim.result =  claim.datec.strftime('%d.%m.%Y') + ' Заявка создана\n' + (claim.datec +  timedelta(days=3)).strftime('%d.%m.%Y') + ' Заявка на рассмотрении, ожидайте звонка менеджера\n' + (claim.datec +  timedelta(days=7)).strftime('%d.%m.%Y') + ' Заявка одобрена'
    claim.save()
    
    reviews = Reviews()
    reviews.dater = claim.finish;
    reviews.hotel = hotel
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Красивая панорама открывается с рамки! Завораживающая поездка на лифте с прозрачной стеной. Вход в парк платный, но если вы после экскурсии на рамку, то можно пройти бесплатно. Сделать красивые кадры на фоне рамки.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    print("Country, Region, Hotel, Claim, Reviews Ok")
    
    ##### Новости #####
    News = apps.get_model("kaz", "News")
    
    news = News()
    news.daten = datetime.now() - timedelta(days=35)
    news.title = 'В Казахстане появится прямой рейс Алматы - Бали'
    news.details = """Остров Бали - одно из излюбленных направлений казахстанских туристов, и единственное, что сдерживает массовый турпоток казахстанских путешественников, это отсутствие прямого авиасообщения между Казахстаном и Индонезией. Ожидается, что уже к концу этого года проблема решится, передает корреспондент Tengritravel.kz.\r\n
    "В рамках подписания меморандума о взаимопонимании между городами-побратимами между Алматы и Бали изучается возможность открытия прямого рейса Алматы - Бали, который будет организован одной из индонезийских авиакомпаний. Рейс может быть открыт уже к концу этого года - в ноябре или декабре", - заявил посол Индонезии в Казахстане Мохамад Фаджрул Рахман.\r\n
    Обсуждение открытия прямых рейсов находится на стадии переговоров с казахстанскими туроператорами и авиакомпаниями, уже получен положительный отклик и принято решение о сотрудничестве.\r\n
    "В 2023 году мы ожидаем принять 10 тысяч казахстанских туристов в Индонезию, как и до пандемии. Оптимизм есть, поскольку казахстанцы с начала этого года могут въезжать в Индонезию с визой по прибытии, и мы зафиксировали почти 400 казахстанцев, прибывающих в Индонезию до марта", - рассказал советник посла по экономическим и политическим делам Густаф Дауд Сираит.\r\n
    В 2022 году Индонезию посетило 2275 казахстанцев, а нашу страну - 480 граждан Индонезии.
    """
    news.photo = 'images/news1.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=30)
    news.title = '"У меня пожизненная скидка". Казахстанец объехал 95 стран мира'
    news.details =  """Казахстанский блогер, путешественник и общественный деятель Александр Цой посетил 95 стран: до пандемии мужчина успевал объехать по 10-12 стран в год, а в период "ковидных" ограничений побывал в крупнейших городах Казахстана. В беседе с корреспондентом Tengritravel.kz путешественник рассказал о своих наработках и опыте.\r\n
    Александр признался, что изучает место следующего выезда, у него есть свои лайфхаки.\r\n
    "Я заранее стараюсь читать об этих местах, даже если у нас будет гид. Захожу в Instagram, ввожу эту достопримечательность и получаю 10 лучших фото, на фоне Тадж-Махала например.\r\n
    Я смотрю и знаю заранее уже, как я буду фотографироваться. В последние 20 стран, когда летел, я знал, как я буду фотографироваться и где буду стоять", - рассказал Цой.
    """
    news.photo = 'images/news2.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=25)
    news.title = 'Назван лучший город Европы для туристов'
    news.details = """Лондон, Париж и Амстердам возглавили рейтинг городов Европы, подходящих для туризма и долгосрочного проживания. Консалтинговая компания Resonance Consultancy расставила по местам 100 лучших мегаполисов континента, передает Tengritravel.kz.\r\n
    По информации ресурса Time Out, рейтингу можно доверять, ведь мнение составителей авторитетно.\r\n
    "Resonance Consultancy, фирма, организовавшая WorldsBestCities.com, составила рейтинг 100 лучших городов Европы на 2023 год. При составлении списка учитывались многие факторы, в том числе пешеходная доступность, достопримечательности, разнообразие, впечатления, уровень занятости и даже хештеги в Instagram", - пишет источник.\r\n
    Топ-10 лучших европейских городов выглядит так:\r\n
    Лондон, Великобритания\r\n
    Париж, Франция\r\n
    Амстердам, Нидерланды\r\n
    Барселона, Испания\r\n
    Цюрих, Швейцария\r\n
    Мадрид, Испания\r\n
    Берлин, Германия\r\n
    Рим, Италия\r\n
    Базель, Швейцария\r\n
    Женева, Швейцария\r\n
    """
    news.photo = 'images/news3.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=20)
    news.title = '"Летел как король". Турист "выкупил" самолет за 73 тысячи тенге'
    news.details = """ританский путешественник приобрел дешевый билет на рейс и оказался в сказочных условиях: мужчина был единственным пассажиром на борту и бортпроводники относились к нему, "как к королю", передает Tengritravel.kz со ссылкой на Daily Star.\r\n
    По информации издания, 65-летний Пол Уилкинсон летел из португальского Фару в Белфаст самолетом авиакомпании Jet2.\r\n
    "Этот полет мужчина не забудет никогда: экипаж обращался с ним, как с "членом королевской семьи". Пол получил VIP-обслуживание на борту, "как будто летел на собственном частном самолете". Пассажир был потрясен, когда, подойдя к выходу на посадку, обнаружил, что он единственный в очереди в самолет.\r\n
    Он даже спросил сотрудников аэропорта, был ли его рейс задержан или отменен, но они сообщили ему, что самолет собирается взлететь, так как Пол - единственный пассажир, забронировавший билет на рейс", - рассказывает источник.\r\n
    """
    news.photo = 'images/news4.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=15)
    news.title = '"Когда любишь свою работу". Изобретательный гид на Бали покорил соцсети'
    news.details = """Актерское мастерство гида в Индонезии покорило социальные сети: мужчина нашел неожиданную "подработку" - он стал популярным после подбора для своих клиентов наилучших вариантов для фото на фоне водопада, передает Tengritravel.kz.\r\n
    По информации автора ролика с гидом, эпизод снят у водопада Канто Лампо на Бали.\r\n
    "Мужчина с телефоном раскрывает клиентам варианты для лучших фото", - пишут в сети, а другие добавляют: "Он очень любит свою работу".
    """
    news.photo = 'images/news5.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=10)
    news.title = 'Как безвизовый режим с Китаем повлияет на экономику Казахстана'
    news.details = """Правительства Казахстана и Китая планируют ввести безвизовый режим для своих граждан в обе стороны. Корреспондент Tengrinews.kz поинтересовалась у эксперта, как безвизовый режим может повлиять на экономику нашей страны.\r\n
    "Объясню почему. Китайская экономика - это 90 казахстанских экономик. То есть у нас ВВП порядка 200 миллиардов долларов, тогда как их ВВП порядка 18 триллионов. Во-вторых, их экономика гораздо сложнее. Если у нас в глобальном плане Казахстан может предложить сырье, то китайская экономика - это серьезная обработка совершенно разных товаров. Если раньше это были полуфабрикаты, то сейчас Китай делает и потребительские товары: технику, электротехнику, электробытовые приборы и много всего разного. Здесь с точки зрения экономики для нас тоже будет плюс", - считает эксперт.\r\n
    Еще одним плюсом может стать сельское хозяйство и туризм Казахстана, отмечает Жаиков. По мнению эксперта, именно Восточно-Казахстанская область в будущем может создать платежеспособный спрос.\r\n
    "Мы немного отстали в понимании Китая. Эта страна уже гораздо богаче, чем мы. Не по формальным показателям ВВП на душу населения, а по заработным платам, по доходам. У них растущий средний класс, они начинают гораздо более качественно питаться, чем раньше, гораздо больше ездят за рубеж. И в этом плане Казахстану есть что предложить, поскольку безусловными бенефициарами нашей страны являются сельское хозяйство и туризм. Если говорить регионально, это однозначно Восточно-Казахстанская область, Жетысу, Алматы и Алматинская область. Понятно, что весь ВВП наш, возможно, сильно не сдвинется, но его отдельные отрасли и регионы будут достаточно ощутимыми бенефициарами этой истории", - добавил казахстанский экономист.\r\n
    А вот что касается экспорта и импорта, то, по мнению эксперта, здесь не стоит ожидать "больших движений". Также, по его словам, излишни страхи, что Казахстан "станет больше отправлять сырья", поскольку китайская сторона уже давно "участвует в добыче и в первичной обработке". То же самое касается и нефтегазовой промышленности.
    """
    news.photo = 'images/news6.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=5)
    news.title = 'Казахстанцы смогут летать в Дели из Шымкента'
    news.details = """Авиамаршрут Шымкент - Дели - Шымкент впервые запускают из Казахстана, передает Tengritravel.kz со ссылкой на пресс-службу Комитета гражданской авиации.\r\n
    По информации ведомства, маршрут будет запущен в конце мая - планируются два рейса в неделю.\r\n
    "Впервые в истории открывается новый авиамаршрут Шымкент - Дели - Шымкент. Рейсы будут выполняться авиаперевозчиком Fly Arystan c 22 мая 2023 года с частотой 2 раза в неделю по понедельникам и четвергам на воздушном судне типа Airbus-320", - говорится в сообщении.\r\n
    Ранее стало известно, что Казахстан планирует ввести безвизовый режим с Китаем, а мы рассказали о малоизвестных туристических казахстанских маршрутах.\r\n
    Ранее был назван самый популярный для иностранцев регион в Казахстане, а также стало известно, когда казахстанцы смогут летать в Нью-Йорк, Токио, Сингапур и Шанхай.
    """
    news.photo = 'images/news7.jpeg' 
    news.save()
    
    print("News Ok")


class Migration(migrations.Migration):

    dependencies = [
        ('kaz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(beginning),       
        migrations.RunSQL("""CREATE VIEW view_hotel AS
                        SELECT hotel.id, region.country_id, country.title AS country, hotel.region_id, region.title AS region, hotel.title, hotel.details, hotel.photo, hotel.price, (SELECT AVG(rating) FROM reviews WHERE reviews.hotel_id = hotel.id) AS avg_rating 
                        FROM hotel LEFT JOIN region ON hotel.region_id = region.id
                        LEFT JOIN country ON region.country_id = country.id;"""),
    ]

