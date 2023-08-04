import boto3

def main():
    session = boto3.Session(
        profile_name = '',
        region_name = ''
    )

    iam_client = session.client('iam')
    reponse = iam_client.list_users()
    
    iam_users = reponse['Users']

    for user in iam_users:        
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/user/password_last_used.html#
        # If iam.user has PasswordLastUsed, it's because he has console access.
        try:
            if user['PasswordLastUsed']:
                print(user['UserName'])
        except:
            continue

if __name__ == '__main__':
    main()