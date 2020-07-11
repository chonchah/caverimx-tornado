# CAVERIMX FRAMEWORK TORNADO BASED

# HOW TO IMPLEMENT?


## DEPENDENCIES
1. Docker, Make you sure the lastest release running in the target machine. You can visit https://docs.docker.com/docker-for-windows/install/
2. Install docker-compose. Wether your machine run under windows you need use Docker Toolbox https://docs.docker.com/toolbox/toolbox_install_windows  For more systems visit https://docs.docker.com/compose/

Clone this repo.
```bash
git clone https://gitlab.com/caverimx/caverimx-tornado.git
cd caverimx-tornado
```


## ENVIROMENT'S CONFIGURATION
Copy the file 
`
docker-services/env-example to docker-services/.env
`
Edit docker's environments file for docker. Inside repository directory run and edit with your best editor.

```bash
cp docker-services/env-example docker-services/.env
```
## INIT DOCKER CONTAINER
```bash
docker-compose up
```