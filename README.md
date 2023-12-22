# audio_to_text_transcription
 Converting real-time audio or uploaded audio file audio to text using whisper in python
 
1. Create a Virtual Environment:
   First, set up a virtual environment in Anaconda to keep your project dependencies isolated. Open the Anaconda Navigator or a terminal and run the following commands:
   ```
   conda create --name myenv python=3.10
   conda activate myenv
   ```
   Replace `myenv` with the desired name for your virtual environment.

2. Install Required Packages:
   Install the necessary Python packages for your Streamlit app by running the following commands:
   ```
   pip install streamlit pydub sounddevice
   pip install scipy
   ```
   This ensures you have Streamlit, PyDub, Sounddevice, and SciPy installed in your virtual environment.

3. Install Git:
   Install Git, a version control system, using the following command:
   ```
   conda install git
   ```

4. Install Whisper (OpenAI's Speech Recognition):
   Install the Whisper library, which is used for speech recognition, with the following command:
   ```
   pip install git+https://github.com/openai/whisper.git
   ```

5. Install FFmpeg:
   Install FFmpeg, a multimedia framework, from the Conda Forge channel:
   ```
   conda install -c conda-forge ffmpeg
   ```
   This provides functionality for audio and video processing in your Streamlit app.

6. Run the Streamlit App:
   Finally, run your Streamlit app with the following command:
   ```
   streamlit run app.py 
   ```

   Replace `app.py` with the actual name of your Streamlit app script. This command starts the development server and opens the app in your default web browser.
   We can also add complete path of the file

By following these steps, you'll have a virtual environment with all the necessary dependencies installed, and you can run your Streamlit app seamlessly.
