# Политика конфиденциальности

## 1. Сбор данных
Приложение использует Pinterest API для:
- Публикации пинов от имени пользователя.
- Доступа к данным досок (названия, описания).

## 2. Использование данных
- **API-ключи** (CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN) применяются исключительно для авторизации через Pinterest API.
- **Изображения и метаданные** загружаются только на серверы Pinterest.
- Данные пользователя не передаются третьим лицам.

## 3. Хранение информации
- API-ключи хранятся локально в файле `.env`, который не попадает в систему контроля версий.
- Мы не сохраняем логи действий пользователя.

## 4. Права пользователя
Вы можете:
- Отозвать доступ приложения через [настройки Pinterest](https://www.pinterest.com/settings/apps/).
- Удалить `.env`-файл для прекращения работы скрипта.

## 5. Безопасность
Все ключи защищены стандартными методами шифрования. Для работы скрипта требуется доступ только к тем правам, которые явно запрашиваются при авторизации.

## Контакты
Для вопросов: ваш-email@example.com.
