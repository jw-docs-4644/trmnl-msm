# trmnl-msm

Fetch school lunch menus and display them on TRMNL.

## What it does

This plug-in fetches school menu information from My School Menus ([https://menus.healthepro.com/](https://menus.healthepro.com/)). You can add up to two schools and customize the plug-in to show menu data for the current day, the current and next days, or the entire week.

<!-- Display school lunch menus from Health-e Pro (menus.healthepro.com) on a TRMNL e-ink display. Supports multiple schools, configurable display modes (today, today+tomorrow, full week). -->

## Screenshots



<!-- Screenshots of each view size -->

## Setup

### Prerequisites

<!-- Python 3.11+, TRMNL device, trmnlp gem (optional, for local preview) -->

### Find your school IDs

<!-- How to browse menus.healthepro.com and grab org_id, site_id, menu_id from the URL -->

### Configure

<!-- cp config.example.toml config.toml, edit with your IDs, explain display modes -->

### Install & run

<!-- python3 -m venv .venv && .venv/bin/pip install requests, then bin/fetch -->

## Deploy to TRMNL

### Create a private plugin

<!-- Create on trmnl.com, paste Liquid templates, get UUID -->

### Push data

<!-- TRMNL_PLUGIN_UUID=xxx bin/fetch -->

### Automate

<!-- Cron job or GitHub Actions scheduled workflow -->

## Local preview

<!-- bin/dev to run trmnlp serve, bin/fetch --date YYYY-MM-DD to simulate dates -->

## Configuration reference

<!-- Full config.toml options: organization_id, display, site_id, site_name, menu_id, menu_name -->

## License

<!-- MIT -->
