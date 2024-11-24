#!/bin/bash
if [ "{{ dxh_py.use_celery }}" == "y" ] && [ "{{ dxh_py.use_docker }}" == "y" ]; then
  if [ "{{ dxh_py.database_engine }}" == "postgresql" ]; then
    ENV_FILE="./.envs/.production/.postgres"
  elif [ "{{ dxh_py.database_engine }}" == "mysql" ]; then
    ENV_FILE="./.envs/.production/.mysql"
  else
    echo "Unsupported database engine: {{ dxh_py.database_engine }}"
    exit 1
  fi

  LOCAL_ENV_FILE="./.envs/.local/.django"
  if [ -f "$LOCAL_ENV_FILE" ]; then
    DEBUG=$(grep -E '^DEBUG=' $LOCAL_ENV_FILE | cut -d '=' -f2 | tr -d '"')
    if [ "$DEBUG" == "True" ]; then
      if [ "{{ dxh_py.database_engine }}" == "postgresql" ]; then
        ENV_FILE="./.envs/.local/.postgres"
      elif [ "{{ dxh_py.database_engine }}" == "mysql" ]; then
        ENV_FILE="./.envs/.local/.mysql"
      fi
    fi
  else
    echo "Local environment file not found: $LOCAL_ENV_FILE"
    echo "Using production environment file by default."
  fi

  if [ -f "$ENV_FILE" ]; then
    export $(grep -v '^#' $ENV_FILE | xargs)
  else
    echo "Environment file not found: $ENV_FILE"
    exit 1
  fi

  BACKUP_DIR="./backups"
  TIMESTAMP=$(date +"%Y_%m_%dT%H_%M_%S")
  mkdir -p $BACKUP_DIR

  if [ "{{ dxh_py.database_engine }}" == "postgresql" ]; then
    export PGPASSWORD=$POSTGRES_PASSWORD
    docker exec -i $POSTGRES_CONTAINER pg_dump -U $POSTGRES_USER -d $POSTGRES_DB > $BACKUP_DIR/backup_$TIMESTAMP.sql
  elif [ "{{ dxh_py.database_engine }}" == "mysql" ]; then
    docker exec -i $MYSQL_CONTAINER mysqldump -u$MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE > $BACKUP_DIR/backup_$TIMESTAMP.sql
  else
    echo "Unsupported database engine: {{ dxh_py.database_engine }}"
    exit 1
  fi

  tar -czf $BACKUP_DIR/backup_$TIMESTAMP.sql.gz -C $BACKUP_DIR backup_$TIMESTAMP.sql
  rm $BACKUP_DIR/backup_$TIMESTAMP.sql

  find $BACKUP_DIR -type f -name "*.gz" -mtime +7 -delete

  echo "Backup completed: $BACKUP_DIR/backup_$TIMESTAMP.sql.gz"
fi
