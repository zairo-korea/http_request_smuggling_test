docker rm -f -v $(docker ps -a -q --filter="name=clcl_frontend")
docker rmi clcl_frontend
