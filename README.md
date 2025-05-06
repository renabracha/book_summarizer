# Book Summarizer

## Acknowledgment
I would like to thank the following individuals and organisations that made this project possible. 
* Groq for providing me free access to their API key and thereby allowing me to gain hands-on experience in making API calls without having to constantly worry about token limits.
* Google Books for enabling me to perform full-text searches on book content on the Web using their free API.

## Abstract
This project was inspired by discovering a barcode scanner app on my Android phone. It uses scanned ISBNs and prompt engineering techniques to retrieve and summarize book information. The key feature is a 300-word synopsis, written in an engaging tone to spark the reader’s interest in the book. All information is displayed in a clean, user-friendly web app interface.

<br>

The application follows this sequence:
1. Prompt the user to enter an ISBN.
2. Retrieve book information using the Google Books API.
3. Generate a synopsis of the book.

## Development Notes
* The barcode scanner used is a mobile app on my Android device. A future improvement could involve connecting the phone or an external scanner to automatically feed ISBNs into the application.
* It was engaging to experiment with the synopsis generation prompt — adjusting its tone to sound anywhere between a neutral book blurb and an enthusiastic sales pitch.
* I developed and tested the prototype in a Jupyter Notebook on Google Colab, taking advantage of GPU support (T4). This made it easy to debug the code step-by-step.
* After completing the notebook version, I converted the code into a `.py` script so the program could run independently.
* I explored multiple secure methods of accessing API keys and used **Streamlit** to build a simple web interface that allows users to interact with the tool easily.

## Installation
To run book_summarizer.py, do the following:

### Step 1. Place the files in a folder. 
1. Place the `.py` file in a local folder (e.g. `C:\temp\book_summarizer`).
2. Create a file called `.env` and place the GROQ API key in the following format:
	`GROQ_API_KEY = <groq_api_key>`
3. Place the `.env` file in the same local folder. 

### Step 2. Install Python. 
1. In Windows, open the Command Prompt window.
2. Make sure Python is installed. In the Command Prompt window, type:
	`python --version`
If you get an error or "Python is not recognized", you need to install Python:
	1. Go to `https://www.python.org/downloads/`.
	2. Download the latest Python installer for Windows
	3. Run the installer and make sure to check `Add Python to PATH` during installation

### Step 3. Set up a virtual environment. 
This keeps your project dependencies isolated:
1. In the Command Prompt window, go to the script folder. Type:<br>
	`cd C:\<path to your script folder>`
2. In the Command Prompt, create a Python virtual environment named `book_summarizer_env`.<br>
	`python -m venv book_summarizer_env`
3. In the Command Prompt, activate the Python virtual environment.<br>
	`book_summarizer_env\Scripts\activate`
4. Install the required dependencies.<br>
  `pip install -r requirements.txt`

### Step 4. Run the script. 
1. In the Command Prompt window, run the Streamlit application. Type:<br>
	`streamlit run book_summarizer.py`
<br>
<br>
This will start a local web server and open the application in your browser. Press the Analyse button to view the results. 

## Web app in action
![Alt text for screen reader](https://github.com/renabracha/book_summarizer/blob/main/sceenshot_1.JPG?raw=true)
![Alt text for screen reader](https://github.com/renabracha/book_summarizer/blob/main/sceenshot_2.JPG?raw=true)