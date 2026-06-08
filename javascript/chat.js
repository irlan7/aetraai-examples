import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "sk-aetra-YOUR_API_KEY",
  baseURL: "https://api.aetraai.com/api/v1",
});

const response = await client.chat.completions.create({
  model: "aetra-sonnet",
  messages: [{ role: "user", content: "Hello AetraAI!" }],
});
console.log(response.choices[0].message.content);
