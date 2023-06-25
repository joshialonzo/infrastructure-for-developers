docker build -t our-web-server -f web-server.Dockerfile .
docker run -d --name our-web-server -p 5001:5000 our-web-server