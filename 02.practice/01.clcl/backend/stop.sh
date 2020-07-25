docker rm -f -v $(docker ps -a -q --filter="name=clcl_backend")
docker rmi clcl_backend
