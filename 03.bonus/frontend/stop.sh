docker rm -f -v $(docker ps -a -q --filter="name=tete_frontend")
docker rmi tete_frontend
