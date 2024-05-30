# Streamlit-based user interface
# in terminal: streamlit run "file/path.py"

## 0) Preliminary setup
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import base64
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## 1) Title and university logo
### import and convert the image to bytes
def pil_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

response1 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/FED_logo.png")
image1 = Image.open(BytesIO(response1.content))

### define position and dimension
image1_64 = pil_to_base64(image1)

### create a container with customed settings
st.markdown(
    """
    <style>
    .container {
        display: flex;
        align-items: center; 
        padding: 10px;
    }
    .title {
        color: white; 
        font-size: 45px;
        font-weight: bold;
        font-family: "Roboto", sans-serif;
        margin-right: 20px
    }
    .logo {
        width: 150x;
        height: 150px;
        margin-right: 20px
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div class="container">
        <img src="data:image/png;base64,{image1_64}" class="logo">
        <h1 class="title">FED MONETARY POLICY SENTIMENT CALCULATOR</h1>
    </div>
    """,
    unsafe_allow_html=True
)

## 2) Aknowledgements and infos 
st.write("by Elia Landini, Jessie Cameron & Lina Abril (Pantheon-Sorbonne University)")
if st.button("GitHub"):
    js = "window.open('https://github.com/EliaLand/FED-text-score-software')"
    st.write(f"<script>{js}</script>", unsafe_allow_html=True)

## 3) Abstract
st.write("## Abstract")
st.write("""
         <div style="text-align: justify">
         The project aims to conduct textual analysis of the Federal Reserve's (FED) Monetary Policy Reports through the deployment of Python-based software.
         This report is written semi-annually and provided to Congress containing discussions on the conduct of monetary policy and economic developments and prospects for the future.
         First, we develop a web scraping script to extract textual data from the FED's website.
         Subsequently, we use the Natural Language Toolkit (NLTK) package to preprocess the text, including tokenization, stemming, and converting words to lowercase.
         Next, the Loughran McDonald Sentiment Dictionary is employed to transform the cleaned qualitative text data into a quantitative measure of the FED's communication tone.
         This communication measure is then be regressed against the output gap and inflation gap, obtained via API, to assess the sensitivity of the FED's communication to these macroeconomic variables.
         Throughout the project, we employ various visualisation and analysis packages to explore the data and conduct preliminary analysis.
         </div>
         """,
         unsafe_allow_html=True)
st.write("   ") 
st.write("   ")

## 4) Perceived sentiment survey
### set up
st.write("## 1 minute survey")
st.write("We are conducting a survey to gather insights on current hot topics in monetary policy. We value your perception and opinions, and your responses will be treated with strict confidentiality and in accordance with non-profiling and anonymity principles.")
### survey questions
#### Question 1
q1 = st.slider(
    "On a scale from 1 to 10, how would you rate the suitability of the approach undertaken by developed countries central banks in addressing current inflation trends? (1 = Not Suitable at All, 10 = Extremely Suitable)",
    1, 10, 5)
#### Question 2
q2 = st.slider(
    "On a scale from 1 to 10, how would you rate the suitability of the approach undertaken by developing countries central banks in addressing current inflation trends? (1 = Not Suitable at All, 10 = Extremely Suitable)",
    1, 10, 5)
#### Question 3
q3 = st.radio(
    "To what extent do you agree with the following statement: \"The 2008 Global Financial Crisis (GFC) highlighted the critical importance of regulatory intervention and supervision over the banking system, a relevance further underscored by the Covid-19 pandemic.\"",
    ("Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"))
#### Question 4
q4 = st.radio(
    "Do you support the Bank of Japan’s recent decision to hike interest rates for the first time since the Global Financial Crisis and end its yield curve control program?",
    ("Yes", "No", "Not sure"))
#### Question 5
q5 = st.radio(
    "What are your thoughts on the use of quantitative easing as a tool for economic stabilization?",
    ("Strongly Support", "Support", "Oppose", "Strongly Oppose", "No Opinion"))
#### Question 6
q6 = st.radio(
    "Do you think that the Federal Reserve will cut interest rates at the June meeting?",
    ("Yes", "No", "Not sure"))
#### Question 7
q7 = st.text_area("Please share any additional thoughts or insights on current monetary policies and their impact on the economy.")
#### Submit button
if st.button("Submit"):
    responses = {
        "Q1": q1,
        "Q2": q2,
        "Q3": q3,
        "Q4": q4,
        "Q5": q5,
        "Q6": q6,
        "Q7": q7,
    }
    st.write("Thank you for your responses!")
    st.write(responses)
st.write("   ") 
st.write("   ")

## 5) Press conference reports dataframe
st.write("## Press conference reports dataframe")
st.markdown("""
<div style="text-align: justify">
This section describes the preliminary text analysis performed on the data from the Federal Reserve (FED). The analysis includes calculating several textual features that provide insights into the complexity and structure of the statements. nltk package is a comprehensive library for natural language processing and it is used for:            

* **Tokenization:** Tokenization: Splitting the text into individual words and sentences using word_tokenize and sent_tokenize..
* **Stopwords:** Providing a list of common stopwords in English, which is used to calculate the ratio of stopwords in the text.
            
Also on creating new variables to analyse the textual data from the Federal Reserve (FED). Specifically, it calculates:

* **1. Word Count**: Total number of words per statement.
* **2. Sentence Count**: Total number of sentences per statement.
* **3. Unique Word Count**: Total number of unique words in the text.
* **4. Character Count**: Total number of characters in the text.
* **5. Average Words per Sentence**: Average number of words per sentence.
* **6. Ratio of Complex Words**: Share of complex words (words with three or more syllables) to the total word count.
* **7. Ratio of Stop Words**: Proportion of stop words (common words like "and", "the", "is", etc.) to the total word count.
* **8. Average Syllables per Word**: Average number of syllables per word in the text.
* **9. Lexical Diversity**: Calculates the ratio between the number of unique words and the total number of words.
* **10. Average Sentence Length**: Average length of sentences in the text.

---

After computing these variables, the data are summarised using descriptive statistics tables and visually. This exploratory analysis provides insights into the textual characteristics of the FED data before conducting regression analysis.
</div>
""",
unsafe_allow_html=True)
FED_df = pd.read_csv(r"C:\Users\eland\Desktop\code\FED_df_data.csv")
st.dataframe(FED_df)
st.write("   ") 
st.write("   ")

## 6) Cleaned textual dataframe
st.write("## Cleaned textual dataframe")
st.write("""
<div style="text-align: justify">
"The presented dataframe provides an overview on textual data after as result of the deployment of serial cleaning tecniques. The Monetary Policy Reports are pre-processed by excluding administrative details on the webpage to focus on the core of the text. In addition, several additional steps were undertaken to clean the data prior to estimating the tone of the minutes. This includes following steps to preprocess text data using NLTK. The process includes tokenisation, stopword removal, and lemmatization.
</div>
""",
unsafe_allow_html=True)
st.write("   ")
FED_cleaned_df = pd.read_csv(r"C:\Users\eland\Desktop\code\FED_cleaned_df.csv")
st.dataframe(FED_cleaned_df)
st.write("   ") 
st.write("   ")

## 7) Textual variables visualization
st.write("## Textual variables visualization")
response2 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/graph1.png")
image2 = Image.open(BytesIO(response2.content))
image2_64 = pil_to_base64(image2)
st.image(image2, use_column_width=True)
st.write("   ") 
response3 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/graph2.png")
image3 = Image.open(BytesIO(response3.content))
image3_64 = pil_to_base64(image2)
st.image(image3, use_column_width=True)
st.write("   ") 
st.write("   ")

## 8) Word frequencies
st.write("## Word frequencies")
st.write("""
<div style="text-align: justify">
Taking the text of all the columns, we join and remove some repeated words which have no economic sense, then we count them and find the frequency in which they appear, with wordcloud, matplotlib and seaborn we plot to visualize which are the most repeated words.
</div>
""",
unsafe_allow_html=True)
st.write("   ")
response4 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/graph3.png")
image4 = Image.open(BytesIO(response4.content))
image4_64 = pil_to_base64(image4)
st.image(image4, use_column_width=True)
st.write("   ") 
response5 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/graph4.png")
image5 = Image.open(BytesIO(response5.content))
image5_64 = pil_to_base64(image5)
st.image(image5, use_column_width=True)
st.write("   ")

# 9) Comunication variable
st.write("## Comunication variable: from qualitative to quantitative")
st.markdown("""
This section converts the qualitative textual data to a quantitative measure. A lexicon-based method is used which relies on a pre-defined list of words called lexicons or dictionaries, each associated with sentiment scores ranging from positive to negative. In particular, the Loughran and McDonald (2011) financial sentiment dictionary is employed in this study as it is the most suitable approach for classifying financial and economic texts.

The sentiment score is calculated by subtracting the count of negative words from the count of positive words, and then dividing by the total count of positive and negative words. Mathematically, this is represented as:

$$
\\text{Tone} = \\frac{N_{\\text{pos}} - N_{\\text{neg}}}{N_{\\text{pos}} + N_{\\text{neg}}}
$$

Where:
- $N_{\\text{pos}}$ is the number of words in the minutes that are classified as positive according to the Loughran-McDonald sentiment dictionary.
- $N_{\\text{neg}}$ is the number of words that are classified as negative.

The measure of tone is bounded between [-1:1]. A positive value of the tone measure reflects some optimism in the language used, while a negative value reflects some pessimism.
""")
st.markdown("""
| Scale    | Number of Words | Sample Words                                                                                                               |
|----------|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Negative | 2,335            | adverse, caution, challenge, collapse, crisis, decline, deteriorate, difficult, diminish, exacerbate, failure, liquidated, loss, negative, punishes, recession, severe, slowdown, stagnate, unemployed |
| Positive | 354              | achieve, advantage, attain, boom, constructive, efficient, enhance, favourable, gained, highest, improve, leading, optimistic, positive, profitable, progress, rebound, stabilize, strengthen, strong |

*Source: Loughran and McDonald (2011)*
""")
st.write("   ") 
response6 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/graph5.png")
image6 = Image.open(BytesIO(response6.content))
image6_64 = pil_to_base64(image6)
st.image(image6, use_column_width=True)
st.write("   ")
st.write("   ")

# 10) Macro-variables
st.write("## Macro-variables")
FED_df_final = pd.read_csv(r"C:\Users\eland\Desktop\code\FED_df_final.csv")
st.dataframe(FED_df_final)
st.write("   ")
response7 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/graph6.png")
image7 = Image.open(BytesIO(response7.content))
image7_64 = pil_to_base64(image7)
st.image(image7, use_column_width=True)
st.write("   ") 
response8 = requests.get("https://raw.githubusercontent.com/EliaLand/FED-text-score-software/main/Plotting/graph7.png")
image8 = Image.open(BytesIO(response8.content))
image8_64 = pil_to_base64(image8)
st.image(image8, use_column_width=True)
st.write("   ")
st.write("   ") 

# 11) Regression Analysis
st.write("## Regression Analysis")
st.markdown("""
The study follows a similar approach to Bulir et al. (2013) and arrives at the following specification:

$$
C_t = \\alpha + \\beta_T T_t + \\beta_{\\mu} (\\mu_t - \\mu_t^*) + \\beta_{\\pi} (\\pi_t - \\pi_t^*) + \\beta_{FC} \\delta_{FC} + \\beta_{cov} \\delta_{cov} + \\varepsilon_t 
$$

Where:
- $C_t$: is the tone of communication measured using the Loughran-McDonald sentiment dictionary, with higher values indicative of a more positive tone, while lower values suggest a more negative sentiment.
- The model includes two deterministic variables: $\\alpha$ is a constant and $T_t$ is a linear trend.
- $\\beta_{\\mu} (\\mu_t - \\mu_t^*)$: difference between the logarithmic level of real Gross Domestic Product (GDP, $\\mu_t$) and its trend value ($\\mu_t^*$), estimated using the Hodrick-Prescott (HP) filter.
- $\\beta_{\\pi} (\\pi_t - \\pi_t^*)$: is the absolute difference between contemporaneous inflation ($\\pi_t$) and the Fed's inflation target ($\\pi_t^*$).
- $\\delta_{FC}$ is a dummy variable equal to 1 from 2007:H2 to 2009:H1, 0 otherwise, to capture the effects of the financial crisis.
- $\\delta_{cov}$ is a dummy variable equal to 1 from 2020:H1 to 2023:H2, 0 otherwise, to analyse the Covid-19 period.
""")
st.write("   ")
st.markdown("""
<table>
<thead>
    <tr>
        <th>Dep. Variable:</th>
        <td>comm</td>
        <th>R-squared:</th>
        <td>0.335</td>
    </tr>
    <tr>
        <th>Model:</th>
        <td>OLS</td>
        <th>Adj. R-squared:</th>
        <td>0.256</td>
    </tr>
    <tr>
        <th>Method:</th>
        <td>Least Squares</td>
        <th>F-statistic:</th>
        <td>5.066</td>
    </tr>
    <tr>
        <th>Date:</th>
        <td>Thu, 30 May 2024</td>
        <th>Prob (F-statistic):</th>
        <td>0.00101</td>
    </tr>
    <tr>
        <th>Time:</th>
        <td>12:15:24</td>
        <th>Log-Likelihood:</th>
        <td>0.095492</td>
    </tr>
    <tr>
        <th>No. Observations:</th>
        <td>48</td>
        <th>AIC:</th>
        <td>11.81</td>
    </tr>
    <tr>
        <th>Df Residuals:</th>
        <td>42</td>
        <th>BIC:</th>
        <td>23.04</td>
    </tr>
    <tr>
        <th>Df Model:</th>
        <td>5</td>
        <th></th>
        <td></td>
    </tr>
    <tr>
        <th>Covariance Type:</th>
        <td>HC3</td>
        <th></th>
        <td></td>
    </tr>
</thead>
</table>

<table>
<thead>
    <tr>
        <th>Variable</th>
        <th>coef</th>
        <th>std err</th>
        <th>z</th>
        <th>P>|z|</th>
        <th>[0.025</th>
        <th>0.975]</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>const</td>
        <td>-0.4437</td>
        <td>0.060</td>
        <td>-7.365</td>
        <td>0.000</td>
        <td>-0.562</td>
        <td>-0.326</td>
    </tr>
    <tr>
        <td>trend</td>
        <td>0.0129</td>
        <td>0.003</td>
        <td>4.559</td>
        <td>0.000</td>
        <td>0.007</td>
        <td>0.018</td>
    </tr>
    <tr>
        <td>CPI_gap</td>
        <td>-0.0704</td>
        <td>0.065</td>
        <td>-1.085</td>
        <td>0.278</td>
        <td>-0.198</td>
        <td>0.057</td>
    </tr>
    <tr>
        <td>GDP_gap</td>
        <td>4.7211</td>
        <td>2.455</td>
        <td>1.923</td>
        <td>0.054</td>
        <td>-0.090</td>
        <td>9.533</td>
    </tr>
    <tr>
        <td>FC</td>
        <td>-0.2579</td>
        <td>0.094</td>
        <td>-2.756</td>
        <td>0.006</td>
        <td>-0.441</td>
        <td>-0.075</td>
    </tr>
    <tr>
        <td>Covid</td>
        <td>-0.2412</td>
        <td>0.295</td>
        <td>-0.818</td>
        <td>0.413</td>
        <td>-0.819</td>
        <td>0.336</td>
    </tr>
</tbody>
</table>

<table>
<thead>
    <tr>
        <th>Omnibus:</th>
        <td>1.459</td>
        <th>Durbin-Watson:</th>
        <td>1.751</td>
    </tr>
    <tr>
        <th>Prob(Omnibus):</th>
        <td>0.482</td>
        <th>Jarque-Bera (JB):</th>
        <td>0.695</td>
    </tr>
    <tr>
        <th>Skew:</th>
        <td>0.215</td>
        <th>Prob(JB):</th>
        <td>0.707</td>
    </tr>
    <tr>
        <th>Kurtosis:</th>
        <td>3.404</td>
        <th>Cond. No.</th>
        <td>2.02e+03</td>
    </tr>
</thead>
</table>

*Notes:*  
[1] Standard Errors are heteroscedasticity robust (HC3).  
[2] The condition number is large, 2.02e+03. This might indicate that there are strong multicollinearity or other numerical problems.
[3] Robustness checks and their results are adressed in the main code file.
""", unsafe_allow_html=True)