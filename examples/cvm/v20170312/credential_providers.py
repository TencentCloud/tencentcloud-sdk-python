from tencentcloud.common import credential
from tencentcloud.cvm.v20170312 import cvm_client


def new_cli_by_default_credential():
    return cvm_client.CvmClient(credential.DefaultCredentialProvider().get_credential(), 'ap-guangzhou')


def new_cli_by_environment():
    return cvm_client.CvmClient(credential.EnvironmentVariableCredential().get_credential(), 'ap-guangzhou')


def new_cli_by_profile():
    return cvm_client.CvmClient(credential.ProfileCredential().get_credential(), 'ap-guangzhou')


def new_cli_by_cvm_role():
    return cvm_client.CvmClient(credential.CVMRoleCredential().get_credential(), 'ap-guangzhou')


def new_cli_by_tke_oidc():
    return cvm_client.CvmClient(credential.DefaultTkeOIDCRoleArnProvider().get_credential(), 'ap-guangzhou')
