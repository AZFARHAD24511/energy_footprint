# Energy Process Explorer

A Streamlit dashboard to explore energy‐intensive processes:

- Filter by keyword
- View table of matching processes
- Bar charts for production energy input and energy content

## Deploy on Streamlit Cloud

1. Push this repo to GitHub.
2. Go to https://streamlit.io/cloud → “New app” → Select your repo/branch.
3. Set **Main file**: `energy_process_dashboard.py`
4. Click **Deploy**.

Any push to `main` will auto–redeploy your app.

## Local install

```bash
git clone https://github.com/AZFARHAD24511/energy-process-explorer.git
cd energy-process-explorer
pip install -r requirements.txt
streamlit run energy_process_dashboard.py
# energy_footprint
