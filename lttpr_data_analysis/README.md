# Randomizer Log Generator

Lets you locally generate alttpr logs. Currently on v31.

**Note**: This requires an ALTTP J1.0 rom which is saved in the base directory and is named `lttp.sfc`.

## Quickstart:

In the root of this directory, git clone the alttp_vt_randomizer:

```bash
git clone git@github.com:sporchia/alttp_vt_randomizer.git
```

**NOTE**: You may have to delete the composer.lock file since, for whatever reason, it seems to crash things for me.

Next use docker to build the Dockerfile,

```bash
docker build -t lttpr .
```

Mount the output drive to save logs and run the docker image:

```bash
docker run -v <local-dir>/output:/src/output -it lttpr
```

Inside, use the command:

```bash
php artisan alttp:randomize --skip-md5 --spoiler --no-rom --no-interaction --bulk=<number-of-spoilers> ./lttp.sfc ./output
```

Replace `<number-of-spoilers>` with the number of spoiler logs you want to generate.

**Note**: This does an interactive session. If you don't want to run this, take the -it off and use the command at the end of the docker rn file as usual.
