#!/bin/bash

function check_ok () {
  if [ $? -eq 0 ]
  then
    echo "OK"
  else
    echo "ERROR" && exit 1
  fi
}

function zip_lambda ()
{
  echo "Zipping dependencies"
  cd venv/lib/python3.11/site-packages
  zip -r ../../../../deployment_package.zip .
  cd ../../../../

  echo "Zipping lambda"
  zip -g deployment_package.zip handler.py
  check_ok
}

function sync_lambda ()
{
  echo "syncing lambda"
  aws --region us-east-1 lambda update-function-code --function-name PdfMerger --zip-file fileb://./deployment_package.zip --profile greenmanatee
  check_ok
}

function delete_zip ()
{
  echo "deleting zip"
  rm deployment_package.zip
  check_ok
}


zip_lambda
sync_lambda
delete_zip
exit 0
