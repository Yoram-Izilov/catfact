# Cat Facts

## Run the application with Python
- runs on port 5000
```sh
python catfact.py 
```

## Run the application with Docker
```sh
docker build -t cat-fact-image .
docker run -d -p 5000:5000 --name cat-fact-app cat-fact-image
```

## Run the application with minikube
- first add "192.168.49.2 catfacts.local" to /etc/hosts (check your minikube ip)  
```sh
minikube ip 
sudo vim /etc/hosts
```
- run the helm chart:
```sh
helm install cat-fact-app ./chart
```
### That's it! try to fetch a fact in http://catfacts.local/
