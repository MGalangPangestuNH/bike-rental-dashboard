Dashboard Penyewaan Sepeda ✨

Setup Environment - Anaconda

conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

Setup Environment - Shell/Terminal

mkdir dashboard_penyewaan_sepeda
cd dashboard_penyewaan_sepeda
pipenv install
pipenv shell
pip install -r requirements.txt

Run Streamlit App

streamlit run app.py

