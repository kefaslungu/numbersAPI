# Number Classifier API  

## 🌍 Live URL  
**Base URL:** [`http://hngkefas.azurewebsites.net`](http://hngkefas.azurewebsites.net)  

## Overview  
The **Number Classifier API** provides interesting mathematical properties about a given number. It checks whether the number is **prime**, **perfect**, **Armstrong**, and more. It also fetches a **fun fact** from the **[Numbers API](http://numbersapi.com/)**.  

## Features  
* Determines if a number is **prime**  
* Checks if it's an **Armstrong number**  
* Identifies if it's **perfect** (sum of its divisors equals the number)  
* Classifies as **odd** or **even**  
* Computes the **sum of its digits**  
* Fetches a **fun fact** from the **[Numbers API](http://numbersapi.com/)**  

## API Endpoint  
### **GET /api/classify-number?number=371**  I will be using 371 through out, but feel free to change it.
**Example Response (200 OK):**  
```
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}
```
### **Error Response (400 Bad Request):**  
```json
{
  "number": "alphabet",
  "error": true
}
```
** Note:** Only valid integers are accepted.  

## Deployment  
The API is deployed on **Azure App Service** and supports **CORS**.  

## How to Run Locally  
1. Clone the repository:  
   ```
   git clone https://github.com/kefaslungu/numbersapi.git
   cd numbersapi
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:  
   ```bash
   python app.py
   ```
4. Access the API at:  
   ```
   http://127.0.0.1:5000/api/classify-number?number=371
   ```

## Tech Stack  
- **Backend:** Python (Flask)  
- **Deployment:** Azure App Service  
- **External API:** **[Numbers API](http://numbersapi.com/)**  