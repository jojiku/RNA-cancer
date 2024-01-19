<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Non-invasive diagnosis of brain tumor</h3>

  <p align="center">
    Tumour detection with RNA
  </p>
  
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#updates">Updates</a>
    </li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- UPDATES -->
## Updates 

### 17.12.2023:
The final project consists of Streamlit UI, FastAPI backend with PostgreSQL and Faiss indexes, and <a href="https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1">DistilUsev1</a> (trained with ContrastiveCE) on separate embedder module. The embedder module **riches 25 RPS in peak** on 13th Gen Intel(R) Core(TM) i9-13900HX CPU.

### 15.12.2023:
We tried four raw (not trained) popular sentence transformers:
* DistilUsev1
* DistilUsev2
* mpnet
* MiniLM
Concluded that DistilUsev1, even though it was not trained on our data, had the same quality as Doc2Vec. DistilUsev1 was chosen as a base model.

Also service API is now available for searching corresponding vacancies and resumes, using Faiss for storing essintal embeddings and PostgreSQL for other info.

### 13.12.2023:
Experiments with Doc2Vec were made: 
Doc2Vec - v1 (vector_size = 35, epochs = 50): positive similarity = 0.414, positive similarity = 0.298, difference = 0.116. Meteor score: 0.342, 
Rouge score: 0.28.

Doc2Vec - v2 (vector_size = 15, epochs = 50): positive similarity = 0.158, positive similarity = 0.106, difference = 0.0515. Meteor score: 0.126, 
Rouge score: 0.103.

For more info please visit <a href="https://www.notion.so/Team-19-Job-Resume-matching-56f93b10243a4989acbfdcb88d014b03">our notion page</a>.
<!-- preprocessing -->
## Preprocessing
We had to work on our data as there weren't any 'ready' datasets for our project. <a href="https://www.kaggle.com/datasets/vyacheslavpanteleev1/hhru-it-vacancies-from-20211025-to-20211202">Dataset with vacancies</a> was matched with <a href="https://drive.google.com/file/d/1ikA_Ht45fXD2w5dWZ9sGTSRl-UNeCVub/view?usp=share_link">resume data</a> manually, with 2 different approaches:
* By calculating similarities between full texts of resumes and vacancies using Word2Vec, Doc2Vec and TFidVectorization (file resume_matching_data.ipynb). But the results we got here were dissatisfying.
* By matching on key words and setting strict filters on data. This approach turned out to be effective.

<!-- ABOUT THE PROJECT -->
## About The Project


**Non -invasive diagnosis of tumors** means checking the presence of cancer without a biopsy (which is the most accurate method for determining tumors). 

Of course, **it is a good idea to constantly use biopsy**, but if the patient is in serious condition, then any surgical intervention can simply kill him. In such cases, you can use an MRI, but it is **expensive** and may not be sensitive enough to detect very small tumors. 

**A relatively new method based on RNA sequencing will be presented as a project**. As a result of the work, it is planned to create a convenient service for doctors who can load RNA data of their patients, and the model will make a prediction about whether a person is sick with cancer or not

<img src="![icon](https://github.com/jojiku/RNA-cancer/assets/56271473/06231c5e-d59f-4657-92a5-19f944caa136)
" height=400 align = "center"/>
