from unittest.mock import patch

from django.test import TestCase

from .models import ContactModel


class ContactFormTests(TestCase):
	@patch("myapp.views.send_mail", side_effect=OSError("SMTP unavailable"))
	def test_contact_submission_is_saved_when_email_fails(self, send_mail):
		response = self.client.post(
			"/contact/",
			{
				"name": "Alex Member",
				"email": "alex@example.com",
				"phone": "5551234567",
				"message": "I would like to join.",
			},
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Your message has been received")
		self.assertEqual(ContactModel.objects.count(), 1)
		enquiry = ContactModel.objects.get()
		self.assertEqual(enquiry.phone, "5551234567")
		send_mail.assert_called_once()
