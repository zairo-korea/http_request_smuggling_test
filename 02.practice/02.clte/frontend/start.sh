docker build -t clte_frontend .
docker run -p 80:1080 --name clte_frontend -it clte_frontend
