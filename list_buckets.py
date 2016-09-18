#Om
#Script to list all buckets that belongs to an object user in ECS.
#ECS is Elastic Cloud Storage from DELL EMC. 
from boto3.session import Session, Config

print('***Welcome to ECS buckets lists. This program will list all the buckets that is owned by an object user***\n\n \
URL of the ECS Node IP or the loadbalancer is hardcoded in the script. Edit the script to change "ecs_url" with \n the IP address that you have set for ECS \n\n \
Likewise change "ecs_obj_user" and "ecs_secret_key" with the ECS object user and the respective secret key.\n\n')

#Connection information
ecs_url = 'https://10.63.17.148:9021' # IP address of ECS
ecs_obj_user = 'az_nfs' # ECS object user
ecs_secret_key = 'KosZlKoqOlGj9geV0ea/nWIJg2ndKtV9/flEqEVC' # Secret key belonging object user

#The url we use is secure and the SSL certificate provided by ECS is not verified,
#so we will capture the InsecureRequestWarning with a logging module.
import logging
logging.captureWarnings(True)

addressing_style = 'path' #ECS recommends using path style
signature_version = 's3'

#Establishing connection to ECS
session = Session(aws_access_key_id=ecs_obj_user, aws_secret_access_key=ecs_secret_key)
s3 = session.resource('s3', endpoint_url=ecs_url, verify=False,   
                      config=Config(signature_version='s3', s3={'addressing_style': 'path'}))

#Prints all the buckets owned by the respective user.
for bucket in s3.buckets.all():
    print ('User', ecs_obj_user, 'owns the following buckets:\n\n',bucket.name)
