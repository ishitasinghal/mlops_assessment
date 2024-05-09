## How to run

```bash
docker build -t mlops .
docker run --rm -it -p 7860:7860 -p 5000:5000 mlops
```

## How to test

```bash
wget --no-check-certificate --quiet \
  --method POST \
  --timeout=0 \
  --header 'Content-Type: application/json' \
  --body-data '{
    "url": "https://raw.githubusercontent.com/ishitasinghal/mlops_assessment/gradio/digits/8.png"
}' \
   'http://localhost:5000/predict'
```


## Screenshots

![Postman](/docs/postman.png?raw=true "Postman")
![Gradio UI](/docs/browser.png?raw=true "Gradio UI")
![K3S Deployment](/docs/k3s.png?raw=true "Kubernetes Resources")