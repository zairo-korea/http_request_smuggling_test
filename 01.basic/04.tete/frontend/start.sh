docker build -t tete_frontend .
docker run -p 80:1080 --name tete_frontend -it tete_frontend
