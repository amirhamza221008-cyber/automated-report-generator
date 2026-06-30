import openai, os

def get_summary(stats: dict) -> str:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
    Tum ek business analyst ho. Ye data stats hain:
    {stats}
    Ek 3-4 line ka executive summary likho — key insights, trends, aur recommendation.
    """
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content