# NZ Dairy Pasture & Yield Optimization System

An end-to-end machine learning and analytics pipeline for New Zealand
pasture-based dairy farming. It forecasts paddock-level pasture growth
(kg DM/ha) and daily herd milk solids (kgMS), then recommends paddock
rotations and nitrogen fertiliser use within environmental limits.

## Status
🚧 In progress. Currently: project setup and domain research.

## Planned features
- Data pipeline for NZ weather and Sentinel-2 satellite (NDVI) data
- Pasture growth forecasting (XGBoost / LightGBM)
- Milk solids prediction (Random Forest / LSTM)
- Prescriptive optimizer for grazing and fertiliser (PuLP)
- Model explainability with SHAP
- Interactive Streamlit dashboard, deployed with Docker

## Data note
Individual NZ farm data is private. This project uses real public data
(weather, satellite imagery, regional statistics) combined with a clearly
labelled **simulated farm layer** for paddock and herd data.

## Project structure
- `Data/raw` - original downloaded data
- `Data/processed` - cleaned data
- `Notebooks` - exploration and analysis
- `src` - reusable pipeline and model code
- `docs` - glossary and documentation

## Author
Amarnad - [GitHub](https://github.com/Amarnad007)

