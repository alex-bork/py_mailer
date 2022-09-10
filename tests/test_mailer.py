import sys, os, unittest
sys.path.append(os.path.realpath('.'))
from mailer import SmtpMail
import configparser
from config_initiator import ConfigInitiator


ConfigInitiator(
    path=os.path.dirname(__file__),
    template=
        '''
        [SMTP]
        smtp_host=
        smtp_port=
        smtp_user=
        smtp_password=

        [MAIL]
        mail_recipient=
        mail_subject = "Test: py_mail"
        mail_text_html = "<h1>Test successful.</h1>"
        ''')

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),'config.ini'))

class Test_MailClass(unittest.TestCase):

    def test_send___with_plain_text_no_exception_raised(self):

        try:
            mail = SmtpMail(
                smtp_host = config['SMTP']['smtp_host'],
                smtp_port = config['SMTP']['smtp_port'],
                smtp_user = config['SMTP']['smtp_user'],
                smtp_password = config['SMTP']['smtp_password'],
                mail_recipients = [config['MAIL']['mail_recipient']],
                mail_subject = "py_mailer Test",
                mail_text = "Test with plain text content successful.")
            mail.send()
        except Exception as ex:
            self.fail(ex)

    def test_send___with_html_no_exception_raised(self):

        try:
            mail = SmtpMail(
                smtp_host = config['SMTP']['smtp_host'],
                smtp_port = config['SMTP']['smtp_port'],
                smtp_user = config['SMTP']['smtp_user'],
                smtp_password = config['SMTP']['smtp_password'],
                mail_recipients = [config['MAIL']['mail_recipient']],
                mail_subject = "py_mailer Test",
                mail_text_html = "<h1>Test with html content successful.</h1>")
            mail.send()
        except Exception as ex:
            self.fail(ex)

    def test_send___with_html_and_attachment_no_exceptions_raised(self):

        try:
            mail = SmtpMail(
                smtp_host = config['SMTP']['smtp_host'],
                smtp_port = config['SMTP']['smtp_port'],
                smtp_user = config['SMTP']['smtp_user'],
                smtp_password = config['SMTP']['smtp_password'],
                mail_recipients = [config['MAIL']['mail_recipient']],
                mail_subject = "py_mailer Test",
                mail_text_html = "<h1>Test with html content and attachment successful.</h1>")
            mail.add_attachment(config['MAIL']['mail_attachment_path'])
            mail.send()
        except Exception as ex:
            self.fail(ex)

    def test_send___value_error_raised(self):

        mail = SmtpMail(smtp_host=config['SMTP']['smtp_host'],
                smtp_port=config['SMTP']['smtp_port'],
                smtp_user=config['SMTP']['smtp_user'],
                #smtp_password=config['SMTP']['smtp_password'],
                mail_recipients=[config['MAIL']['mail_recipient']],
                mail_subject="py_mailer Test",
                mail_text_html="<h1>Test failed.</h1>")
        try:
            mail.send()
        except ValueError as ex:
            return
            
        self.fail(ex)


if __name__ == '__main__':
    unittest.main()