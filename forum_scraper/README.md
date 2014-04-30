# MOOC Forum Scraper

## Setup your ssl key

```bash
openssl genrsa -out key.pem 4096
openssl req -new -key key.pem -out csr.pem
openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
rm csr.pem
```

---

TODO
====
artoo (ajaxSpider / async)

scrap le mooc

kof code review TubeMyNet
finir ForceAtlas2
finir le SVG

---
"/C=US/ST=California/L=San Francisco/O=Local-Company/OU=dev/CN=localhost/emailAddress=test@test.com"
