docker rm -f -v $(docker ps -a -q --filter="name=tecl_backend")
docker rmi tecl_backend
