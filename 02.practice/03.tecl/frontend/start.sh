docker build -t tecl_frontend .
docker run -p 80:1080 --name tecl_frontend -it tecl_frontend
