#### how to use?

##### build image

`docker build -t mid-gen:1.0.0 .`

##### create config and output in current directory:

```bash
touch config.ini
mkdir output
```
##### run and destroy container

`docker run --rm -v ./config.ini:/config/config.ini -v ./output:/output mid-gen:1.0.0`

