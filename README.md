# Microservice Template
FastAPI + MongoDB + MySQL + Redis + central json logging + project config file w/ validations.

## Init Project
```bash
# define configuration. (Required)
# project/config/__init__.py
# define APP_NAME and use to get app logger.
# the configuration file must be in the project root path: 
# $APP_HOME/config.yaml

# configure logging. (Optional)
# project/logging/__init__.py

# configure database. (Optional)
# set client configuration and credentials in $APP_HOME/config.yaml
# select databases [sql, nosql] and uncomment dependencies.
# defining models (sqlalchemy|beanie) inheriting "Base" in:
# project/database/(sql|nosql)/models.py

# configure cache if require. (Optional)
# project/cache/__init__.py
# set client configuration and credentials in $APP_HOME/config.yaml
# uncomment dependencies.

# create model schemas, routes and core code.
# add routes and defining endpoint prefix in main.app

# Dockerfile and docker-compose.yaml compose file in:
# infra/docker/*

# Predefined and editable Environment Variables:
# PYTHONUNBUFFERED=1 
# PYTHONDONTWRITEBYTECODE=1 
# APP_HOME=/microservice
# HOST=0.0.0.0 
# PORT=5000
```

## Commands
```bash
# sql migrations.
# generate new revision.
migrations revision --autogenerate
# upgrade to last revision.
migrations upgrade head
# downgrade 1 revision.
migrations downgrade -1

# other commands.
python -m cli [command]
```

## Roadmap
 - Extend logging configuration with yaml. (https://gist.github.com/kingspp/9451566a5555fb022215ca2b7b802f19)
 - Move 'alembic.ini' and 'migrations/' to 'project/sql/' and create new command in 'cli.py' for replace native alembic command with new config paths. (https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision)
 - Create cutter cookie project generator. (https://cookiecutter.readthedocs.io/en/stable/README.html#features)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
