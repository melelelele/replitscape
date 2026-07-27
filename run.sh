#!/usr/bin/env bash
set -euo pipefail

rm -rf .server-build
mkdir -p .server-build

javac   --release 17   --add-modules jdk.httpserver   -encoding UTF-8   -d .server-build   Server.java

exec java   --add-modules jdk.httpserver   -cp .server-build   Server
