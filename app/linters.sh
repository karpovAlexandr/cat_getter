source venv/bin/activate

echo "running black"
black .

echo "running isort"
isort --profile black .