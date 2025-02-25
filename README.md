# Distance-Based Classification

## Overview
This project applies distance-based classification using various distance metrics while following best practices in version control, automation, containerization, and experiment tracking.

## Project Structure
```
├── distance_classification.py
├── test_script.py
├── Dockerfile
├── requirements.txt
├── .github/workflows/main.yml
├── distance_classification.ipynb  
├── data/
├── README.md
```

## Setup Instructions
### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd ML-Labs
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Classification Script
```sh
python distance_classification.py
```

---

## Automation with GitHub Actions
A GitHub Actions workflow is set up to automatically execute the classification script and validate changes.

### Workflow Configuration
Located at `.github/workflows/main.yml`, it performs:
- Dependency installation
- Running tests
- Executing Jupyter Notebook
- Logging results to Weights & Biases (WandB)

### Triggering the Workflow
This workflow runs automatically on every push.
To trigger manually:
```sh
git add .
git commit -m "Trigger CI/CD pipeline"
git push origin main
```

---

## Containerization with Docker
### Build and Run the Docker Container
```sh
docker build -t distance_classification .
docker run distance_classification
```

### Dockerfile
```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "distance_classification.py"]
```

---

---

## Tracking Results with Weights & Biases (WandB)
### Setup WandB
1. Sign up at [wandb.ai](https://wandb.ai/)
2. Obtain API Key from WandB Settings.
3. Initialize WandB in the script:
   ```python
   import wandb
   wandb.init(project='distance_classification_project')
   wandb.log({"Metric Score": score})
   ```
4. View experiment logs on your WandB dashboard.

---

### Sample WandB Screenshot:
![Screenshot 2025-02-25 214714](https://github.com/user-attachments/assets/6bc4d0d4-a1d1-402a-bbc3-7be9183e069a)
![Screenshot 2025-02-25 214639](https://github.com/user-attachments/assets/787742b9-9729-459f-b270-5b2c7c3ed200)
![Screenshot 2025-02-25 214609](https://github.com/user-attachments/assets/f078d568-dc64-4d58-bd7e-9eb63890660f)
![Screenshot 2025-02-25 214537](https://github.com/user-attachments/assets/1667608e-5539-441f-8a8b-12986e0805ca)




---

### License
MIT License. Contributions welcome!

---

Happy coding! 🚀
