# VK-Chat-Bot

Это ВК чат-бот для регистрации в группе на автобусный тур.


# Инструкция

1) Поднять базу данных через консоль командой:
→ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

2) Запустите bot.py 

3) Найти группу в ВК https://vk.com/theprodigytour2009 и написать ей сообщение. 
Отреагирует автоответчик. Следуйте его интструкциям  
   

# Функционал
- Автоответчик;
- Регистрация по имени и почтовому ящику;
- Генерация индивидуально билета с аватаром;
- Логирование;
- Работа с базой данных;
- Покрытие тестами. 