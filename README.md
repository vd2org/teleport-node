Teleport node
-------------

This project provides a simple solution to start a **[teleport](https://goteleport.com/)** node on a host through Docker. 

The Docker image copies the teleport binary to the host and runs it in host mode.

The default root path is `/var/teleport-node`, which can be adjusted by setting the `HOST_ROOT` variable.

### Supported platforms

* linux/amd64
* linux/arm64

### Available versions

[Here](https://github.com/users/vd2org/packages/container/package/teleport-node)

### Creating an Auth Token

Use the following command to create a new auth token:

```shell
tctl nodes add
```

This will generate a new token like this:

```shell
> docker exec -ti teleport tctl nodes add
The invite token: ddnp9yobukji84aturqa59oiqsxux896
This token will expire in 30 minutes.
```

### Starting with Docker

You can start the teleport node using Docker with the following command:

```shell
docker run -d --name teleport-node \
  --privileged \
  --network=host \
  --ipc=host \
  --pid=host \
  --volume=/:/rootfs \
  --restart=always \
  -e "INIT_PROXY_SERVER=teleport.example.com:443" \
  -e "INIT_TOKEN=ddnp9yobukji84aturqa59oiqsxux896" \
  ghcr.io/vd2org/teleport-node:v14.3.30
```

### Starting with Docker Compose

You can also start the teleport node using Docker Compose with the following command:

```shell
curl https://raw.githubusercontent.com/vd2org/teleport-node/v14.3.30/compose.yml |
INIT_TOKEN=ddnp9yobukji84aturqa59oiqsxux896 INIT_PROXY_SERVER=teleport.example.com:443 docker compose -p teleport-node -f - up -d
```

### Upgrading an existing container

To upgrade an existing image, use the following command:

```shell
curl https://raw.githubusercontent.com/vd2org/teleport-node/v14.3.30/compose.yml | docker compose -p teleport-node -f - up -d
```
