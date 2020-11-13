#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:15:41 2020

@author: shyambhu.mukherjee
"""

import streamlit as st
import pandas as pd
import numpy as np
import spacy
from spacy import displacy
import base64

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

st.title("streamlit-based spacy interactive app")
st.subheader("putting some buttons")

if st.button("choose big model"):
    nlp = spacy.load("en_core_web_lg")
else:
    nlp = spacy.load("en_core_web_sm")

st.subheader("trying out checkbox")
check = st.checkbox("will you let your data get stored?")

if check:
    print("fake notion! nothing recording now!")
else:
    pass

st.subheader("radio button")
radio = st.radio("choose your action",options = ["entity checking",
                                                 "dependency tree showcase",
                                                 "pos tagging"])
if radio == "entity checking":
    print("entity is chosen")
elif radio == "dependency tree showcase":
    print("dependency tree visualization is done")
elif radio == "pos tagging":
    print("pos tagging will be shown")
else:
    pass
st.write(radio)
st.subheader("write the text")
text = st.text_input("text box","Example: write here")

st.subheader("Outputs:")
doc = nlp(text)
st.write(doc)
special_output = []

if radio == "entity checking":
    st.subheader("ents")
    for token in doc.ents:
        st.write(token.text,token.label_)

if radio == "dependency tree showcase":
    obj = displacy.render(doc,style = "dep")
    render_svg(obj)
if radio == "pos tagging":
    st.write("pos tags")
    for token in doc:
        text = str(token.text)
        position = str(token.pos_)
        st.write(text,position)
