# Locked Out

## Categories

cloud

## Write Up

Given only the URL of the AWS S3 bucket <https://external-spaceship-storage-b38e8c6.s3-eu-west-1.amazonaws.com/> :

1. Launch this URL, and you will see a public content available on the listing, ie. external-spaceship-storage.txt
2. Launch the URL <https://external-spaceship-storage-b38e8c6.s3-eu-west-1.amazonaws.com/external-spaceship-storage.txt> to downloadthis text file
3. In this text file, you are able to find the Access Key ID, Secret Access Key, and the first flag
4. Download the awscli and launch the command `aws configure`, to authenticate by providing those information mentioned above
5. Command `aws s3 ls` lists all the directories on the corresponding authorized S3 bucket, and you will see a private directory that wasn't found on step 1. You should be able to find a file in it, which contain the 2nd flag
6. Command `aws s3 cp <source> <target>` allows you to download/copy the file from S3 bucket (requires prefix s3://FULL_PATH) to local machine

### Flags

1. CTF{6c2c45330a85b126f551}
2. CTF{4ababede5580d9a22a2a}

### References

- <https://medium.com/@shamnad.p.s/how-to-create-an-s3-bucket-and-aws-access-key-id-and-secret-access-key-for-accessing-it-5653b6e54337> [3,4]
- <https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html>