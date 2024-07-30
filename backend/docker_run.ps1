docker run --name book-review-db -e POSTGRES_PASSWORD=admin -d --network=book-review postgres
docker run --name book-review-django -d -p 8000:8000 --network=book-review book-review-app