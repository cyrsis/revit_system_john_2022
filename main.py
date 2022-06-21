import streamlit as st

from pathlib import Path


def main():
    st.markdown((Path("README.md")).read_text())


if __name__ == "__main__":
    main()
