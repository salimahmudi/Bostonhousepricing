# Boston House Pricing Prediction

## Software and Tools Requirements

Before starting the project, ensure the following tools are installed:

1. **[GitHub Account](https://github.com)** - Manage your code repositories.
2. **[Heroku Account](https://heroku.com)** - Deploy the application.
3. **[VSCode IDE](https://code.visualstudio.com/)** - Recommended IDE for editing your code.
4. **[Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)** - Command-line tool for Git operations.

## Project Setup Instructions

Follow the steps below to set up and run the **Boston House Pricing Project**.

### 1. Create a Conda Environment

```bash
conda activate development
```

Create a new Conda environment to manage project dependencies:

```bash
conda create -p venv python==3.7 -y
```

Explanation: This creates a virtual environment named `venv` with Python 3.7. The `-y` flag automatically confirms the installation.

### 2. Initialize Conda

Ensure Conda is properly initialized in your terminal:

```bash
conda init
```

Explanation: Initializes Conda in your shell. After running this command, restart the terminal.

### 3. Activate the Conda Environment

Activate the environment you created earlier:

```bash
conda activate C:\Users\salima\Desktop\Portfolio_Data_Analysis_Projects\Project4_EndToEndMachineLearningProject\housepricing\Bostonhousepricing\venv
conda activate C:\path\to\your\environment\venv
```

Explanation: Activates the `venv` environment. Replace the path with the correct location of your environment.

### 4. Install Required Libraries

Install the necessary libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Explanation: Installs libraries such as Flask, sklearn, pandas, etc., that are required for the project.

### 5. Set Up Git with GitHub

If you're using Git for version control, configure Git with your GitHub credentials:

```bash
git config --global user.name "salimahmudi"
git config --global user.email "salimahammoudi2025@gmail.com"
```

Explanation: These commands set your username and email for Git commits.

### 6. Add Files to Git

Add the files you want to track with Git:

```bash
git add .
```

Explanation: Stages all files in the current directory for a commit. You can also specify files individually.

### 7. Check Git Status

Check the status of your Git repository before committing:

```bash
git status
```

Explanation: Shows which files have been modified or added and which are ready to commit.

### 8. Commit Your Changes to Git

Commit your changes with a message:

```bash
git commit -m "Initial commit"
```

Explanation: Commits the changes with a descriptive message.

### 9. Push Code to GitHub

Push your local repository to GitHub:

```bash
git push origin master
git push origin main

```

Explanation: Pushes the `main` branch to your GitHub repository. Ensure the repository is already linked.

### 10. Run the Flask Application Locally

Start the Flask app:

```bash
flask run
```

Explanation: Runs the Flask development server. You can access the app locally at `http://127.0.0.1:5000`.

### 11. Deploy the Application to Heroku

Log in to your Heroku account:

```bash
heroku login
```

Explanation: Logs you into Heroku. A browser window will open for authentication.

### 12. Create a New Heroku App

Create a new Heroku app:

```bash
heroku create
```

Explanation: Creates a new app on Heroku. Heroku will assign a random name, or you can specify your own.

### 13. Push the Code to Heroku

Push your code to Heroku:

```bash
git push heroku main
```

Explanation: Pushes your code to Heroku for deployment. Heroku will detect the Python app and configure it automatically.

### 14. Open Your Application on Heroku

Once deployed, open your app in the browser:

```bash
heroku open
```

Explanation: Opens the deployed app’s URL in your browser.

## Conclusion

By following these steps, you will:

- Set up a Conda environment.
- Install the necessary libraries.
- Set up Git and push code to GitHub.
- Run the app locally using Flask.
- Deploy the app to Heroku for public access.

Feel free to modify the app or extend its functionality. Let me know if you run into any issues or need further assistance!

---

### Key Highlights:

- **Conda Setup**: Instructions for creating and activating the Conda environment with Python 3.7.
- **Git Configuration**: Setting up Git with your GitHub credentials and pushing changes.
- **Flask App**: Running the app locally with Flask and deploying it to Heroku.
- **Heroku Deployment**: Logging into Heroku, creating an app, and pushing code to Heroku for deployment.

This comprehensive **`README.md`** will guide you through setting up, running, and deploying your project.

---

Let me know if you need any additional modifications!