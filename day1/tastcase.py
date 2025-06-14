import unittest
from solution import extract_emails

class TestExtractEmails(unittest.TestCase):

    def test_single_email(self):
        self.assertEqual(extract_emails("Contact me at test@example.com"), ["test@example.com"])

    def test_multiple_emails(self):
        text = "Emails: a@a.com, b.b@domain.net, user+1@site.org"
        expected = ["a@a.com", "b.b@domain.net", "user+1@site.org"]
        self.assertEqual(extract_emails(text), expected)

    def test_no_emails(self):
        self.assertEqual(extract_emails("There is no email here!"), [])

    def test_malformed_email(self):
        text = "wrong@com, valid@mail.com"
        self.assertEqual(extract_emails(text), ["valid@mail.com"])

    def test_email_with_subdomain(self):
        text = "Send to dev@mail.support.org"
        self.assertEqual(extract_emails(text), ["dev@mail.support.org"])

if __name__ == '__main__':
    unittest.main()