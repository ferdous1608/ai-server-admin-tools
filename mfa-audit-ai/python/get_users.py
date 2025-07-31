import requests
import pandas as pd
from msal import ConfidentialClientApplication

TENANT_ID = "your-tenant-id"
CLIENT_ID = "app-client-id"
CLIENT_SECRET = "secret"

authority = f"https://login.microsoftonline.com/{TENANT_ID}"
scopes = ["https://graph.microsoft.com/.default"]

app = ConfidentialClientApplication(
    CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET
)

token = app.acquire_token_for_client(scopes=scopes)["access_token"]

url = "https://graph.microsoft.com/v1.0/reports/credentialUserRegistrationDetails"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
with open("mfa_users.csv", "w") as f:
    f.write(response.text)

print("Saved MFA report to mfa_users.csv")