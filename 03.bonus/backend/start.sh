docker build -t tete_backend .
docker run -p 8080:80 --name tete_backend -it tete_backend
