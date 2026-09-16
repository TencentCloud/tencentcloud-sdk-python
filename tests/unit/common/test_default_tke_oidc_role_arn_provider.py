from tencentcloud.common.credential import DefaultTkeOIDCRoleArnProvider, OIDCRoleArnCredential


def test_default_tke_oidc_role_arn_provider_get_credential(mocker):
    provider = DefaultTkeOIDCRoleArnProvider()
    get_credentials = mocker.patch.object(provider, "get_credentials")
    provider.get_credential()
    get_credentials.assert_called_once()


def test_default_tke_oidc_role_arn_provider_get_credentials(mocker):
    provider = DefaultTkeOIDCRoleArnProvider()
    with mocker.patch('tencentcloud.common.credential.OIDCRoleArnCredential._init_from_tke', return_value=None):
        cred = provider.get_credentials()
        assert cred._is_tke is True
