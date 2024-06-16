## Использование

```
$ docker build -t mtu .
$ docker run --rm mtu google.com
$ docker run --rm mtu google.com -m 68 -M 1500
```

## Параметры
- `dst` задает host для нахождения MTU, позиционный аргумент
- `-m` задает ограничение снизу на искомый MTU
- `-M` задает ограничение сверху на искомый MTU
