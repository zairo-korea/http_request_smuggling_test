docker build -t clcl_frontend .
docker run -p 80:1080 --name clcl_frontend -it clcl_frontend
