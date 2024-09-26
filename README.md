NOTE: 

must have .env must have many api keys.



To generate (complexity) model, uncomment code in "scorer.py" in backend/utils/ and run it.


### DEPLOYING BACKEND USING DOCKER
Test locally:
- docker build -t azalea .
Deploy:
- docker build --platform linux/amd64 -t registry.heroku.com/azalea-ai-ml/web . && docker push registry.heroku.com/azalea-ai-ml/web && heroku container:release web -a azalea-ai-ml

Current attempt:
docker buildx build --platform linux/amd64 -t registry.heroku.com/azalea-ai-ml/web . --push && heroku container:release web -a azalea-ai-ml


### ADDING API KEYS TO ```Heroku```
