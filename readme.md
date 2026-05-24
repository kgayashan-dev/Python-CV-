venv is already included with Python 3, so you usually do not need to install it separately on macOS.

You just create a virtual environment like this:

python3 -m venv .venv

⸻

Full Setup

1. Go to your project folder

cd ~/Documents/GitHub/COMPUTER\ VISION/Computer-Vision-Assignment-1

⸻

2. Create virtual environment

python3 -m venv .venv

This creates:

.venv/

inside your project.

⸻

3. Activate virtual environment

source .venv/bin/activate

Now terminal becomes:

(.venv)

⸻

4. Install packages inside .venv

python3 -m pip install opencv-python numpy matplotlib

⸻

5. Run your Python file

python3 task1.py

⸻

6. Exit virtual environment

deactivate

⸻

If venv gives error

Install/update Python properly:

brew install python

OR reinstall from:

Python Official Website￼

Then retry:

python3 -m venv .venv

⸻

Verify .venv Created

Run:

ls -a

You should see:

.venv

The -a shows hidden folders/files.