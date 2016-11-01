## Raw data

We gathered reviews about several e-shops from [https://market.yandex.ru/](Yandex.Market). In order to do this, we derived the following criteria:
  - e-shop is "reliable" when it has about the same count of negative and positive reviews (judging by grade);
  - e-shop is "unreliable" when it has mostly (> 90%) positive reviews + review count is low (< 200).
We expect reviews for "unreliable" shops to be mostly paid, because real people tend to express more opinions than "excellent".
  
Then we manually created three lists of e-markets: reliable, unreliable and everything else.

Reliable:
 - МВидео
 - МТС
 - Мегафон
 - Эльдорадо
 
Unreliable:
 - Landcom
 - Opt-Device
 - Telebar.ru
 - SLK-Service.ru
 - BONCH.PRO
 - ProAnima.RU
 
Everything else:
 - Cifrovoi.com
 - Apple-Zone
 
We gather 100 reviews per market using Y.Market API (1200 in total), then shuffle those groups and split them into 4 equal parts (300 reviews per part).
 
### Statistics
data.json
 - Raw reviews count: 1200
 - Number of negative reviews: 186
 
data1.json
 - Number of entries: 300
 - Number of negative reviews: 23

data2.json
 - Number of entries: 300
 - Number of negative reviews: 100

data3.json
 - Number of entries: 300
 - Number of negative reviews: 60

data4.json
 - Number of entries: 300
 - Number of negative reviews: 3
