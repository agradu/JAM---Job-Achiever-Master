from unittest import mock
from email_module import Email


def test_send_email():
    email = Email("sender@example.com", ["receiver@example.com"], "Subject")
    password = "test_password"
    body = "Test email body"
    attachments = ["file1.pdf", "file2.pdf"]

    with mock.patch.object(email, "send") as mock_send:
        email.send(password, body, attachments)
        mock_send.assert_called_once_with(password, body, attachments)
