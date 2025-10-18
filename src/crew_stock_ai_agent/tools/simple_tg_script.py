import datetime
import requests


# MESSAGE = "Test"

# url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"

# payload = {
#     "chat_id": TG_CHANNEL_ID,
#     "text": MESSAGE
# }

# response = requests.post(url, data=payload)

# if response.status_code == 200:
#     print("Message sent successfully!")
# else:
#     print("Failed to send message:", response.text)

a = datetime.datetime.today().strftime('%Y-%m-%d')
print(a)