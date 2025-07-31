import openai
import pandas as pd
import json

# Load API key
with open("../config.json") as f:
    config = json.load(f)
openai.api_key = config["api_key"]

# Load logs
df = pd.read_csv("../logs/system_logs.csv")
logs_text = "\n".join(df["Message"].dropna().tolist()[:10])

# Call OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": f"Summarize these Windows logs:\n{logs_text}"}]
)

print(response.choices[0].message.content)