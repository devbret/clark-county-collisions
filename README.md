# Clark County Collisions

![Screenshot of heatmap displaying collisions in Clark County, Washington.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/d8f7c4dd-4d2e-42ad-95fc-112eb79bebb6.png)

View traffic collision records in Clark County, WA as an interactive web-based heatmap.

## Overview

This project transforms traffic collision data into an interactive, filterable heatmap using Python and a JavaScript frontend. The Python script processes a CSV file containing coordinates, cleans the data and outputs a JSON file with the fields required for visualization.

In terms of JavaScript, a Leaflet map renders the processed data as a heat layer where intensity reflects collision severity. A control panel allows users to filter collisions by year, injury and fatality counts, weather, lighting, severity and text search. Additional controls allow users to adjust heat radius and blur, toggle the heat layer and automatically fit displayed data onto the screen.
