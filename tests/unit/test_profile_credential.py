from tencentcloud.common.credential import ProfileCredential


def test_profile_without_default_section(tmpdir, monkeypatch):
    path = tmpdir.join("credentials")
    path.write("[other]\nsecret_id=other-id\nsecret_key=other-key\n")
    monkeypatch.setattr("os.path.expanduser", lambda _: str(path))

    assert ProfileCredential().get_credential() is None


def test_profile_rereads_default_section(tmpdir, monkeypatch):
    path = tmpdir.join("credentials")
    path.write("[default]\nsecret_id=test-id\nsecret_key=test-key\n")
    monkeypatch.setattr("os.path.expanduser", lambda _: str(path))
    provider = ProfileCredential()

    assert provider.get_credential().get_credential_info() == (
        "test-id", "test-key", None)
    path.write("[other]\nsecret_id=other-id\nsecret_key=other-key\n")
    assert provider.get_credential() is None
