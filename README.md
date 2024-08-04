# yandex-password-backup (v.0.0.1)

***
##  Что это?

Сервис для работы с личными паролями в хранилищаx.

## Что умеет сервис?

1. Получать пароли из зашифрованного zip-архива из сервиса Яндекс.Пароли.
2. Получать пароли из Google Таблицы.
3. Проверять эти пароли на:
   - Повторы.
   - Отсутствие пар.
   - Различающиеся пароли в парах.


## Запуск
1. Склонируйте репозиторий:
```bash
git@gitflic.ru:glazarev/yandex-password-backup.git
сd yandex-password-backup
```

2. Установите виртуальное venv-окружение и активируйте:
```bash
python3.10 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r req.txt
```

4. Укажите данные приложения в .env:
```bash
pip install -r req.txt
```

# Меню:
[Changelog](https://gitflic.ru/project/glazarev/yandex-password-backup/blob?file=docs%2Fchange_log.md&branch=master&mode=markdown)