#!/bin/bash
set -e

APP_HOME="$(cd "$(dirname "$0")" && pwd)"
cd "$APP_HOME/src"

exec "$APP_HOME/.venv/bin/python" "$APP_HOME/src/dht_exporter.py"
