{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/veeravallisarathkumar/Tick-Tok-Project/blob/main/Activity_Course%202%20TikTok%20project%20lab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DtNBZFHO3M7n"
      },
      "source": [
        "# **TikTok Project**\n",
        "**Course 2 - Get Started with Python**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zJCatj3xzrQZ"
      },
      "source": [
        "Welcome to the TikTok Project!\n",
        "\n",
        "You have just started as a data professional at TikTok.\n",
        "\n",
        "The team is still in the early stages of the project. You have received notice that TikTok's leadership team has approved the project proposal. To gain clear insights to prepare for a claims classification model, TikTok's provided data must be examined to begin the process of exploratory data analysis (EDA).\n",
        "\n",
        "A notebook was structured and prepared to help you in this project. Please complete the following questions."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rgSbVJvomcVa"
      },
      "source": [
        "# **Course 2 End-of-course project: Inspect and analyze data**\n",
        "\n",
        "In this activity, you will examine data provided and prepare it for analysis.\n",
        "<br/>\n",
        "\n",
        "**The purpose** of this project is to investigate and understand the data provided. This activity will:\n",
        "\n",
        "1.   Acquaint you with the data\n",
        "\n",
        "2.   Compile summary information about the data\n",
        "\n",
        "3.   Begin the process of EDA and reveal insights contained in the data\n",
        "\n",
        "4.   Prepare you for more in-depth EDA, hypothesis testing, and statistical analysis\n",
        "\n",
        "**The goal** is to construct a dataframe in Python, perform a cursory inspection of the provided dataset, and inform TikTok data team members of your findings.\n",
        "<br/>\n",
        "*This activity has three parts:*\n",
        "\n",
        "**Part 1:** Understand the situation\n",
        "* How can you best prepare to understand and organize the provided TikTok information?\n",
        "\n",
        "**Part 2:** Understand the data\n",
        "\n",
        "* Create a pandas dataframe for data learning and future exploratory data analysis (EDA) and statistical activities\n",
        "\n",
        "* Compile summary information about the data to inform next steps\n",
        "\n",
        "**Part 3:** Understand the variables\n",
        "\n",
        "* Use insights from your examination of the summary data to guide deeper investigation into variables\n",
        "\n",
        "<br/>\n",
        "\n",
        "To complete the activity, follow the instructions and answer the questions below. Then, you will us your responses to these questions and the questions included in the Course 2 PACE Strategy Document to create an executive summary.\n",
        "\n",
        "Be sure to complete this activity before moving on to Course 3. You can assess your work by comparing the results to a completed exemplar after completing the end-of-course project."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HjFGokxv2pc5"
      },
      "source": [
        "# **Identify data types and compile summary information**\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MRUYfzCb4vop"
      },
      "source": [
        "Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.\n",
        "\n",
        "# **PACE stages**\n",
        "\n",
        "<img src=\"images/Pace.png\" width=\"100\" height=\"100\" align=left>\n",
        "\n",
        "   *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)\n",
        "   *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)\n",
        "   *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)\n",
        "   *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zRHb2QQWj99m"
      },
      "source": [
        "<img src=\"images/Plan.png\" width=\"100\" height=\"100\" align=left>\n",
        "\n",
        "\n",
        "## **PACE: Plan**\n",
        "\n",
        "Consider the questions in your PACE Strategy Document and those below to craft your response:\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TD5rUDqtNoiH"
      },
      "source": [
        "### **Task 1. Understand the situation**\n",
        "\n",
        "*   How can you best prepare to understand and organize the provided information?\n",
        "\n",
        "\n",
        "*Begin by exploring your dataset and consider reviewing the Data Dictionary.*"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "C9WkTfMU4_mB"
      },
      "source": [
        "==> ENTER YOUR RESPONSE HERE"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1E9Y5aC0IAA-"
      },
      "source": [
        "<img src=\"images/Analyze.png\" width=\"100\" height=\"100\" align=left>\n",
        "\n",
        "## **PACE: Analyze**\n",
        "\n",
        "Consider the questions in your PACE Strategy Document to reflect on the Analyze stage."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4I-fjg7pNOe4"
      },
      "source": [
        "### **Task 2a. Imports and data loading**\n",
        "\n",
        "Start by importing the packages that you will need to load and explore the dataset. Make sure to use the following import statements:\n",
        "*   `import pandas as pd`\n",
        "\n",
        "*   `import numpy as np`\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "I4Jj3QLINOsL"
      },
      "outputs": [],
      "source": [
        "# Import packages\n",
        "import pandas as pd\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YJpU5tFvNNDy"
      },
      "source": [
        "Then, load the dataset into a dataframe. Creating a dataframe will help you conduct data manipulation, exploratory data analysis (EDA), and statistical activities.\n",
        "\n",
        "**Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oYk-rdaWNN4G"
      },
      "outputs": [],
      "source": [
        "# Load dataset into dataframe\n",
        "data = pd.read_csv(\"tiktok_dataset.csv\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "L6KgK-M8o3we"
      },
      "source": [
        "### **Task 2b. Understand the data - Inspect the data**\n",
        "\n",
        "View and inspect summary information about the dataframe by **coding the following:**\n",
        "\n",
        "1. `data.head(10)`\n",
        "2. `data.info()`\n",
        "3. `data.describe()`\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "pW7syBEskCS8",
        "outputId": "a3179e3a-95ad-4d2d-d6dc-142a7624190e"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>#</th>\n",
              "      <th>claim_status</th>\n",
              "      <th>video_id</th>\n",
              "      <th>video_duration_sec</th>\n",
              "      <th>video_transcription_text</th>\n",
              "      <th>verified_status</th>\n",
              "      <th>author_ban_status</th>\n",
              "      <th>video_view_count</th>\n",
              "      <th>video_like_count</th>\n",
              "      <th>video_share_count</th>\n",
              "      <th>video_download_count</th>\n",
              "      <th>video_comment_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>claim</td>\n",
              "      <td>7017666017</td>\n",
              "      <td>59</td>\n",
              "      <td>someone shared with me that drone deliveries a...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>under review</td>\n",
              "      <td>343296.0</td>\n",
              "      <td>19425.0</td>\n",
              "      <td>241.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>claim</td>\n",
              "      <td>4014381136</td>\n",
              "      <td>32</td>\n",
              "      <td>someone shared with me that there are more mic...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>active</td>\n",
              "      <td>140877.0</td>\n",
              "      <td>77355.0</td>\n",
              "      <td>19034.0</td>\n",
              "      <td>1161.0</td>\n",
              "      <td>684.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>claim</td>\n",
              "      <td>9859838091</td>\n",
              "      <td>31</td>\n",
              "      <td>someone shared with me that american industria...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>active</td>\n",
              "      <td>902185.0</td>\n",
              "      <td>97690.0</td>\n",
              "      <td>2858.0</td>\n",
              "      <td>833.0</td>\n",
              "      <td>329.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>claim</td>\n",
              "      <td>1866847991</td>\n",
              "      <td>25</td>\n",
              "      <td>someone shared with me that the metro of st. p...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>active</td>\n",
              "      <td>437506.0</td>\n",
              "      <td>239954.0</td>\n",
              "      <td>34812.0</td>\n",
              "      <td>1234.0</td>\n",
              "      <td>584.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>claim</td>\n",
              "      <td>7105231098</td>\n",
              "      <td>19</td>\n",
              "      <td>someone shared with me that the number of busi...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>active</td>\n",
              "      <td>56167.0</td>\n",
              "      <td>34987.0</td>\n",
              "      <td>4110.0</td>\n",
              "      <td>547.0</td>\n",
              "      <td>152.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>6</td>\n",
              "      <td>claim</td>\n",
              "      <td>8972200955</td>\n",
              "      <td>35</td>\n",
              "      <td>someone shared with me that gross domestic pro...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>under review</td>\n",
              "      <td>336647.0</td>\n",
              "      <td>175546.0</td>\n",
              "      <td>62303.0</td>\n",
              "      <td>4293.0</td>\n",
              "      <td>1857.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>7</td>\n",
              "      <td>claim</td>\n",
              "      <td>4958886992</td>\n",
              "      <td>16</td>\n",
              "      <td>someone shared with me that elvis presley has ...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>active</td>\n",
              "      <td>750345.0</td>\n",
              "      <td>486192.0</td>\n",
              "      <td>193911.0</td>\n",
              "      <td>8616.0</td>\n",
              "      <td>5446.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>8</td>\n",
              "      <td>claim</td>\n",
              "      <td>2270982263</td>\n",
              "      <td>41</td>\n",
              "      <td>someone shared with me that the best selling s...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>active</td>\n",
              "      <td>547532.0</td>\n",
              "      <td>1072.0</td>\n",
              "      <td>50.0</td>\n",
              "      <td>22.0</td>\n",
              "      <td>11.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>9</td>\n",
              "      <td>claim</td>\n",
              "      <td>5235769692</td>\n",
              "      <td>50</td>\n",
              "      <td>someone shared with me that about half of the ...</td>\n",
              "      <td>not verified</td>\n",
              "      <td>active</td>\n",
              "      <td>24819.0</td>\n",
              "      <td>10160.0</td>\n",
              "      <td>1050.0</td>\n",
              "      <td>53.0</td>\n",
              "      <td>27.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>10</td>\n",
              "      <td>claim</td>\n",
              "      <td>4660861094</td>\n",
              "      <td>45</td>\n",
              "      <td>someone shared with me that it would take a 50...</td>\n",
              "      <td>verified</td>\n",
              "      <td>active</td>\n",
              "      <td>931587.0</td>\n",
              "      <td>171051.0</td>\n",
              "      <td>67739.0</td>\n",
              "      <td>4104.0</td>\n",
              "      <td>2540.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    # claim_status    video_id  video_duration_sec  \\\n",
              "0   1        claim  7017666017                  59   \n",
              "1   2        claim  4014381136                  32   \n",
              "2   3        claim  9859838091                  31   \n",
              "3   4        claim  1866847991                  25   \n",
              "4   5        claim  7105231098                  19   \n",
              "5   6        claim  8972200955                  35   \n",
              "6   7        claim  4958886992                  16   \n",
              "7   8        claim  2270982263                  41   \n",
              "8   9        claim  5235769692                  50   \n",
              "9  10        claim  4660861094                  45   \n",
              "\n",
              "                            video_transcription_text verified_status  \\\n",
              "0  someone shared with me that drone deliveries a...    not verified   \n",
              "1  someone shared with me that there are more mic...    not verified   \n",
              "2  someone shared with me that american industria...    not verified   \n",
              "3  someone shared with me that the metro of st. p...    not verified   \n",
              "4  someone shared with me that the number of busi...    not verified   \n",
              "5  someone shared with me that gross domestic pro...    not verified   \n",
              "6  someone shared with me that elvis presley has ...    not verified   \n",
              "7  someone shared with me that the best selling s...    not verified   \n",
              "8  someone shared with me that about half of the ...    not verified   \n",
              "9  someone shared with me that it would take a 50...        verified   \n",
              "\n",
              "  author_ban_status  video_view_count  video_like_count  video_share_count  \\\n",
              "0      under review          343296.0           19425.0              241.0   \n",
              "1            active          140877.0           77355.0            19034.0   \n",
              "2            active          902185.0           97690.0             2858.0   \n",
              "3            active          437506.0          239954.0            34812.0   \n",
              "4            active           56167.0           34987.0             4110.0   \n",
              "5      under review          336647.0          175546.0            62303.0   \n",
              "6            active          750345.0          486192.0           193911.0   \n",
              "7            active          547532.0            1072.0               50.0   \n",
              "8            active           24819.0           10160.0             1050.0   \n",
              "9            active          931587.0          171051.0            67739.0   \n",
              "\n",
              "   video_download_count  video_comment_count  \n",
              "0                   1.0                  0.0  \n",
              "1                1161.0                684.0  \n",
              "2                 833.0                329.0  \n",
              "3                1234.0                584.0  \n",
              "4                 547.0                152.0  \n",
              "5                4293.0               1857.0  \n",
              "6                8616.0               5446.0  \n",
              "7                  22.0                 11.0  \n",
              "8                  53.0                 27.0  \n",
              "9                4104.0               2540.0  "
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Display and examine the first ten rows of the dataframe\n",
        "data.head(10)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uo90wIjK7z-k",
        "outputId": "4a181459-5dfc-4b7f-db0b-f64cbb0c4ba8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 19382 entries, 0 to 19381\n",
            "Data columns (total 12 columns):\n",
            " #   Column                    Non-Null Count  Dtype  \n",
            "---  ------                    --------------  -----  \n",
            " 0   #                         19382 non-null  int64  \n",
            " 1   claim_status              19084 non-null  object \n",
            " 2   video_id                  19382 non-null  int64  \n",
            " 3   video_duration_sec        19382 non-null  int64  \n",
            " 4   video_transcription_text  19084 non-null  object \n",
            " 5   verified_status           19382 non-null  object \n",
            " 6   author_ban_status         19382 non-null  object \n",
            " 7   video_view_count          19084 non-null  float64\n",
            " 8   video_like_count          19084 non-null  float64\n",
            " 9   video_share_count         19084 non-null  float64\n",
            " 10  video_download_count      19084 non-null  float64\n",
            " 11  video_comment_count       19084 non-null  float64\n",
            "dtypes: float64(5), int64(3), object(4)\n",
            "memory usage: 1.8+ MB\n"
          ]
        }
      ],
      "source": [
        "# Get summary info\n",
        "data.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rrdPW1l67zrR",
        "outputId": "e9701b26-df9e-4d0b-bd9c-93fc401e81f7"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>#</th>\n",
              "      <th>video_id</th>\n",
              "      <th>video_duration_sec</th>\n",
              "      <th>video_view_count</th>\n",
              "      <th>video_like_count</th>\n",
              "      <th>video_share_count</th>\n",
              "      <th>video_download_count</th>\n",
              "      <th>video_comment_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>19382.000000</td>\n",
              "      <td>1.938200e+04</td>\n",
              "      <td>19382.000000</td>\n",
              "      <td>19084.000000</td>\n",
              "      <td>19084.000000</td>\n",
              "      <td>19084.000000</td>\n",
              "      <td>19084.000000</td>\n",
              "      <td>19084.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>9691.500000</td>\n",
              "      <td>5.627454e+09</td>\n",
              "      <td>32.421732</td>\n",
              "      <td>254708.558688</td>\n",
              "      <td>84304.636030</td>\n",
              "      <td>16735.248323</td>\n",
              "      <td>1049.429627</td>\n",
              "      <td>349.312146</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>5595.245794</td>\n",
              "      <td>2.536440e+09</td>\n",
              "      <td>16.229967</td>\n",
              "      <td>322893.280814</td>\n",
              "      <td>133420.546814</td>\n",
              "      <td>32036.174350</td>\n",
              "      <td>2004.299894</td>\n",
              "      <td>799.638865</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.234959e+09</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>4846.250000</td>\n",
              "      <td>3.430417e+09</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>4942.500000</td>\n",
              "      <td>810.750000</td>\n",
              "      <td>115.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>9691.500000</td>\n",
              "      <td>5.618664e+09</td>\n",
              "      <td>32.000000</td>\n",
              "      <td>9954.500000</td>\n",
              "      <td>3403.500000</td>\n",
              "      <td>717.000000</td>\n",
              "      <td>46.000000</td>\n",
              "      <td>9.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>14536.750000</td>\n",
              "      <td>7.843960e+09</td>\n",
              "      <td>47.000000</td>\n",
              "      <td>504327.000000</td>\n",
              "      <td>125020.000000</td>\n",
              "      <td>18222.000000</td>\n",
              "      <td>1156.250000</td>\n",
              "      <td>292.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>19382.000000</td>\n",
              "      <td>9.999873e+09</td>\n",
              "      <td>60.000000</td>\n",
              "      <td>999817.000000</td>\n",
              "      <td>657830.000000</td>\n",
              "      <td>256130.000000</td>\n",
              "      <td>14994.000000</td>\n",
              "      <td>9599.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                  #      video_id  video_duration_sec  video_view_count  \\\n",
              "count  19382.000000  1.938200e+04        19382.000000      19084.000000   \n",
              "mean    9691.500000  5.627454e+09           32.421732     254708.558688   \n",
              "std     5595.245794  2.536440e+09           16.229967     322893.280814   \n",
              "min        1.000000  1.234959e+09            5.000000         20.000000   \n",
              "25%     4846.250000  3.430417e+09           18.000000       4942.500000   \n",
              "50%     9691.500000  5.618664e+09           32.000000       9954.500000   \n",
              "75%    14536.750000  7.843960e+09           47.000000     504327.000000   \n",
              "max    19382.000000  9.999873e+09           60.000000     999817.000000   \n",
              "\n",
              "       video_like_count  video_share_count  video_download_count  \\\n",
              "count      19084.000000       19084.000000          19084.000000   \n",
              "mean       84304.636030       16735.248323           1049.429627   \n",
              "std       133420.546814       32036.174350           2004.299894   \n",
              "min            0.000000           0.000000              0.000000   \n",
              "25%          810.750000         115.000000              7.000000   \n",
              "50%         3403.500000         717.000000             46.000000   \n",
              "75%       125020.000000       18222.000000           1156.250000   \n",
              "max       657830.000000      256130.000000          14994.000000   \n",
              "\n",
              "       video_comment_count  \n",
              "count         19084.000000  \n",
              "mean            349.312146  \n",
              "std             799.638865  \n",
              "min               0.000000  \n",
              "25%               1.000000  \n",
              "50%               9.000000  \n",
              "75%             292.000000  \n",
              "max            9599.000000  "
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Get summary statistics\n",
        "data.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jrENd-iQZRdA"
      },
      "source": [
        "===> ENTER YOUR RESPONSE TO QUESTIONS 1-3 HERE"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gYx1emvno7U_"
      },
      "source": [
        "### **Task 2c. Understand the data - Investigate the variables**\n",
        "\n",
        "In this phase, we will begin to investigate the variables more closely to better understand them.\n",
        "\n",
        "You know from the project proposal that the ultimate objective is to use machine learning to classify videos as either claims or opinions. A good first step towards understanding the data might therefore be examining the `claim_status` variable. Begin by determining how many videos there are for each different claim status."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Kb8fPcw3rvvo",
        "outputId": "0ef30bdf-0763-4901-a9d9-f64d1da265c7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "claim      9608\n",
              "opinion    9476\n",
              "Name: claim_status, dtype: int64"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# What are the different values for claim status and how many of each are in the data?\n",
        "data['claim_status'].value_counts()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QSE317zdZp1q"
      },
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FpD-nHv5Cpiy"
      },
      "source": [
        "Next, examine the engagement trends associated with each different claim status.\n",
        "\n",
        "Start by using Boolean masking to filter the data according to claim status, then calculate the mean and median view counts for each claim status."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fuwMO66VCri1",
        "outputId": "5731fdad-6ddc-4839-f9b2-36b1fcc0bde3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "mean video view count: 501029.4527477102\n",
            "median video view count: 501555.0\n"
          ]
        }
      ],
      "source": [
        "# What is the average view count of videos with \"claim\" status?\n",
        "avg_view_count = data[data['claim_status']== 'claim'].mean(numeric_only=True)['video_view_count']\n",
        "print('mean video view count:',avg_view_count)\n",
        "median_view_count = data[data['claim_status']== 'claim'].median(numeric_only=True)['video_view_count']\n",
        "print('median video view count:',median_view_count)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FCRPxmpHCrQW",
        "outputId": "875512b9-2fce-4336-f9db-48c7f002a4cf"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Mean video view count: 4956.43224989447\n",
            "Median video view count: 4953.0\n"
          ]
        }
      ],
      "source": [
        "# What is the average view count of videos with \"opinion\" status?\n",
        "opinions = data[data['claim_status']=='opinion']\n",
        "print('Mean video view count:', opinions['video_view_count'].mean())\n",
        "print('Median video view count:', opinions['video_view_count'].median())\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6zIf6L7cC9be"
      },
      "source": [
        "\n",
        "Now, examine trends associated with the ban status of the author.\n",
        "\n",
        "Use `groupby()` to calculate how many videos there are for each combination of categories of claim status and author ban status."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Luu6W5b7DGtt",
        "outputId": "938318c6-64ba-499d-efbf-62b6aec7d748"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>#</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>claim_status</th>\n",
              "      <th>author_ban_status</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"3\" valign=\"top\">claim</th>\n",
              "      <th>active</th>\n",
              "      <td>6566</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>banned</th>\n",
              "      <td>1439</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>under review</th>\n",
              "      <td>1603</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"3\" valign=\"top\">opinion</th>\n",
              "      <th>active</th>\n",
              "      <td>8817</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>banned</th>\n",
              "      <td>196</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>under review</th>\n",
              "      <td>463</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                   #\n",
              "claim_status author_ban_status      \n",
              "claim        active             6566\n",
              "             banned             1439\n",
              "             under review       1603\n",
              "opinion      active             8817\n",
              "             banned              196\n",
              "             under review        463"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Get counts for each group combination of claim status and author ban status\n",
        "data.groupby(['claim_status', 'author_ban_status']).count()[['#']]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xWpGkxCTDHlE"
      },
      "source": [
        "\n",
        "Continue investigating engagement levels, now focusing on `author_ban_status`.\n",
        "\n",
        "Calculate the median video share count of each author ban status."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jaWqtj3yENy0",
        "outputId": "6a6155c1-cdff-4228-e4f3-3f75a57209ea"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead tr th {\n",
              "        text-align: left;\n",
              "    }\n",
              "\n",
              "    .dataframe thead tr:last-of-type th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th colspan=\"2\" halign=\"left\">video_view_count</th>\n",
              "      <th colspan=\"2\" halign=\"left\">video_like_count</th>\n",
              "      <th colspan=\"2\" halign=\"left\">video_share_count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>author_ban_status</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>active</th>\n",
              "      <td>215927.039524</td>\n",
              "      <td>8616.0</td>\n",
              "      <td>71036.533836</td>\n",
              "      <td>2222.0</td>\n",
              "      <td>14111.466164</td>\n",
              "      <td>437.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>banned</th>\n",
              "      <td>445845.439144</td>\n",
              "      <td>448201.0</td>\n",
              "      <td>153017.236697</td>\n",
              "      <td>105573.0</td>\n",
              "      <td>29998.942508</td>\n",
              "      <td>14468.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>under review</th>\n",
              "      <td>392204.836399</td>\n",
              "      <td>365245.5</td>\n",
              "      <td>128718.050339</td>\n",
              "      <td>71204.5</td>\n",
              "      <td>25774.696999</td>\n",
              "      <td>9444.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                  video_view_count           video_like_count            \\\n",
              "                              mean    median             mean    median   \n",
              "author_ban_status                                                         \n",
              "active               215927.039524    8616.0     71036.533836    2222.0   \n",
              "banned               445845.439144  448201.0    153017.236697  105573.0   \n",
              "under review         392204.836399  365245.5    128718.050339   71204.5   \n",
              "\n",
              "                  video_share_count           \n",
              "                               mean   median  \n",
              "author_ban_status                             \n",
              "active                 14111.466164    437.0  \n",
              "banned                 29998.942508  14468.0  \n",
              "under review           25774.696999   9444.0  "
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.groupby(['author_ban_status']).agg(\n",
        "    {'video_view_count': ['mean', 'median'],\n",
        "     'video_like_count': ['mean', 'median'],\n",
        "     'video_share_count': ['mean', 'median']})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "V9eIkY8TENkK",
        "outputId": "d65448f5-e5ec-41d8-c506-735836a2da22"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>video_share_count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>author_ban_status</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>active</th>\n",
              "      <td>437.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>banned</th>\n",
              "      <td>14468.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>under review</th>\n",
              "      <td>9444.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                   video_share_count\n",
              "author_ban_status                   \n",
              "active                         437.0\n",
              "banned                       14468.0\n",
              "under review                  9444.0"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# What's the median video share count of each author ban status?\n",
        "data.groupby(['author_ban_status']).median(numeric_only=True)[['video_share_count']\n",
        "]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gLLZObEHEOQf"
      },
      "source": [
        "\n",
        "Use `groupby()` to group the data by `author_ban_status`, then use `agg()` to get the count, mean, and median of each of the following columns:\n",
        "* `video_view_count`\n",
        "* `video_like_count`\n",
        "* `video_share_count`\n",
        "\n",
        "Remember, the argument for the `agg()` function is a dictionary whose keys are columns. The values for each column are a list of the calculations you want to perform."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fVlTvmO-Ebgc",
        "outputId": "41f44418-4350-4609-8e91-29ea638918d0"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead tr th {\n",
              "        text-align: left;\n",
              "    }\n",
              "\n",
              "    .dataframe thead tr:last-of-type th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th colspan=\"3\" halign=\"left\">video_view_count</th>\n",
              "      <th colspan=\"3\" halign=\"left\">video_like_count</th>\n",
              "      <th colspan=\"3\" halign=\"left\">video_share_count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>author_ban_status</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>active</th>\n",
              "      <td>15383</td>\n",
              "      <td>215927.039524</td>\n",
              "      <td>8616.0</td>\n",
              "      <td>15383</td>\n",
              "      <td>71036.533836</td>\n",
              "      <td>2222.0</td>\n",
              "      <td>15383</td>\n",
              "      <td>14111.466164</td>\n",
              "      <td>437.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>banned</th>\n",
              "      <td>1635</td>\n",
              "      <td>445845.439144</td>\n",
              "      <td>448201.0</td>\n",
              "      <td>1635</td>\n",
              "      <td>153017.236697</td>\n",
              "      <td>105573.0</td>\n",
              "      <td>1635</td>\n",
              "      <td>29998.942508</td>\n",
              "      <td>14468.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>under review</th>\n",
              "      <td>2066</td>\n",
              "      <td>392204.836399</td>\n",
              "      <td>365245.5</td>\n",
              "      <td>2066</td>\n",
              "      <td>128718.050339</td>\n",
              "      <td>71204.5</td>\n",
              "      <td>2066</td>\n",
              "      <td>25774.696999</td>\n",
              "      <td>9444.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                  video_view_count                          video_like_count  \\\n",
              "                             count           mean    median            count   \n",
              "author_ban_status                                                              \n",
              "active                       15383  215927.039524    8616.0            15383   \n",
              "banned                        1635  445845.439144  448201.0             1635   \n",
              "under review                  2066  392204.836399  365245.5             2066   \n",
              "\n",
              "                                           video_share_count                \\\n",
              "                            mean    median             count          mean   \n",
              "author_ban_status                                                            \n",
              "active              71036.533836    2222.0             15383  14111.466164   \n",
              "banned             153017.236697  105573.0              1635  29998.942508   \n",
              "under review       128718.050339   71204.5              2066  25774.696999   \n",
              "\n",
              "                            \n",
              "                    median  \n",
              "author_ban_status           \n",
              "active               437.0  \n",
              "banned             14468.0  \n",
              "under review        9444.0  "
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.groupby(['author_ban_status']).agg({\n",
        "    'video_view_count' : ['count', 'mean', 'median'],\n",
        "    'video_like_count' : ['count', 'mean', 'median'],\n",
        "    'video_share_count' : ['count', 'mean', 'median']\n",
        "})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i7R3vKUhEb8_"
      },
      "source": [
        "**Question:** What do you notice about the number of views, likes, and shares for banned authors compared to active authors?\n",
        "\n",
        "Now, create three new columns to help better understand engagement rates:\n",
        "* `likes_per_view`: represents the number of likes divided by the number of views for each video\n",
        "* `comments_per_view`: represents the number of comments divided by the number of views for each video\n",
        "* `shares_per_view`: represents the number of shares divided by the number of views for each video"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eyymCn6oFDP3"
      },
      "outputs": [],
      "source": [
        "# Create a likes_per_view column\n",
        "data['likes_per_view'] = data['video_like_count']/ data['video_view_count']\n",
        "\n",
        "# Create a comments_per_view column\n",
        "data['comments_per_view'] = data['video_comment_count'] /data['video_view_count']\n",
        "\n",
        "# Create a shares_per_view column\n",
        "data['shares_per_view'] = data['video_share_count'] / data['video_view_count']"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Y238Q5jaFOwQ"
      },
      "source": [
        "Use `groupby()` to compile the information in each of the three newly created columns for each combination of categories of claim status and author ban status, then use `agg()` to calculate the count, the mean, and the median of each group."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WZoK3_-bFPW2",
        "outputId": "3223ed3a-3643-4d14-8129-c35adfe68619"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead tr th {\n",
              "        text-align: left;\n",
              "    }\n",
              "\n",
              "    .dataframe thead tr:last-of-type th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th colspan=\"3\" halign=\"left\">likes_per_view</th>\n",
              "      <th colspan=\"3\" halign=\"left\">comments_per_view</th>\n",
              "      <th colspan=\"3\" halign=\"left\">shares_per_view</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>median</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>claim_status</th>\n",
              "      <th>author_ban_status</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"3\" valign=\"top\">claim</th>\n",
              "      <th>active</th>\n",
              "      <td>6566</td>\n",
              "      <td>0.329542</td>\n",
              "      <td>0.326538</td>\n",
              "      <td>6566</td>\n",
              "      <td>0.001393</td>\n",
              "      <td>0.000776</td>\n",
              "      <td>6566</td>\n",
              "      <td>0.065456</td>\n",
              "      <td>0.049279</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>banned</th>\n",
              "      <td>1439</td>\n",
              "      <td>0.345071</td>\n",
              "      <td>0.358909</td>\n",
              "      <td>1439</td>\n",
              "      <td>0.001377</td>\n",
              "      <td>0.000746</td>\n",
              "      <td>1439</td>\n",
              "      <td>0.067893</td>\n",
              "      <td>0.051606</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>under review</th>\n",
              "      <td>1603</td>\n",
              "      <td>0.327997</td>\n",
              "      <td>0.320867</td>\n",
              "      <td>1603</td>\n",
              "      <td>0.001367</td>\n",
              "      <td>0.000789</td>\n",
              "      <td>1603</td>\n",
              "      <td>0.065733</td>\n",
              "      <td>0.049967</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"3\" valign=\"top\">opinion</th>\n",
              "      <th>active</th>\n",
              "      <td>8817</td>\n",
              "      <td>0.219744</td>\n",
              "      <td>0.218330</td>\n",
              "      <td>8817</td>\n",
              "      <td>0.000517</td>\n",
              "      <td>0.000252</td>\n",
              "      <td>8817</td>\n",
              "      <td>0.043729</td>\n",
              "      <td>0.032405</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>banned</th>\n",
              "      <td>196</td>\n",
              "      <td>0.206868</td>\n",
              "      <td>0.198483</td>\n",
              "      <td>196</td>\n",
              "      <td>0.000434</td>\n",
              "      <td>0.000193</td>\n",
              "      <td>196</td>\n",
              "      <td>0.040531</td>\n",
              "      <td>0.030728</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>under review</th>\n",
              "      <td>463</td>\n",
              "      <td>0.226394</td>\n",
              "      <td>0.228051</td>\n",
              "      <td>463</td>\n",
              "      <td>0.000536</td>\n",
              "      <td>0.000293</td>\n",
              "      <td>463</td>\n",
              "      <td>0.044472</td>\n",
              "      <td>0.035027</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                               likes_per_view                      \\\n",
              "                                        count      mean    median   \n",
              "claim_status author_ban_status                                      \n",
              "claim        active                      6566  0.329542  0.326538   \n",
              "             banned                      1439  0.345071  0.358909   \n",
              "             under review                1603  0.327997  0.320867   \n",
              "opinion      active                      8817  0.219744  0.218330   \n",
              "             banned                       196  0.206868  0.198483   \n",
              "             under review                 463  0.226394  0.228051   \n",
              "\n",
              "                               comments_per_view                      \\\n",
              "                                           count      mean    median   \n",
              "claim_status author_ban_status                                         \n",
              "claim        active                         6566  0.001393  0.000776   \n",
              "             banned                         1439  0.001377  0.000746   \n",
              "             under review                   1603  0.001367  0.000789   \n",
              "opinion      active                         8817  0.000517  0.000252   \n",
              "             banned                          196  0.000434  0.000193   \n",
              "             under review                    463  0.000536  0.000293   \n",
              "\n",
              "                               shares_per_view                      \n",
              "                                         count      mean    median  \n",
              "claim_status author_ban_status                                      \n",
              "claim        active                       6566  0.065456  0.049279  \n",
              "             banned                       1439  0.067893  0.051606  \n",
              "             under review                 1603  0.065733  0.049967  \n",
              "opinion      active                       8817  0.043729  0.032405  \n",
              "             banned                        196  0.040531  0.030728  \n",
              "             under review                  463  0.044472  0.035027  "
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "data.groupby(['claim_status', 'author_ban_status']).agg(\n",
        "    {'likes_per_view': ['count', 'mean', 'median'],\n",
        "     'comments_per_view': ['count', 'mean', 'median'],\n",
        "     'shares_per_view': ['count', 'mean', 'median']})\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RLhoV4xDFp_o"
      },
      "source": [
        "**Question:**\n",
        "\n",
        "How does the data for claim videos and opinion videos compare or differ? Consider views, comments, likes, and shares."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tF_82VLgzrQm"
      },
      "source": [
        "<img src=\"images/Construct.png\" width=\"100\" height=\"100\" align=left>\n",
        "\n",
        "## **PACE: Construct**\n",
        "\n",
        "**Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project.\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "2dDGfu9Kjs_B"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HPVfDMum_xYl"
      },
      "source": [
        "==> ENTER YOUR RESPONSE HERE"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zFGlwPqEjdUO"
      },
      "source": [
        "**Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the \"save\" icon at the top of this notebook to ensure your work has been logged."
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.6"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}