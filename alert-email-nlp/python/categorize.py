import openai
import pandas as pd

openai.api_key = "sk-REPLACE_THIS"

df = pd.read_csv("../output/log.csv")
for _, row in df.iterrows():
    prompt = f"Classify the urgency of this alert:\nSubject: {row['Subject']}\nBody: {row['Body']}"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"{row['Subject']}: {res.choices[0].message.content.strip()}")