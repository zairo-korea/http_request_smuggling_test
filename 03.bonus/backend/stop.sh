docker rm -f -v $(docker ps -a -q --filter="name=tete_backend")
docker rmi tete_backend
