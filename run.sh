#!/bin/bash
ulimit -m 1024000
exec python $@
