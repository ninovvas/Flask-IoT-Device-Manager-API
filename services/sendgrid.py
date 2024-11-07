from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class SendGridService:

    def __init__(self):
        # Initialize SendGrid client using the API key from environment variables
        self.sendgrid_api_key = config("SENDGRID_API_KEY")
        self.sendgrid_client = SendGridAPIClient(self.sendgrid_api_key)
        self.from_email = config("FROM_EMAIL")
        self.to_email = config("TO_EMAIL")
        self.template_id = config("SENDGRID_TEMPLATE_ID")

    # Define a function to send email
    def send_email(self, to_email, subject, body):
        from_email = self.from_email

        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=body,
        )

        message.template_id = self.template_id

        try:
            response = self.sendgrid_client.send(message)
            print(f"Status Code: {response.status_code}")
            print(f"Body: {response.body}")
            print(f"Headers: {response.headers}")
            return response.status_code
        except Exception as e:
            print(f"Error sending email: {e}")
            return None

    def notify_sensor_data_threshold(self, sensor_data, notify_value):
        if float(sensor_data["value"]) > float(notify_value):  # Example threshold
            self.send_email(
                to_email=self.to_email,
                subject="My Sensor Alert",
                body=f"Alert! This is my application! the <b>{sensor_data['sensor_name']}</b> sensor reading is too high: <b>{sensor_data['value']}</b>.",
            )
