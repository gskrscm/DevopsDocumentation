## Useful Cmds:

- To Check Version: 
`docker version`

#### Process:
- To check list of process running:
`docker ps`

- To check all process: 
`docker ps -a`


#### Images:
- To list images: docker images
- To create image: docker build -t "<name>:<tag>"


#### Containers: 
- To Start Container: 
  docker run -d --name <container name> -p 0.0.0.0:8080:80 <image name>
    - -d: detached mode
- To start stopped container: 
  docker start <container-name>

- Login to Container: 
`  docker exec -it <container name/ id> bash`'

Docker Container Lifecycle https://medium.com/@nagarwal/lifecycle-of-docker-container-d2da9f85959


