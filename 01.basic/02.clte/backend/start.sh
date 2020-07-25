docker build -t clte_backend .
docker run -p 8080:80 --name clte_backend -it clte_backend
