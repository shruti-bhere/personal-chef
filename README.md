#  AI Personal Chef Agent

A smart recipe assistant built with **Python**, **LangGraph**, and **Google Gemini**.

This agent acts as your culinary expert. You provide ingredients (e.g., *"potatoes and gram flour"*), and the agent suggests creative recipes. It uses a **ReAct (Reason + Act)** workflow: if it knows the recipe, it tells you immediately; if not, it autonomously searches the web using **Tavily** to find the best instructions.

---

##  Step 1: Install Requirements

You need to tell Python which libraries to use.

1.  **Create the file:** Create a new file named `requirements.txt` in your project folder.

2.  **Add the library names:** Paste the following list into `requirements.txt`:
    ```text
    langchain
    langchain-google-genai
    langchain-community
    langgraph
    tavily-python
    python-dotenv
    google-generativeai
    ```

3.  **Install them:** Open your terminal and run this command:
    ```bash
    pip install -r requirements.txt
    ```

---

##  Step 2: Configure API Keys

The agent needs keys to access Google (The Brain) and Tavily (The Searcher).

1.  **Create the file:** Create a new file named `.env` (note the dot at the start).

2.  **Add your keys:** Paste your keys inside like this:
    ```ini
    GOOGLE_API_KEY=AIzaSy...  <-- Replace with your actual key
    TAVILY_API_KEY=tvly-...   <-- Replace with your actual key
    ```

---

##  Step 3: Run the Application

This project runs in your terminal (CLI).

1.  **Run the command:** Type this in your terminal and hit Enter:
    ```bash
    python main.py
    ```

2.  **How to use it:**
    * You will see a prompt: `User >`
    * **Step A (Ingredients):** Type "I have chicken and rice, what can I make?"
    * **Step B (Specifics):** Ask "Find me a spicy recipe for this."
    * **Step C (Exit):** Type `q` or `quit` to stop the program.

---

## Troubleshooting Common Errors

###  Error: `ValueError: TAVILY_API_KEY is missing`
**Reason:** You forgot to put the keys in the `.env` file, or the file is named wrong.
**Solution:** Check that your file is exactly named `.env` (not `.env.txt`) and has values inside.

### Error: `404 Model Not Found`
**Reason:** The code might be