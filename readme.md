

# Run the application with Python
- runs on port 5000
```sh
python catfact.py 
```

# Run the application with Docker
```sh
docker build -t cat-fact-image .
docker run -d -p 5000:5000 cat-fact-image
```

# 