# AWS Deployment Notes

1. Create an ECR repository for each image (`apple-api`, `apple-webapp`).
2. Push images (the CD workflow does this on merge to main).
3. Run on EC2 with docker-compose, or ECS/Fargate with two services:
   - `api` (port 8000, internal only)
   - `webapp` (port 5000, behind an ALB or nginx)
4. Set `FASTAPI_URL` on the webapp to the internal address of the api service.
5. Store the model (`best.pt`) in S3 and download it at container start,
   or bake it into the api image.
