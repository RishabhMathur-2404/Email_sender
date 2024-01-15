from email import message

import pymongo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# MongoDB connection
client = pymongo.MongoClient("mongodb://UpswingProdUctIOnReAdwrItE7:Upswingb7mXhuVF8kFmKkzvYgMku5RXt9HZdMfGttA0@34.93.90.156:27017/?authSource=admin&readPreference=primary&directConnection=true&ssl=false&authMechanism=SCRAM-SHA-256")
db = client.upswing_staging
collection = db.daily_report

# Collection containing user emails
user_collection = db.users
# Fetch all user emails
user_emails = user_collection.find({}, {"email": 1})

# Fetch data from MongoDB
document = collection.find_one({})

# HTML Template with placeholders
html_template = """
<!DOCTYPE html
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset-utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modern HTML Email Templates </title>
  <style type="text/css">

body{{
  margin: 0;
  background: #cccccc;
}}
table{{
  border-spacing: 0;
}}
td{{
  padding: 0;
}}
img{{
  border: 0;
}}

.grid-container{{
  width: 100%;
  table-layout: fixed;
  /* background-color: #cccccc;
  padding-bottom: 60px; */
}}
.main{{
  background-color: #ffffff;
  margin: 0 auto;
  width: 100%;
  max-width: 600px;
  border-spacing: 0;
  font-family: sans-serif;
  color: #171a1b;
}}
.grid{{
  text-align: center;
  font-size: 0;
  justify-content: center;
  display: flex;
}}
/* .grid .col-6{{
  width: 100%;
  max-width: 300px;
  display: inline-block;
  text-align: center;
}} */


.grid-item {{
  background-color: white;
  padding: 20px;
  font-size: 30px;
  border-radius: 8px;

  border-radius: 8px;
  border: 1px solid #DBDBDB;
  background: #FFF;
  box-shadow: 0px 4px 4px 0px rgba(137, 137, 137, 0.05);
}}

/* .item1 {{
  grid-row: 1;
  width: 100px;
  height: 110px;
  flex-shrink: 0;
}}
.item2 {{
  grid-row: 1;
  width: 100px;
  height: 110px;
  flex-shrink: 0;
}}
.item3 {{
  grid-row: 1;
  width: 100px;
  height: 110px;
  flex-shrink: 0;
}}
.item4 {{
  grid-row: 1;
  width: 100px;
  height: 110px;
  flex-shrink: 0;
}} */

.icon {{
  margin-bottom: 3px;
}}

.icon-background {{
  background-color: #FCF1E7;
  width: 35px;
  height: 30px;
  border-radius: 5px;
  margin-top: -5px;
}}
.p1-text {{
  color: #F8A45A;
  font-family: Roboto;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 22px;
  /* 137.5% */
  letter-spacing: 0.5px;
  margin-top: 10px;
  text-align: left;
}}
h3 {{
  color: #4B4B4B;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 22px;
  /* 137.5% */
  letter-spacing: 0.5px;
  margin-top: 10px;
  text-align: left;
}}

.icon1-background {{
  background-color: #FFE7E7;
  width: 35px;
  height: 30px;
  border-radius: 5px;
  margin-top: -5px;
}}
.p2-text {{
  color: #E56875;
  font-family: Roboto;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 22px;
  /* 137.5% */
  letter-spacing: 0.5px;
  margin-top: 10px;
  text-align: left;
}}
.p3-text {{
  color: #C7C73A;
  font-family: Roboto;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 22px;
  /* 137.5% */
  margin-top: -5px;
  text-align: left;
}}
.icon3-background {{
  background-color: #FFFFD7;
  width: 35px;
  height: 30px;
  border-radius: 5px;
  margin-top: -5px;
}}
.icon4-background {{
  background-color: #E1F4FF;
  width: 35px;
  height: 30px;
  border-radius: 5px;
  margin-top: -5px;
}}
.p4-text {{
  color: #65BCF0;
  font-family: Roboto;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 22px;
  /* 137.5% */
  letter-spacing: 0.5px;
  margin-top: -5px;
  text-align: left;
}}

.two-col .last{{
  padding: 15px 0;
  align-items: center;
}}
.two-col .padding{{
  /* padding: 20px; */
  padding-bottom: 10px;
}}
.two-col .content{{
  font-size: 15px;
  line-height: 20px;
  text-align: center;
}}

.button{{
  background-color: white;
  color: #171a1b;
  text-decoration: none;
  padding: 5px 10px;
  border-radius: 5px;
  font-weight: bold;
}}
.button1{{
    background-color: #171a1b;
    color: white;
    text-decoration: none;
    padding: 5px 10px;
    border-radius: 5px;
    font-weight: bold;
}}

  </style>

</head>

<body>
  <div class="grid-container">
    <table class="main" width="100%">
      <tr>
        <td height="8" style="background-color: #171a1b;"></td>
      </tr>

      <tr>
        <td style="padding: 14px 0 4px;">
          <table width="100%">
            <tr>
              <td class="grid">
                <table class="col-6">
                  <tr>
                    <td>
                      <a href=""><img
                          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVXEZVR3eb0OPPVCDS52GqPKyI8fqUfilvmA&usqp=CAU"
                          alt="logo" width="140"></a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>

      <tr>
        <td>
          <a href="#"><img
              src="https://www.nucleustechnologies.com/blog/wp-content/uploads/2022/10/Outlook-Email-Template.jpg"
              alt="" width="600" style="max-width: 100%;"></a>
        </td>
      </tr>



      <tr>
        <td>
          <table width="100%">
            <td class="grid">
              <table class="col">
                <tr>
                  <td>
                    <div class="grid-item item1">
                      <div class="icon-background">
                        <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"
                          fill="none">
                          <path d="M2.5 3.75V16.244" stroke="#F8A45A" stroke-linecap="round" />
                          <path d="M17.5 7.5V16.25" stroke="#F8A45A" stroke-linecap="round" stroke-linejoin="round" />
                          <path d="M5 1.25H11.25" stroke="#F8A45A" stroke-linecap="round" stroke-linejoin="round" />
                          <path d="M5 18.75H15" stroke="#F8A45A" stroke-linecap="round" />
                          <path d="M17.5 16.25C17.5068 17.4986 16.25 18.75 15 18.75" stroke="#F8A45A"
                            stroke-linecap="round" stroke-linejoin="round" />
                          <path d="M2.5 16.25C2.5 17.5 3.75 18.75 5 18.75" stroke="#F8A45A" stroke-linecap="round"
                            stroke-linejoin="round" />
                          <path d="M2.5 3.74818C2.5 2.5 3.75 1.27784 5 1.25" stroke="#F8A45A" stroke-linecap="round"
                            stroke-linejoin="round" />
                          <path d="M17.4932 7.50561L11.25 1.25" stroke="#F8A45A" stroke-linecap="round"
                            stroke-linejoin="round" />
                          <path d="M11.25 5C11.2538 6.2432 12.505 7.5 13.75 7.5" stroke="#F8A45A" stroke-linecap="round"
                            stroke-linejoin="round" />
                          <path d="M11.25 5V1.25" stroke="#F8A45A" stroke-linecap="round" stroke-linejoin="round" />
                          <path d="M13.75 7.5H17.5" stroke="#F8A45A" stroke-linecap="round" stroke-linejoin="round" />
                          <path d="M5 16.25H8.75" stroke="#F8A45A" stroke-linecap="round" stroke-linejoin="round" />
                          <path d="M5 13.75H11.25" stroke="#F8A45A" stroke-linecap="round" stroke-linejoin="round" />
                          <path d="M5 11.25H8.75" stroke="#F8A45A" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                      </div>
                      <h3>Total Reservation</h3>
                      <p class="p1-text">{total_reservations}/280</p>
                    </div>
                  </td>
                </tr>
              </table>
              <table class="col">
                <tr>
                  <td>
                    <div class="grid-item item2">
                      <div class="icon1-background">
                        <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"
                          fill="none">
                          <path
                            d="M10.0002 3.33333C10.8842 3.33333 11.7321 3.68452 12.3572 4.30964C12.9823 4.93476 13.3335 5.78261 13.3335 6.66666C13.3335 7.55072 12.9823 8.39856 12.3572 9.02368C11.7321 9.64881 10.8842 9.99999 10.0002 9.99999C9.11611 9.99999 8.26826 9.64881 7.64314 9.02368C7.01802 8.39856 6.66683 7.55072 6.66683 6.66666C6.66683 5.78261 7.01802 4.93476 7.64314 4.30964C8.26826 3.68452 9.11611 3.33333 10.0002 3.33333ZM10.0002 11.6667C13.6835 11.6667 16.6668 13.1583 16.6668 15V16.6667H3.3335V15C3.3335 13.1583 6.31683 11.6667 10.0002 11.6667Z"
                            fill="#E56875" />
                        </svg>
                      </div>
                      <h3>Total Guest Count</h3>
                      <p class="p2-text">{total_guests}/196</p>
                    </div>
                  </td>
                </tr>
              </table>
              <table class="col">
                <tr>
                  <td>
                    <div class="grid-item item3">
                      <div class="icon3-background">
                        <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"
                          fill="none">
                          <path
                            d="M5.8335 15C4.44461 15 3.26405 14.5139 2.29183 13.5417C1.31961 12.5694 0.833496 11.3889 0.833496 10C0.833496 8.61111 1.31961 7.43056 2.29183 6.45833C3.26405 5.48611 4.44461 5 5.8335 5C6.9585 5 7.94127 5.31583 8.78183 5.9475C9.62239 6.57917 10.2091 7.37444 10.5418 8.33333H17.5002C17.9585 8.33333 18.351 8.49667 18.6777 8.82333C19.0043 9.15 19.1674 9.54222 19.1668 10C19.1668 10.5 18.9932 10.9028 18.646 11.2083C18.2988 11.5139 17.9168 11.6667 17.5002 11.6667V13.3333C17.5002 13.7917 17.3368 14.1842 17.0102 14.5108C16.6835 14.8375 16.2913 15.0006 15.8335 15C15.3752 15 14.9827 14.8367 14.656 14.51C14.3293 14.1833 14.1663 13.7911 14.1668 13.3333V11.6667H10.5418C10.2085 12.625 9.62155 13.4203 8.781 14.0525C7.94044 14.6847 6.95794 15.0006 5.8335 15ZM5.8335 11.6667C6.29183 11.6667 6.68433 11.5033 7.011 11.1767C7.33766 10.85 7.50072 10.4578 7.50016 10C7.50016 9.54167 7.33683 9.14917 7.01016 8.8225C6.6835 8.49583 6.29127 8.33278 5.8335 8.33333C5.37516 8.33333 4.98266 8.49667 4.656 8.82333C4.32933 9.15 4.16627 9.54222 4.16683 10C4.16683 10.4583 4.33016 10.8508 4.65683 11.1775C4.9835 11.5042 5.37572 11.6672 5.8335 11.6667Z"
                            fill="#C7C73A" />
                        </svg>
                      </div>
                      <h3>Total Keys Delivered</h3>
                      <p class="p3-text">{total_keys}</p>
                    </div>
                  </td>
                </tr>
              </table>
              <table class="col">
                <tr>
                  <td>
                    <div class="grid-item item4">
                      <div class="icon4-background">
                        <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"
                          fill="none">
                          <path
                            d="M3.33334 17.5C3.09723 17.5 2.89917 17.42 2.73917 17.26C2.57917 17.1 2.49945 16.9022 2.5 16.6667C2.5 16.4306 2.58 16.2325 2.74 16.0725C2.9 15.9125 3.09778 15.8328 3.33334 15.8333H4.16667V4.16667C4.16667 3.70833 4.33 3.31583 4.65667 2.98917C4.98334 2.6625 5.37556 2.49945 5.83334 2.5H14.1667C14.625 2.5 15.0175 2.66333 15.3442 2.99C15.6708 3.31667 15.8339 3.70889 15.8333 4.16667V15.8333H16.6667C16.9028 15.8333 17.1008 15.9133 17.2608 16.0733C17.4208 16.2333 17.5006 16.4311 17.5 16.6667C17.5 16.9028 17.42 17.1008 17.26 17.2608C17.1 17.4208 16.9022 17.5006 16.6667 17.5H3.33334ZM14.1667 15.8333V4.16667H10.4167V3.25C11.0278 3.36111 11.5278 3.64583 11.9167 4.10417C12.3056 4.5625 12.5 5.09722 12.5 5.70833V14.9583C12.5 15.3611 12.3681 15.7189 12.1042 16.0317C11.8403 16.3444 11.5069 16.5353 11.1042 16.6042V15.8333H14.1667ZM9.16667 10.8333C9.40278 10.8333 9.60084 10.7533 9.76084 10.5933C9.92084 10.4333 10.0006 10.2356 10 10C10 9.76389 9.92 9.56583 9.76 9.40583C9.6 9.24583 9.40223 9.16611 9.16667 9.16667C8.93056 9.16667 8.7325 9.24667 8.5725 9.40667C8.4125 9.56667 8.33278 9.76445 8.33334 10C8.33334 10.2361 8.41334 10.4342 8.57334 10.5942C8.73334 10.7542 8.93111 10.8339 9.16667 10.8333Z"
                            fill="#65BCF0" />
                        </svg>
                      </div>
                      <h3>Total Door Opened</h3>
                      <p class="p4-text">{total_doors}</p>
                    </div>
                  </td>
                </tr>
              </table>
            </td>
          </table>
        </td>
      </tr>
      <tr>
        <td style="background-color: #26292b; color: white;">
          <table width="100%">
            <tr>
              <td class="two-col last">

                <table class="col">
                  <tr>
                    <td class="padding">
                      <table class="content">
                        <tr>
                          <td>
                            <a href="#"><img
                                src="https://media.istockphoto.com/id/513055310/vector/thin-line-flat-design-banner-for-about-us-web-page.jpg?s=612x612&w=0&k=20&c=rpcoe2VFlWIxFchb1wwD82l2OwGENKZfv3kC55NBEDs="
                                alt="" width="600" style="max-width: 100%;"></a>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>

                <table class="col">
                  <tr>
                    <td class="padding">
                      <table class="content">
                        <tr>
                          <td>
                            <p style="font-weight:bold; font-size: 18px; margin-top: -1px;">Daily Report</p>
                            <p>
                              We monitor total reservations,
                              guest counts, key distributions, and gate operations,
                              ensuring every aspect of our service contributes to a seamless and secure experience
                              for
                              our guests."
                            </p>
                            <a href="#" class="button">Read More</a>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>

      <tr>
        <td style="padding: 15px 0 50px;">
          <table width="100%">
            <tr>
              <td style="text-align: center; padding: 15px;">
                <p style="font-size: 20px; font-weight:bold;">Your Opinion Matters to Us</p>
                <p style="line-height: 23px; font-size:15px; padding:5px 0 15px; ">Your opinions, suggestions, and ideas
                  are vital to help us improve and serve you better in the future.
                  Please follow this link to provide your feedback</p>
                <a href="#" class="button1">Share My Feedback</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>

      <tr>
        <td style="background-color: black;">
          <table width="100%">
            <tr>
              <td style="text-align: center; padding: 45px 20px; color: white;">
                <a href="#"><img
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVXEZVR3eb0OPPVCDS52GqPKyI8fqUfilvmA&usqp=CAU"
                    alt="logo" width="160"></a>
                <p style="padding: 10px;">Template</p>
                <p style="padding: 10px;">123 Street Road, City, State 000000</p>
                <p style="padding: 10px; font-size: 10px;">UNSUBSCRIBE</p>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </div>
</body>
</html>
"""

# Fetch data from MongoDB for the email content
document = collection.find_one({})

# Insert data into HTML
html_content = html_template.format(
    total_reservations=document["total_reservations"],
    total_guests=document["total_guests"],
    total_keys=document["total_keys"],
    total_doors=document["total_doors"]
)

# Email details
from_email = "rishabhmathur2404@gmail.com" # Your Gmail address
subject = "Test"

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "rishabhmathur2404@gmail.com"
smtp_password = "vxdm mhlz yrnq uzsd"

# Initialize SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Start TLS encryption
server.login(smtp_username, smtp_password)

# Send email to each user
for user in user_emails:
    if "email" in user:
        to_email = user["email"]

        # Create a MIMEMultipart message
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject

        # Attach HTML content
        part = MIMEText(html_content, 'html')
        message.attach(part)

        # Send email
        server.sendmail(from_email, to_email, message.as_string())

# Quit SMTP server
server.quit()
