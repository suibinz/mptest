
import pytest

@pytest.fixture
def smtp():
	import smtplib
	yield smtplib.SMTP("smtp.gmail.com")
	print("Teardown smtp")
	smtp.close()

def test_ehlo(smtp):
	response, msg = smtp.ehlo()
	assert response == 250
	assert 0 

test_ehlo(smtp)