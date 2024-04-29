pip3 install -r ./PythonLambdaLayer/requirements.txt -t ./PythonLambdaLayer/python
sam deploy \
  --template-file task1template.yaml \
  --stack-name aryanstack1 \
  --region us-west-2 \
  --capabilities CAPABILITY_IAM \
  --s3-bucket aryantestbuckertcf \
  --tags "JRDev=Aryan" "TaskNo=1"

sam deploy \
  --template-file task2template.yaml \
  --stack-name aryanstack1 \
  --region us-west-2 \
  --capabilities CAPABILITY_IAM \
  --s3-bucket aryantestbuckertcf
  --tags "JRDev=Aryan" "TaskNo=2" \

sam deploy \
  --template-file task3template.yaml \
  --stack-name aryanstack1 \
  --region us-west-2 \
  --capabilities CAPABILITY_IAM \
  --s3-bucket aryantestbuckertcf \
  --tags "JRDev=Aryan" "TaskNo=3"