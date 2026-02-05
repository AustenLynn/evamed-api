#!/bin/sh
set -e

DUMP_FILE="/docker-entrypoint-initdb.d/backup2025.dump"

if [ -f "$DUMP_FILE" ]; then
  echo "Restoring database from $DUMP_FILE"
  if pg_restore --list "$DUMP_FILE" > /dev/null 2>&1; then
    pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" --no-owner --no-privileges "$DUMP_FILE"
  else
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "$DUMP_FILE"
  fi
fi
