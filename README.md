# rhi-server

`rhi-server` provides API for [rhi](https://github.com/warabanshi/rhi) command.

## Luanch server
There's a `docker-compose.yml` file under the project directory. So, just run a command as follows

```
$ docker-compose up -d
```

## Storage path

The storage path is in `app/config.py`. It supports plain text file and the path points the direcotry under the docker container so it's ephemeral so far. (I'll fix it in soon)
