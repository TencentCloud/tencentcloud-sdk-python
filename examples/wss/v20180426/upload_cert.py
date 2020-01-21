import os
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.wss.v20180426 import wss_client, models
try:
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "wss.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = wss_client.WssClient(cred, "", clientProfile)

    req = models.UploadCertRequest()
    # This is just an example, please use your real certificate file instead.
    req.Cert = """-----BEGIN CERTIFICATE-----
MIIFejCCBGKgAwIBAgISA2rvMNLaaa+8oqfizkFpXqhxMA0GCSqGSIb3DQEBCwUA
MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD
ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xOTEyMjgyMDIyNDVaFw0y
MDAzMjcyMDIyNDVaMCAxHjAcBgNVBAMTFWZ1bWVuZ3dhbmdsdW9rZWppLmNvbTCC
ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPOuUV+f3cGhz+bi9SRNnfqB
tIGvvvGCsIZ/23juRxD2bS+L2RMq6aY1d5cESgPZKjEKOPmtMOgUyuGAY+nFfCkt
oBYTVtH+p/AdhDSmPbKgI+pxrxbCL7TWrUDokZQ5wqkyoVrEGyDt2SezPDoHx9Ml
Uypm107VdEh9sLJNaNFWl+7yfKBdeXqSfIM1aNJRsxX65UuFCDJnvHOQ2LJx6pvt
5McxWY+yAyOVPtMOFB6F66khIQaEyKTh/I6wa+OSYycnA1FXXWJKEEl+THw/xHl1
SORcWDJPaaoT/V/TeZ/8MgENrrRTxho6et7MsJFTD4rRCHf9WtZKDaSOPFWKOJ8C
AwEAAaOCAoIwggJ+MA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcD
AQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUsn2926q4GyQrK62/
Ehza8OeiusIwHwYDVR0jBBgwFoAUqEpqYwR93brm0Tm3pkVl7/Oo7KEwbwYIKwYB
BQUHAQEEYzBhMC4GCCsGAQUFBzABhiJodHRwOi8vb2NzcC5pbnQteDMubGV0c2Vu
Y3J5cHQub3JnMC8GCCsGAQUFBzAChiNodHRwOi8vY2VydC5pbnQteDMubGV0c2Vu
Y3J5cHQub3JnLzA5BgNVHREEMjAwghcqLmZ1bWVuZ3dhbmdsdW9rZWppLmNvbYIV
ZnVtZW5nd2FuZ2x1b2tlamkuY29tMEwGA1UdIARFMEMwCAYGZ4EMAQIBMDcGCysG
AQQBgt8TAQEBMCgwJgYIKwYBBQUHAgEWGmh0dHA6Ly9jcHMubGV0c2VuY3J5cHQu
b3JnMIIBAwYKKwYBBAHWeQIEAgSB9ASB8QDvAHUA8JWkWfIA0YJAEC0vk4iOrUv+
HUfjmeHQNKawqKqOsnMAAAFvTmPflQAABAMARjBEAiBb7yGozP13BfTnnLyK8NAt
7354QbWf0yNYOIiT8PP1UgIgDwwXhfsELGA8VFalChDw/P4z75ZsaaL/YpNi40x+
hGUAdgCyHgXMi6LNiiBOh2b5K7mKJSBna9r6cOeySVMt74uQXgAAAW9OY9+DAAAE
AwBHMEUCIDawc+ZKFIGhj8B84hSzUI9x76PNLzP+WYTR6DIv2d2cAiEAzYf9ZuAr
i6VB/fHPXj3aE2HBPYh46GjnDaad0V6ZxHwwDQYJKoZIhvcNAQELBQADggEBAI6v
gu2nJYMzokZi9pPcfoaQf9GiP/EOfLXSDZGZA3lG/kVhxhxuz1AOdDlQ7DPzz4dQ
Nt2DnloL/N2knJme6JAso5LEroDHUe5UunBLL7a2g8A8StslOvp3ofHfVgMCYT/Z
kqykQWZSrS5lmEbVhyvnA3BfTUp7AjPmeULdQ69pOCl0BwttZmEYNMjvVXzwOgCY
g/3796QgrUjebIeXlRPvZEj9TWlmOVCSQOVyZTLCFBmR0XGq3HNxK0G8h+ff086J
7Rkh2pOVSSbdgATjrb+hKqZDIQbEqZTvEIeFaNDBtnfPDtIy+2QH3Gef2iaL+iDe
ItIsAFakeCertificat=
-----END CERTIFICATE-----

-----BEGIN CERTIFICATE-----
MIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/
MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
DkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow
SjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT
GkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF
q6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8
SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0
Z8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA
a6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj
/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T
AQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG
CCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv
bTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k
c3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw
VAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC
ARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz
MDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu
Y3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF
AAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo
uM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/
wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu
X4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG
PfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6
ItIsAFakeCertificateFile========
-----END CERTIFICATE-----"""
    # CertType can be "CA" (CLIENT CERT) or "SVR" (SERVER CERT)
    req.CertType = "CA"
    # use your real project id, 0 is the id of default project
    req.ProjectId = 0
    # constant value, for this action, you must set it to "ssl"
    req.ModuleType = "ssl"

    resp = client.UploadCert(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
