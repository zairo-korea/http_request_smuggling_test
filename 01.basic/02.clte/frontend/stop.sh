docker rm -f -v $(docker ps -a -q --filter="name=clte_frontend")
docker rmi clte_frontend
