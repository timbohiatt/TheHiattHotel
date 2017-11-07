yes | docker system prune -a
docker build --no-cache -t thehiatthotel -f Dockerfile .
docker run -p 4000:80 thehiatthotel
