# Clark County Collisions

![Screenshot of heatmap displaying collisions in Clark County, Washington.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/d8f7c4dd-4d2e-42ad-95fc-112eb79bebb6.png)

Convert collision coordinate data from Clark County, WA into JSON and visualize it as an interactive heatmap with filtering, statistics and map controls.

## Overview

This project transforms traffic collision data into an interactive, filterable heatmap using Python and a JavaScript frontend. The Python script processes a CSV file containing coordinates, cleans the data and outputs a JSON file with the fields required for visualization.

In terms of JavaScript, a Leaflet map renders the processed data as a heat layer where intensity reflects collision severity. A control panel allows users to filter collisions by year, injury and fatality counts, weather, lighting, severity and text search. Additional controls allow users to adjust heat radius and blur, toggle the heat layer and automatically fit displayed data onto the screen.

## Basic Setup Instructions

Below are the required software programs and instructions for installing and using this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/clark-county-collisions.git`

4. Navigate to the repo's directory: `cd clark-county-collisions`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate your virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Download the [collisions source data](https://hub-clarkcountywa.opendata.arcgis.com/datasets/collisions/explore?location=45.764050%2C-122.504200%2C11) as a CSV file

9. Place the `Collisions.csv` file into the `data` directory of this repo

10. Process the raw data: `python3 app.py`

11. Launch an `HTTP` server: `python3 -m http.server`

12. Access the heatmap visualization in a browser: `http://localhost:8000`

13. When finished using the app: `CTRL + C`

14. Exit the virtual environment: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Source interesting, relevant and publicly available data from an official government source

- Use Python to transform the raw data into a useable structure and format

- Visualize the Python output in an interactive and engaging fashion using modern web development tools

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
