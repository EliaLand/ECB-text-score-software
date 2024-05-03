# ECB Text Score Software (Beta version)
The project aims to conduct textual analysis of the European Central Bank's (ECB) Monetary Policy Statements through the deployment of Python-based software. These monetary policy decisions take place every six months and following the meeting, the President and the Vice President of the ECB explain the decision at the press conference and answer questions from journalists. 
Firstly, we will develop a web scraping script to extract textual data from the ECB's website. Subsequently, we'll use the Natural Language Toolkit (NLTK) package to preprocess the text, including tokenization, stemming, and converting words to lowercase.
Next, the Loughran McDonald Sentiment Dictionary will be employed to transform the cleaned qualitative text data into a quantitative measure of the ECB's communication tone. This communication measure will then be regressed against the output gap and inflation gap, obtained via API, to assess the sensitivity of the ECB's communication to these macroeconomic variables.
Throughout the project, we'll employ various visualization and analysis packages to explore the data and conduct preliminary analysis. Finally, we plan to develop a user-friendly interface for easy access and interpretation of our findings.

## Acknowledgments:
We acknowledge the support of Elia Landini, Jessie Cameron & Lina Abril (Pantheon-Sorbonne University) in the development of this project.
