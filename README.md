# Vintage Tag Analyzer

This web application analyzes images of military and vintage tags using AI. Upload an image, and the app will provide details about the item, its history, and its estimated value.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/tien1868/vintage_tag_analyzer)

---

## 🚀 How to Deploy Your Own Version

You can deploy your own instance of this application with a single click.

1.  **Click the "Deploy to Render" Button**: Click the button above to start the deployment process on Render.
2.  **Connect Your GitHub Account**: You'll be prompted to connect your GitHub account to Render.
3.  **Create the Web Service**: Give your new service a name and click "Create Web Service". Render will automatically use the settings from your repository to build and deploy the application.
4.  **Add Environment Variables**: Once the service is created, go to the "Environment" tab and add your API keys:
    *   `OPENAI_API_KEY`: Your key from OpenAI.
    *   `XAI_API_KEY`: (Optional) Your key from xAI.
5.  **Wait for Deployment**: Render will automatically redeploy your application with the new environment variables. Once it's live, you'll have your own public URL.

## 🛠️ Local Development

To run this application on your local machine:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/tien1868/vintage_tag_analyzer.git
    cd vintage_tag_analyzer
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables**:
    Create a `.env` file in the root of the project and add your API keys:
    ```
    OPENAI_API_KEY="your_openai_key_here"
    XAI_API_KEY="your_xai_key_here"
    ```

4.  **Run the Application**:
    ```bash
    gunicorn app:app
    ```

    The application will be available at `http://127.0.0.1:8000`.

