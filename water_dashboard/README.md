# Water Quality Dashboard

## Purpose
An interactive dashboard for exploring Biscayne Bay water-quality data.

## Dataset
The app uses `biscayneBay_waterquality.csv`, a dataset provided by
Prof. Gregory Reis for this course containing water-quality
readings collected in Biscayne Bay.

Measurements include temperature, salinity, depth, and geographic
coordinates. Users may also upload a CSV with the same structure.

## How to Run Locally

Once the app is deployed, you can open the public link in the
Live App section without installing anything. These instructions
are for running the code on your own computer.

With Python 3 installed, download or clone the standalone dashboard
repository and open a terminal in its main folder. This folder
should contain `water_dashboard.py`, `requirements.txt`, and
`biscayneBay_waterquality.csv`.

### Windows (PowerShell)

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install required packages:

```powershell
python -m pip install -r requirements.txt
```

Start the dashboard:

```powershell
streamlit run water_dashboard.py
```

### macOS (Terminal)

Create and activate a virtual environment, install the required
packages, and start the dashboard:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run water_dashboard.py
```

Open the URL shown in the terminal if the browser does not
open automatically. Press Ctrl+C to stop.

## How to Use

The included Biscayne Bay dataset loads automatically.

- **Data:** Browse the readings and descriptive statistics. Use the
  multiselect to choose which columns appear in the raw data table.
  Leave it empty to show all columns.
- **Charts:** Select a parameter for the line chart. Hover over points
  to see values, use the chart controls to zoom or pan, and drag the
  3D plot to rotate it.
- **Maps:** Explore reading locations, with colors showing temperature.
- **About:** Read a short description of the dashboard and its controls.
- **Upload:** Use the sidebar to upload another CSV with the same
  column names and structure as the included dataset.

## Live App
Add your public Streamlit URL after deployment.

