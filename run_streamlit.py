import streamlit.web.cli as stcli
import sys

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "StreamlitDashboards.py"]
    stcli.main()
