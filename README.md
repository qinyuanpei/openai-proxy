# openai-proxy

一个非常简单的项目，旨在解决国内访问 ChatGPT API 的问题，原理是利用 FastAPI 封装了一个原汁原味的 API 接口，只要这个程序部署在国外的服务器上，你就可以没有任何通过地访问 ChatGPT API。如果你没有独立地服务器，还可以使用 Vercel 这种拥有免费额度的服务，你唯一需要做的事情就是在 Vercel 中导入本项目。

# 使用方法
像使用官方 API 接口一样：

```
curl --location --request POST 'https://<Your-Domain.com>/openai/v1/completions' \
-H 'Authorization: Bearer <Your-OpenAI-API-KEY>' \
-H 'Content-Type: application/json' \
-d '{
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content":"Hello ChatGPT!"}]
}'
```

接口返回值：
```
{
    "code": 200,
    "message": "Success",
    "data": {
        "id": "chatcmpl-6to825KCIKMjbxgI6ZCfmzJnisXMj",
        "object": "chat.completion",
        "created": 1678758754,
        "model": "gpt-3.5-turbo-0301",
        "usage": {
            "prompt_tokens": 13,
            "completion_tokens": 11,
            "total_tokens": 24
        },
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "\n\nHello! How can I assist you today?"
                },
                "finish_reason": "stop",
                "index": 0
            }
        ]
    }
}
```



