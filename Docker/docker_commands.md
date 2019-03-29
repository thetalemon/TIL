## 概要
よく使うdockerコマンドまとめておく

- コンテナの中に入る
```
docker exec -i -t [container ID] bash
```

- コンテナの中に入らず、コンテナの中を操作
```
docker exec -i -t [container ID] [command (ex. cat test.txt, ls /var/www/)]
```


- キャッシュなしでビルド
```
docker-compose build --no-cache
```
