# Code Snippet for Social Media experiment
Some useful script to get trending things on social media

# Activating a Virtual Environment on Windows

This guide provides instructions on how to activate a Python virtual environment on a Windows system.

## Step 1: Create a Virtual Environment

If you haven't already created a virtual environment, follow these steps:

1. **Navigate to your project directory**:
   Open **Command Prompt** or **PowerShell**, and change to the directory where you want to create the virtual environment:

   ```bash
   cd path\to\your\project
   ```
2. Create Virtual env
    ```bash
       python -m venv venv
    ```
3. Activate Virtual env
    ```bash
       venv\Scripts\activate
    ```
4. Using git bash
    ```bash
   source venv/Scripts/activate
    ```
5. To deactivate 
    ```bash
    deactivate
    ```
6. Install requirements.txt
    ```bash
    pip install -r requirements.txt
    ```
## Step 2: Running the Script
   
1. Run scrit using below command 
    ```bash
      python get_tweet_sentiment_analysis.py <start|stop|status> <instance_id>
   ```
