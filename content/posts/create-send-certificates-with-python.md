---
title: "Generating (and Sending) Conference Certificates Using Python"
date: 2024-12-12T00:00:00-08:00
weight: 20
draft: false
menu:
  sidebar:
    name: "Generating (and Sending) Conference Certificates Using Python"
    identifier: create-send-certificates-with-python
    weight: 20
tags: ["Python","Third Party Libraries", "Learnings", "API", "Google Workspace", "Google Sheets", "Google Slides", "Automation", "Infrastructure"]
images:
- /images/posts/pyladiescon-certificate-2024.png
hero: /images/posts/pyladiescon-certificate-2024.png
---

## PyLadiesCon Certificate of Attendance

Not sure how common is this practice of giving out certificates to conference attendees. I've been attending mostly Python-related conferences in North America,
and we don't usually get any certificates here.
However, when I went to Python Brasil in Manaus 2022, they gave me a certificate of attendance.
And as a conference organizer, occasionally I'd receive request from a few attendees and volunteers about such certificate, saying that
their employer or school requires it as proof of attendance.

Since [PyLadiesCon](https://conference.pyladies.com) is a global event with participation from all over the world,
our team decided to send out certificates to all attendees, and not only to those who asked for it.

We also think that such a certificate could be a nice token of appreciation for the attendees, especially since we don't
currently give out swag. 

With more than 700 registered attendees, it's not feasible to create these certificates one by one. But thankfully,
we're also Python developers, so of course we write the code for doing it.

Event organizers, take note! Let me show you how to automatically generate certificates and send them via email to your
event attendees using Python.

## Tools we used

Here are the different tools we used for this project:

### Pretix

[Pretix](https://pretix.eu/about/en/) is our ticketing platform. We use the API to retrieve the list of attendees, their names, and their email address.

### Google Slides

We use Google Slides to create a template for the certificate. The idea is to simply update the name of the attendee on the certificate.
Since Google Slides has an APIs that allows you to add text to presentation slides.

### GMail

We need a way to send the certificate via email. We also want the email to be sent through the official PyLadiesCon
email address instead of from my personal GMail address. Another complexity is that the PyLadies GMail account
is a GSuite workspace account, so we need to use the GMail API to send the email. (eg we can't use ``smtplib`` for it).

### Google Sheets

We also want to send certificates to our volunteers and speakers, and we have been using Google Sheets to keep track
of the list of our volunteers and speakers.

### Google Drive

Google Drive is where we are store the certificate template. Since we will be copying/duplicating the template for each
attendee, I needed a way to organize all of those into one folder. We will use Google Drive API later.

### Python

I'm using Python 3.12.

### httpx

I use [httpx](https://www.python-httpx.org/) for making HTTP requests to the Pretix API. This is just a personal preference.
You can use the `requests` library if you prefer.

### google-api-python-client

This is the official Python client library for Google's discover based APIs. We will use this library
to interact with Google Sheets, Google Slides, Google Drive, and GMAIL APIs.

Docs: https://github.com/googleapis/google-api-python-client/blob/main/docs/README.md

```bash
python -m pip install -U google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Preparations

### Create a Google Slide Template

Before writing the code, first we need to come up with a template for the certificate. PyLadiesCon certificate template
is private, however, I've created this [sample certificate Google Slide template](https://docs.google.com/presentation/d/1B0g3bOS1iqZVCLmmgH142H8iq_5o5lIxNFLajRHSBOQ/edit?usp=sharing) that you can use. Make a copy of it,
or come up with your own template.

Here's the important part about the template: You need to have a placeholder text, which will be replaced with the attendee's name.
Make sure the placeholder text is a unique string that can be easily searched and replaced. You may want to use some symbols
to make it unique, basically some kind of text that you know will not appear in the certificate text.

If you look at the [sample certificate template](https://docs.google.com/presentation/d/1B0g3bOS1iqZVCLmmgH142H8iq_5o5lIxNFLajRHSBOQ/edit?usp=sharing) I created,
you'll notice that I used texts like `{{ blog-reader }}` and ``{{ issue-date }}`` as the placeholder text. Feel free to
have as many or as few placeholder text needed.

### Prepare a Google Sheets with the list of attendees and email address

The Sheet should have at least two columns: the name and email address of the attendee. For PyLadiesCon, we have an additional
column to indicate the role of the person, e.g. if they were a speaker, or a volunteer.

Here's [an example spreadsheet](https://docs.google.com/spreadsheets/d/15OgiejruaPCSL00bU2QliAc-hbmmWplmZ_f3khhvOTw/edit?usp=sharing) that
you can use for following along on this blog post.

### Prepare an email template to the attendee

You may want to prepare an email template that you can use to send the certificate to the attendee. The email could
include message like "Thank you for attending my event. Attached is your certificate of attendance.".

### Get Pretix API Token

You can get the API token from Pretix by going to your event dashboard > Teams > click on the team name.

Read the docs about [Pretix Token authorization](https://docs.pretix.eu/en/latest/api/tokenauth.html).

### Create a Google Cloud Project and Enable the APIs

We need to enable certain APIs: Google Sheets, Google Slides, Google Drive, and GMail.

This could be a bit tricky and time-consuming (and also confusing) the first time you do it. But,
once you have created the project, and obtained
the credentials, you can reuse it for other projects.

I won't get into detail on how to create the project and enable the APIs, as it's already well documented in the Google Cloud docs.

If you go to each of the API docs for the above products, there are links and buttons for enabling the APIs. Go there,
click the buttons, and follow through the steps.

- [Google Sheets Python quickstart](https://developers.google.com/sheets/api/quickstart/python)
- [Google Slides Python quickstart](https://developers.google.com/slides/api/quickstart/python)
- [GMail Python quickstart](https://developers.google.com/gmail/api/quickstart/python)
- [Google Drive Python quickstart](https://developers.google.com/drive/api/quickstart/python)

## Pseudocode

For now, we just want to create and send certificates to event attendees.

Pseudocode for creating and sending certificates to attendees.

1. Get the list of attendees from Pretix
2. For each attendee:
   - copy the certificate Google Slide template
   - add the attendee name on the certificate
   - download the certificate as PDF
   - send the PDF certificate via email to the attendee



## Setting up Google APIs with Python client library

Set up the code for working with the various Google APIs: GDrive, Google Sheets, GMail, and Google Slides.

```python
# import the necessary libraries
import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# These are the different scopes we need for the different Google APIs

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]
GSLIDES_TEMPLATE_ID = "" # Google Slide template ID. 
GSHEETS_ID = "" # Sheet containing names and email address.

# "credentials.json" is the credentials you get after you created the Google Cloud project
credentials = None

def authorize_google():
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

authorize_google()

gdrive_service = build("drive", "v3", credentials=credentials)
gslides_service = build("slides", "v1", credentials=credentials)
gmail_service = build("gmail", "v1", credentials=credentials)
gsheets_service = build("sheets", "v4", credentials=credentials)
```

## Create a Pretix Wrapper

I don't think there's a client library for Pretix yet, so I created a simple wrapper for it.

```python
import httpx

BASE_PRETIX_URL = "https://pretix.eu/api/v1/"

organizer_name = "pyladiescon"  # Change this to your organizer name on Pretix
event_name = "2024"  # Change this to your event name on Pretix

class PretixWrapper:
    def __init__(self, token):
        self.headers = {"Authorization": f"Token {token}"}

```

## Get the orders from Pretix using the wrapper

I added the `get_orders` function to call the "[List of all orders](https://docs.pretix.eu/en/latest/api/resources/orders.html#list-of-all-orders)"
API endpoint from pretix. Since the resource is paginated,
I added a while loop there.

```python
class PretixWrapper:
    ...

    def get_orders(self):
        has_response = True
        url = BASE_PRETIX_URL + f"organizers/{organizer_name}/events/{event_name}/orders/"
        index = 0
        while has_response:
            response = httpx.get(url, headers=self.headers)
            url = response.json()["next"]
            has_response = url is not None
            for r in response.json()["results"]:
                index += 1
                yield r
```

Call the API:

```python
import os
# get the token from env variable
# you can hardcode it too, but people always forget to remove it before committing
PRETIX_TOKEN = os.getenv("PRETIX_TOKEN")

# instantiate the pretix wrapper class
pretix_wrapper = PretixWrapper(PRETIX_TOKEN)
response = pretix_wrapper.get_orders()

for order in response:

    # an order could have multiple items, eg if they purchase more than one ticket
    items = order["positions"]

    payment_confirmed = False

    for payment in order["payments"]:
        # we only want to send certificate to attendees who finished the ticketing process (not withdrawn, not cancelled)
        if payment["state"] == "confirmed":
            payment_confirmed = True

    if payment_confirmed:
        for item in items:
            # Depending on how you configure your ticket on pretix, you might get different fields returned.
            # Check the API response to see what fields are available to you
            attendee_name = item["attendee_name"]
            order_id = item["order"]
            position_id = item["positionid"]
            email = item["attendee_email"]
```

I decided to keep track of the attendee's order id and the position id, because I know that this is a unique identifier
for each attendee. I use this later to determine whether the certificate for this person has been generated or not,
so I don't end up with duplicated certificate for the same person.

## Copy the Slide Template

From the above code, I now have the attendee's name. This is good enough information to begin copying the Google Slide
template.

```python

def copy_presentation(source_presentation_id, filename):
    body = {"name": filename}
    drive_response = (
        gdrive_service.files().copy(fileId=source_presentation_id, body=body).execute()
    )
    presentation_copy_id = drive_response.get("id") # the id of the newly created presentation
    return presentation_copy_id

# Use the Pretix order id and position id as the filename for the certificate
filename = f"{order_id}-{position_id}" 
new_slide_id = copy_presentation(GSLIDES_TEMPLATE_ID, filename)
```

## Update the Slide with the Attendee's Name

Now that the certificate template has been copied, we can update it with the attendee's actual name.
What we want to do now is to search for the placeholder text in the slide, and replace it with the attendee's name.

First, prepare the Google Slides request payload.

In my example [Google Slides Template](https://docs.google.com/presentation/d/1B0g3bOS1iqZVCLmmgH142H8iq_5o5lIxNFLajRHSBOQ/edit?usp=sharing),
My placeholder texts are: ``{{blog-reader-name}}``, and ``{{issue-date}}``.

You'll want to adjust the placeholder text and the payload below to match your own template.
Below is an example for replacing the ``{{blog-reader-name}}`` placeholder with the attendee name, and the ``{{issue-date}}``
with today's date.

The important part to look at is the `"replaceAllText"` key in the request payload. Basically, we're telling Google to look
for the specified placeholder text, and replace it with the new text. This is why you need to have a unique placeholder text
and a text that doesn't appear anywhere else in the slide. Using symbols like `{{ }}` could help with making it unique.

```python
from datetime import datetime
requests = [
    {
        "replaceAllText": {
            "containsText": {
                "text": "{{blog-reader-name}}",
                "matchCase": True,
            },
            "replaceText": attendee_name,
        }
    },
    {
        "replaceAllText": {
            "containsText": {
                "text": "{{issue-date}}",
                "matchCase": True,
            },
            "replaceText": f"{datetime.now():%B-%d, %Y}",
        }
    },
]
```

Call Google Slides API to update the slide, passing the above request payload.

```python

body = {"requests": requests}
response = gslides_service.presentations().batchUpdate(
    presentationId=new_slide_id,
    body=body).execute()
```

After this, you should see the certificate updated with the attendee name in Google Drive.

## Download the Google Slide presentation as a PDF File

Maybe you don't want the attendee to know that their certificate was created using Google Slides, so you want to
create PDF version of it.

You can download and export the Google slide as a PDF file using Python.
GDrive API has the `export` method that you can call to do this.

```python
stream = gdrive_service.files().export(fileId=new_slide_id, mimeType="application/pdf").execute()
with open(f"{filename}.pdf", "wb") as f:
    f.write(stream)
```

After this, you should see the PDF file downloaded in the same directory as your script.

## Send the PDF Certificate using GMail

Now it's time to send the certificate to the attendee. Do you have the email message ready?

I'll show you how to send the email in both plain text and HTML format.


```python
from textwrap import dedent

email_message_plain = dedent(f"""
    Dear {attendee_name},
    
    Thanks for reading my blog post. Here is your certificate of appreciation.
    
    Regards,
""")

email_message_html = dedent(f"""
    <p>Dear {attendee_name},</p>
    <p>Thanks for reading my blog post. Here is your certificate of appreciation.</p>
    <p>Regards,</p>

""")
```

Create a helper function for sending email using the GMail API, and also add an attachment to the email

```python
import base64
from email.message import EmailMessage

def send_email(subject, sender_name, sender_email, body_plain, body_html, recipients, filename):
    message = EmailMessage()
    
    # send both plain text and html email
    message.set_content(body_plain)
    message.add_alternative(body_html, subtype="html")

    # load the pdf file and attach it to the email
    with open(f"{filename}.pdf","rb") as f:
        content = f.read()
        message.add_attachment(content, maintype="application", subtype="pdf", filename=f"{filename}.pdf")

    # create the email message, setting the subject, from, and to
    message["Subject"] = subject
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = ", ".join(recipients)

    # prepare the payload to the GMail API
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    gmail_body = {"raw": encoded_message}

    # send the email
    gmail_service.users().messages().send(userId="me", body=gmail_body).execute()
```

Now to actually send the email.

```python

send_email(
    subject="Thanks for reading my blog!",  # Use some catchy subject so they'll read it
    sender_name="Mariatta",  # Change this to your own email address
    sender_email="",  # Your Gmail email address
    body_plain=email_message_plain,
    body_html=email_message_html,
    recipients=[attendee_email],  # the email address of the attendee from Pretix
    filename=filename,  # the certificate pdf filename
)
```

Run the script to send the email.

My trick is to first hardcode the recipient email address to my own personal email address so I know it would work. 
I would also add something like "TEST" to the subject line.

Once I'm confident that the email is being sent correctly, I then change it to the actual recipient's email address and
use the proper subject line.

## Reading attendee list from Google Sheets

What if you don't use Pretix? No problem. As mentioned above, for PyLadiesCon, we also needed to send certificates to
our volunteers and speakers, and this info wasn't on Pretix.

Let me show you how to read the list of names and email address from Google Sheets.

I'm using my [example spreadsheet](https://docs.google.com/spreadsheets/d/15OgiejruaPCSL00bU2QliAc-hbmmWplmZ_f3khhvOTw/edit?usp=sharing)
which has only two columns, the name and email address.

```python

sheet = gsheets_service.spreadsheets()
result = (
    sheet.values()
    .get(spreadsheetId=GSHEETS_ID, range="Certificate Recipients!A2:C200")  # adjust the range to match your sheet
    .execute()
)

values = result.get("values", [])
for row in values:
    attendee_name = row[0]
    attendee_email = row[1]

```

The above code will read the list of names and email address from the Google Sheet, extracting their name and email address.

You can then use the same code as above to copy the Google Slide template, update the slide with the attendee's name.


## The complete script

I've created a [gist](https://gist.github.com/Mariatta/a9884994f8bb85fcedeea796f5f74a08) with the complete script that combines all the above code snippets. 

If you want to see the actual code we used for PyLadiesCon, check it out at the [pyladies/global-conference-infra](https://github.com/pyladies/global-conference-infra) repo:
https://github.com/pyladies/global-conference-infra/blob/main/certificates2024/util.py

## Conclusion

Sending certificates of participation is a nice gesture to show your appreciation.
It's a nice token for saying thank you to your attendees, speakers, and volunteers, and it doesn't cost much to create.
The certificate can be shown to their boss, employer, school, etc as proof that they participated in your event.
If you are an event organizer, I'd recommend you look into generating these certificates to your attendees.

Here's what Laura Funderburk, one of [PyLadiesCon](https://conference.pyladies.com) conference speakers, says about the certificate.

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7273058089929482241" height="608" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>

Other conference attendees have also proudly shared on social media about their certificates. I think it shows that such
certificate is indeed appreciated.

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7273048454145146880" height="681" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7272537021942820864" height="543" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>