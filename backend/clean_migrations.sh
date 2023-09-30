#!/bin/bash
# to clean all migrations files in the project.
find . -type f -name "0*.py" -exec rm -f {} \; -print
find . -type f -name "0*.pyc" -exec rm -f {} \; -print

echo "All migrations in apps are cleaned!"