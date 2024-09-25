NOTE: 

must have .env must have many api keys.



To generate (complexity) model, uncomment code in "scorer.py" in backend/utils/ and run it.


### DOCKER
- docker build -t azalea .
- heroku container:push web -a azalea-ai-ml
- heroku container:release web -a azalea-ai-ml