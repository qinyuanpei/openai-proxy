curl --location --request POST 'http://100.26.242.75:8000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-d '{
"model": "text-davinci-002",
"prompt":"ʲô���˹�����",
"max_tokens": 1024,
"temperature": 0.7,
"messages": [{"role": "user", "prompt":"ʲô���˹�����"}]
}'