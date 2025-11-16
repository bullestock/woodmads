#!/bin/bash
docker run --rm -v $PWD:/project -w /project -u $UID -e HOME=/tmp espressif/idf:release-v4.3 idf.py build
