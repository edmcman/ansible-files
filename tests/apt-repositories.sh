#!/usr/bin/env bash
set -euo pipefail
repo_dir=$(cd "$(dirname "$0")/.." && pwd)
docker run --rm --network host -v "$repo_dir:/repo:ro" -v /usr/local/share/ca-certificates:/tmp/host-ca:ro ubuntu:22.04 bash -euc '
  export DEBIAN_FRONTEND=noninteractive
  apt-get update -qq
  apt-get install -y -qq ansible python3-apt ca-certificates gnupg
  cp /tmp/host-ca/*.crt /usr/local/share/ca-certificates/ 2>/dev/null || true
  update-ca-certificates
  ansible-playbook /repo/tests/apt-repositories.yml
  ansible-playbook /repo/tests/apt-repositories.yml
'
