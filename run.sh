#~/bin/bash 
#[Windows requires help with getting port binding to work](https://stackoverflow.com/questions/48278223/windows-docker-port-not-exposed-reachable)
docker rm -f uvicornPrime || true
docker build -t merlin:latest ./; docker run --name uvicornPrime -p 8080:8080 -it merlin:latest

 