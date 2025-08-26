# Devops for Data Science - Labs

This project follows the labs from the [*DevOps for Data Science*](https://do4ds.com/) book by Alex K. Gold.

## Lab01

1.  **Create a Quarto Project**
    -   Initialized a new Quarto project using RStudio.
2.  **Add a UV Project**
    -   Created a UV project in the same directory.
    -   Reference for UV projects: [UV Project Guide](https://docs.astral.sh/uv/guides/projects/)
3.  **Configure Python Environment in R**
    -   Updated the project .Rprofile so that R uses the Python interpreter from the project’s `.venv` virtual environment through `reticulate`.
4.  **Add EDA and model files**
    -   Added `model.qmd` and `eda.qmd` files.

## Lab02

1.  **Create and Save a Vetiver Model**
    -   Converted the trained model into a Vetiver model object and stored it in a local folder board.
2.  **Create a Vetiver API**
    -   Built a Python API (`api.py`) for the Vetiver model that reads the latest version from the board and exposes it for serving predictions.

## Lab03

1.  **Move Data to DuckDB**
    -   Stored the project data in a local DuckDB database (`my-db.duckdb`).
2.  **Update EDA and Model Scripts**
    -   Modified `eda.qmd` and `model.qmd` to read data directly from DuckDB.
3.  **Create Shiny Apps**
    -   Built Shiny apps in both R (`app-api.R`) and Python (`app-api.py`).
