docker build -t clcl_backend .
docker run -p 8080:80 --name clcl_backend -it clcl_backend
