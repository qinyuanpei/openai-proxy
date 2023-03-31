# openai-proxy

一个非常简单的项目，旨在解决国内访问 ChatGPT API 的问题，原理是利用 FastAPI 封装了一个原汁原味的 API 接口，只要这个程序部署在国外的服务器上，你就可以无痛地访问 ChatGPT API。如果你没有独立地服务器，还可以使用 Vercel 这种拥有免费额度的服务，你唯一需要做的事情是在 Vercel 中导入本项目。

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/qinyuanpei/openai-proxy)

# 使用方法
像使用官方 API 接口一样：

```curl
curl --location --request POST 'https://<Your-Domain.com>/v1/completions' \
-H 'Authorization: Bearer <Your-OpenAI-API-KEY>' \
-H 'Content-Type: application/json' \
-d '{
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content":"Hello ChatGPT!"}]
}'
```

接口返回值：
```json
{
    "id": "chatcmpl-702Bzns9pSGqvLeUVk5tTX3BBmQ1I",
    "object": "chat.completion",
    "created": 1680242783,
    "model": "gpt-3.5-turbo-0301",
    "usage": {
        "prompt_tokens": 56,
        "completion_tokens": 25,
        "total_tokens": 81
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "嗨！你好，有什么我能为你提供帮助的吗？"
            },
            "finish_reason": "stop",
            "index": 0
        }
    ]
}
```



