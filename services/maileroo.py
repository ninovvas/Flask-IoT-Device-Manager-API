import json

import requests
from decouple import config


# MailerSend API endpoint

class MailerooService:

    def __init__(self):
        self.MAILERSEND_API_URL = "https://smtp.maileroo.com/send"
        self.mailersend_api_key = config('MAILERSEND_API_KEY')
        self.from_email = config("FROM_EMAIL")
        self.to_email = config("TO_EMAIL")
        self.headers  = {"X-API-Key": self.mailersend_api_key}

        url = "https://verify.maileroo.net/check"

        data = {
            "api_key": config('MAILERSEND_API_KEY'),
            "email_address":  config("FROM_EMAIL")
        }

        response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

        print(response.text)

    def send_email(self, to_email, subject, body):

        data = {
            "from": {
                "email": self.from_email,
                "name": "My Flask Application"
            },
            "to": [
                {
                    "email": to_email,
                    "name": "Sensor Alert"
                }
            ],
            "subject": subject,
            'html': body
        }

        payload = {
            'from': 'From Name <niov.vasil@googlemail.com>',
            'to': 'To Name <ninov_16@yahoo.com>',
            'subject': 'Test Email',
            'plain': 'This is a test email.',
            'html': '<b>This is a test email.</b>'
        }

        try:
            response = requests.post(self.MAILERSEND_API_URL, json=payload, headers=self.headers)
            #response = requests.request("POST", self.MAILERSEND_API_URL, headers=self.headers, data=data)
            response.raise_for_status()  # Raise an error for bad status codes
            print("Email sent successfully:", response.json())
        except requests.exceptions.RequestException as e:
            print("Error sending email:", e)

    def notify_sensor_data_threshold(self, sensor_data, notify_value):
        if float(sensor_data["value"]) > float(notify_value):  # Example threshold
            self.send_email(
                to_email=self.to_email,
                subject="My Sensor Alert",
                body=f"Alert! This is my application! the <b>{sensor_data['sensor_name']}</b> sensor reading is too high: <b>{sensor_data['value']}</b>."
            )

