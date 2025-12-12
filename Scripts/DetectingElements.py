import os
import re
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from bs4.element import Tag


# Scans html document and create a dataset of all elements present in it
def create_dataset(url):
    """
        Fetches all HTML elements from a webpage for a given URL.

        :param url: URL of the webpage
        """
    df = pd.DataFrame({
        "element": pd.Series(dtype="str"),
        "class": pd.Series(dtype="object"),
        "id": pd.Series(dtype="str"),
        "name": pd.Series(dtype="str"),
        "parent_element": pd.Series(dtype="str"),
        "parent_class": pd.Series(dtype="object"),
        "parent_id": pd.Series(dtype="str"),
        "parent_name": pd.Series(dtype="str")
    })

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses

        soup = BeautifulSoup(response.text, "html.parser")

    except Exception as e:
        print(f"Error fetching URL: {e}")

    for tag in soup.find_all(True):  # True = all tags
        tag_name = tag.name
        tag_class = tag.get("class", [])  # list (can be empty)
        tag_id = tag.get("id")
        tag_name_attr = tag.get("name")

        # getting Parent info
        parent = tag.parent if tag.parent else None
        parent_name = parent.name if parent else None
        parent_class = parent.get("class", []) if parent else []
        parent_id = parent.get("id") if parent else None
        parent_name_attr = parent.get("name") if parent else None

        # Append row
        df.loc[len(df)] = [
            tag_name,
            tag_class,
            tag_id,
            tag_name_attr,
            parent_name,
            parent_class,
            parent_id,
            parent_name_attr
        ]
    print(df)
    os.makedirs('..//Data', exist_ok=True)
    df.to_csv('..//Data//out.csv')

create_dataset("http://test.salesforce.com")