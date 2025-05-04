# Key Mutation

**Key Mutation** — утилита для проверки, менялся ли публичный ключ у Bitcoin-адреса.

## Зачем это нужно

Если адрес использует разные публичные ключи в разных транзакциях, это может нарушать приватность.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python key_mutation.py <bitcoin_address>
```

## Пример

```bash
python key_mutation.py 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
```

## Возможности

- Показывает количество уникальных публичных ключей
- Помогает отследить нарушения privacy best practices

## Лицензия

MIT
