# global-entry-lambda

global entry checker deployed to lambda

## Notes

- This is very specific to my timeframes and locations
- I never had to deploy this, I found appointments just because I was developing this and running it
- To run:
  1. set up a virtualenv
  2. install `python-lambda-local` into the venv
  3. Set up a twilio account with a phone number you can sms from
  4. Run command: `TWILIO_ACCOUNT_SID=??? TWILIO_AUTH_TOKEN=??? TWILIO_TEXT_FROM=+??? TWILIO_TEXT_TO=+??? python-lambda-local -f lambda_handler appointments.py event.json`
  5. Or comment out the creation of the twilio.client and create message on the client if you just want to run locally
