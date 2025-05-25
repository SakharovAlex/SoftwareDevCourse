Скачивание istioctl:
```
curl -L https://istio.io/downloadIstio | sh -
cd istio-*
export PATH=$PWD/bin:$PATH
```
Установка istio в кластер:
```istioctl install --set profile=demo -y```

Включение автоматического внедрения sidecar-прокси:
```kubectl label namespace default istio-injection=enabled```
