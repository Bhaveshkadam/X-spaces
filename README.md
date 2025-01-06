# X-spaces
You can download x spaces (Twitter Spaces) locally in your system.

## Step-by-Step Implementation

### 1. Install yt-dlp

Install `yt-dlp`, a popular and robust tool for downloading media:

```bash
pip install yt-dlp
```
Ensure ffmpeg is installed as yt-dlp uses it for downloading and processing media:
 - On Debian/Ubuntu:
```bash
sudo apt install ffmpeg
```
 - On MacOS:
```bash
brew install ffmpeg
```
### To set up and run the project locally, follow these steps:

 1. Prerequisites
Python 3.7+ installed on your system.
  Virtual Environment (optional but recommended).

2. Clone the Repository
   Clone the project repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. Set Up a Virtual Environment (Optional)
   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```
4. Install Required Packages
   Install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Application
   Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
   - Access the application at `http://127.0.0.1:8000`.
   - API documentation will be available at `http://127.0.0.1:8000/docs`.
