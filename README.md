# delegate-optimism

Скрипт свапает ETH => OP через Uniswap и делегирует OP на свой (твой) кошелек. Делегирование самому себ нужно чтобы участвовать в голосованиях optimism на snapshot. 

Настройка :
1. В ```config.py``` меняем значения 4 переменных : 
- AMOUNT_FROM = от какого кол-во eth свапать
- AMOUNT_TO   = до какого кол-во eth свапать
- SLEEP_FROM  = sleep от (в секундах) между swap, delegate и следующим кошельком
- SLEEP_TO    = sleep до (в секундах) между swap, delegate и следующим кошельком
2. В файл ```private_keys.txt``` добавляем приватники от кошельков. Пустых строк быть не должно. 
3. Запускаем файл ```run.py```

Если OP уже лежит на кошельках и нужно только делегировать, тогда закомментируй запуск функции uniswap_swap в ```run.py```

Выводить eth в сети optimism советую через binance, там нулевая комиссия. Мой скрипт по выводу с binance есть [здесь](https://github.com/zaivanza/binance-withdraw-ccxt) и [здесь](https://github.com/zaivanza/all-in-one). 
