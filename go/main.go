package main

import (
"context"
"fmt"
openai "github.com/sashabaranov/go-openai"
)

func main() {
cfg := openai.DefaultConfig("sk-aetra-YOUR_API_KEY")
cfg.BaseURL = "https://api.aetraai.com/api/v1"
client := openai.NewClientWithConfig(cfg)

resp, err := client.CreateChatCompletion(
context.Background(),
openai.ChatCompletionRequest{
Model: "aetra-sonnet",
Messages: []openai.ChatCompletionMessage{
{Role: "user", Content: "Hello AetraAI!"},
},
},
)
if err != nil {
panic(err)
}
fmt.Println(resp.Choices[0].Message.Content)
}
