curl --location --request POST 'http://100.26.242.75:8000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-d '{
"model": "gpt-3.5-turbo",
"temperature": 0.7,
"messages": [{"role": "user", "prompt":"ʲô���˹�����"}]
}'