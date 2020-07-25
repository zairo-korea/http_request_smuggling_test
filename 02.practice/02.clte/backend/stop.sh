docker rm -f -v $(docker ps -a -q --filter="name=clte_backend")
docker rmi clte_backend
