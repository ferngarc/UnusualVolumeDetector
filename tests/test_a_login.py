from ftplib import FTP


def test_try_logging_in():
    ftp = FTP("ftp.nasdaqtrader.com")
    resp = ftp.login()
    assert "230 User logged in." in resp

