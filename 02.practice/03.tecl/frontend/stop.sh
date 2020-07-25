docker rm -f -v $(docker ps -a -q --filter="name=tecl_frontend")
docker rmi tecl_frontend
