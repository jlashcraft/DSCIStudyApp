import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="D595 Flashcards", page_icon="🧠", layout="centered")

# Flashcard Data (You can easily paste the rest of your questions here)
flashcards = flashcards = flashcards = flashcards = [
    # --- Section 1: Data Processing ---
    {
        "section": "Data Processing",
        "question": "In Python, what does the following code do?\n`import numpy as np; a = np.array([1, 2, 3]); b = np.append(a, 4)`",
        "answer": "Creates a new array b with the value [1, 2, 3, 4]"
    },
    {
        "section": "Data Processing",
        "question": "Which of these Python features is NOT a disadvantage?",
        "answer": "Python cannot integrate with other programming languages."
    },
    {
        "section": "Data Processing",
        "question": "Which of these Python libraries is primarily used for numerical computing?",
        "answer": "NumPy"
    },
    {
        "section": "Data Processing",
        "question": "What will be the output of the following code snippet?\n`a = \"5\"; b = int(a); c = float(b); print(type(c))`",
        "answer": "class 'float'"
    },
    {
        "section": "Data Processing",
        "question": "Which of the following are examples of structured data? (Select all that apply)",
        "answer": "Tabular data in a spreadsheet, Time-series data, Tables in a relational database"
    },
    {
        "section": "Data Processing",
        "question": "Which of the following statements about Categorical data in Pandas is true?",
        "answer": "Categorical data is stored as integer codes with corresponding categories."
    },
    {
        "section": "Data Processing",
        "question": "Which method is used to change the order of categories in a Categorical column?",
        "answer": "as_ordered()"
    },
    {
        "section": "Data Processing",
        "question": "Which method in Pandas is most suitable for chaining custom functions while analyzing data?",
        "answer": "pipe()"
    },
    {
        "section": "Data Processing",
        "question": "What does the following code achieve?\n`df.pipe(lambda x: x[x['cores'] > 2]).pipe(lambda x: x.assign(new_col=x['clock'] * 2))`",
        "answer": "Filters rows where cores > 2 and creates a new column with double the clock value."
    },
    {
        "section": "Data Processing",
        "question": "What is the output of the following code?\n`df['cpu'] = df['cpu'].astype('category'); df['cpu'].cat.categories`",
        "answer": "A list of unique cpu values sorted alphabetically."
    },
    {
        "section": "Data Processing",
        "question": "Which of the following statements about classification tasks is correct?",
        "answer": "SVM can perform both binary and multiclass classification."
    },
    {
        "section": "Data Processing",
        "question": "What is the purpose of the cross_val_score function in Scikit-learn?",
        "answer": "To evaluate performance of estimator using cross-validation."
    },
    {
        "section": "Data Processing",
        "question": "What is the primary difference between classification and clustering tasks? (Select all that apply)",
        "answer": "Classification requires labeled data, while clustering does not. Clustering groups similar data points, while classification assigns predefined labels."
    },
    {
        "section": "Data Processing",
        "question": "What will happen if we normalize the features before using the SVM classifier? (Select all that apply)",
        "answer": "Normalization ensures zero mean and unit variance for each feature. The performance might improve due to better scaling. The numerical stability of the algorithm will increase."
    },
    {
        "section": "Data Processing",
        "question": "Which of the following will NOT affect the score of the SVM classifier?",
        "answer": "Reordering the rows in the dataset."
    },
    {
        "section": "Data Processing",
        "question": "True or False: Feature sub-selection is always necessary for every dataset.",
        "answer": "False"
    },
    {
        "section": "Data Processing",
        "question": "Why is it generally not feasible to train a model on all possible feature subsets?",
        "answer": "The number of subsets grows exponentially with the number of features"
    },
    {
        "section": "Data Processing",
        "question": "Why might a weaker learner be used inside the feature selection loop instead of the main model?",
        "answer": "Weaker learners reduce the cost of repeated training"
    },
    {
        "section": "Data Processing",
        "question": "Why might a feature with one dominant category (e.g., 95% of values are the same) be a candidate for removal?",
        "answer": "It doesn't vary enough to separate classes"
    },
    {
        "section": "Data Processing",
        "question": "The VarianceThreshold method evaluates features based on:",
        "answer": "Their variance, independent of the class label"
    },
    {
        "section": "Data Processing",
        "question": "Which of the following approaches addresses the computational challenge of evaluating all possible subsets of features? (Select all that apply)",
        "answer": "Sampling a small subset of data points for feature selection. Using greedy strategies such as forward or backward selection. Using weak learners instead of computationally expensive models."
    },
    {
        "section": "Data Processing",
        "question": "What is the key difference between feature sub-selection and dimensionality reduction as defined in this course?",
        "answer": "Dimensionality reduction generates new features, while feature sub-selection uses a subset of the existing features."
    },
    {
        "section": "Data Processing",
        "question": "What does the SelectPercentile class in scikit-learn do?",
        "answer": "Selects a percentage of features with the highest scores."
    },
    {
        "section": "Data Processing",
        "question": "Which feature selection method is most appropriate for regression tasks?",
        "answer": "Mutual information regression (mutual_info_regression)"
    },
    {
        "section": "Data Processing",
        "question": "What is the main disadvantage of using the naive approach of evaluating all feature subsets for feature selection?",
        "answer": "It is computationally expensive due to the exponential number of subsets."
    },
    {
        "section": "Data Processing",
        "question": "Which of the following the a reasonable way to select the number of principle components k?",
        "answer": "Choose k to be the smallest value so that 99% of total variance of the data is explained."
    },
    {
        "section": "Data Processing",
        "question": "Which of the following is not an application of PCA?",
        "answer": "Embedding technique for representation learning."
    },
    {
        "section": "Data Processing",
        "question": "Which of the following is wrong regarding PCA?",
        "answer": "PCA is susceptible to local optima, try multiple initialization may help."
    },
    {
        "section": "Data Processing",
        "question": "Why can adding too many features in a Machine Learning model lead to poor performance?",
        "answer": "Too many features can lead to the curse of dimensionality, where noise and irrelevant features degrade the model's predictive power."
    },
    {
        "section": "Data Processing",
        "question": "Which techniques can help address the issue of having too many features in a dataset? (Select all that apply)",
        "answer": "Manifold Learning. Singular Value Decomposition (SVD). Principal Component Analysis (PCA)."
    },

    # --- Section 2: Data Visualization with Tableau ---
    {
        "section": "Data Visualization",
        "question": "What is the main business purpose of Excel as compared to Tableau?",
        "answer": "Quick on-off reports"
    },
    {
        "section": "Data Visualization",
        "question": "What is a recommended approach for representing large datasets in visualizations?",
        "answer": "Summarize or aggregate data where appropriate"
    },
    {
        "section": "Data Visualization",
        "question": "Which Tableau feature is used to filter data displayed in a visualization?",
        "answer": "Filters"
    },
    {
        "section": "Data Visualization",
        "question": "What is a significant advantage of using Tableau over traditional spreadsheet tools?",
        "answer": "Enhanced visualization capabilities and interactivity"
    },
    {
        "section": "Data Visualization",
        "question": "Which of the following is a best practice for using colors in visualizations?",
        "answer": "Use a consistent color scheme that reflects the data context"
    },
    {
        "section": "Data Visualization",
        "question": "Why should legends and annotations be used in visualizations?",
        "answer": "To explain data context and improve readability"
    },
    {
        "section": "Data Visualization",
        "question": "What is required to unleash the full potential of Excel?",
        "answer": "Knowledge of VBA and basic scripting"
    },
    {
        "section": "Data Visualization",
        "question": "What is the role of the Marks card in Tableau?",
        "answer": "To customize the appearance and attributes of visualizations"
    },
    {
        "section": "Data Visualization",
        "question": "What is the function of the 'Show Me' feature in Tableau?",
        "answer": "To suggest the most appropriate visualization based on selected data"
    },
    {
        "section": "Data Visualization",
        "question": "Which of the following best describes a relationship between measures and dimensions?",
        "answer": "Dimensions categorize data, while measures quantify it."
    },
    {
        "section": "Data Visualization",
        "question": "What is the primary use of measures in Tableau?",
        "answer": "To represent numerical data used in calculations"
    },
    {
        "section": "Data Visualization",
        "question": "What is the purpose of dragging dimensions into the Rows or Columns shelf?",
        "answer": "To structure the layout of visualizations"
    },
    {
        "section": "Data Visualization",
        "question": "What is a dimension in Tableau?",
        "answer": "A qualitative field used for categorizing data"
    },
    {
        "section": "Data Visualization",
        "question": "What is a parameter in Tableau?",
        "answer": "A dynamic value that can replace a constant in calculations"
    },
    {
        "section": "Data Visualization",
        "question": "What is a primary benefit of using Tableau's interactive dashboards?",
        "answer": "Enables users to explore and interact with data in real-time"
    },
    {
        "section": "Data Visualization",
        "question": "What is a calculated field in Tableau?",
        "answer": "A custom field created by applying a formula or expression"
    },
    {
        "section": "Data Visualization",
        "question": "What additional attributes can be modified using the Marks card in Tableau?",
        "answer": "Tooltip content, color, and size"
    },
    {
        "section": "Data Visualization",
        "question": "What is a benefit of using hierarchies in Tableau dashboards?",
        "answer": "It enables interactive exploration of data at multiple levels."
    },
    {
        "section": "Data Visualization",
        "question": "In Tableau, what icon represents a hierarchical field in the Data pane?",
        "answer": "A folder icon"
    },
    {
        "section": "Data Visualization",
        "question": "What happens when you change the mark type in Tableau?",
        "answer": "The visual representation of data changes."
    },
    {
        "section": "Data Visualization",
        "question": "How can you create a hierarchy in Tableau?",
        "answer": "Drag and drop fields into the same group in the Data pane"
    },
    {
        "section": "Data Visualization",
        "question": "What is the default aggregation type applied to numeric fields in Tableau?",
        "answer": "SUM()"
    },
    {
        "section": "Data Visualization",
        "question": "Which function is commonly used to create conditional logic in calculated fields?",
        "answer": "All of the Above"
    },
    {
        "section": "Data Visualization",
        "question": "Which of the following is a type of filter in Tableau?",
        "answer": "Dimension filter"
    },
    {
        "section": "Data Visualization",
        "question": "What is a common benefit of using calculated fields in Tableau?",
        "answer": "They allow customization and flexibility in data analysis."
    },
    {
        "section": "Data Visualization",
        "question": "What feature allows users to filter data dynamically in Tableau?",
        "answer": "Quick filters"
    },
    {
        "section": "Data Visualization",
        "question": "Why are aggregate functions important in visual analytics?",
        "answer": "They simplify raw data and highlight key insights."
    },
    {
        "section": "Data Visualization",
        "question": "How can users add tooltips to a visualization in Tableau?",
        "answer": "By editing the Tooltip option in the Marks card"
    },
    {
        "section": "Data Visualization",
        "question": "Why might someone choose a doughnut chart over a pie chart in Tableau?",
        "answer": "Doughnut charts offer a central area for additional information."
    },
    {
        "section": "Data Visualization",
        "question": "What is a detail shelf used for in Tableau?",
        "answer": "To display additional data details in the view"
    },
    {
        "section": "Data Visualization",
        "question": "What is required to properly create the center of a doughnut chart in Tableau?",
        "answer": "Creating a calculated field for the center of the chart"
    },
    {
        "section": "Data Visualization",
        "question": "Which chart type is combined with a pie chart to create a doughnut chart in Tableau?",
        "answer": "Dual-axis chart"
    },
    {
        "section": "Data Visualization",
        "question": "Which feature is commonly used to enhance interactivity in dashboards?",
        "answer": "Filters"
    },
    {
        "section": "Data Visualization",
        "question": "What is a parameter in Tableau?",
        "answer": "A dynamic value that can replace a constant in calculations and filters"
    },
    {
        "section": "Data Visualization",
        "question": "What is the primary advantage of using dashboards over single sheets in Tableau?",
        "answer": "Dashboards allow users to view and interact with multiple visualizations simultaneously."
    },
    {
        "section": "Data Visualization",
        "question": "How are sets in Tableau different from groups?",
        "answer": "Sets can be computed based on conditions, while groups are manual."
    },
    {
        "section": "Data Visualization",
        "question": "What is a storyboard in Tableau?",
        "answer": "A sequence of dashboards or sheets to present a narrative"
    },
    {
        "section": "Data Visualization",
        "question": "How can users display additional information on a map in Tableau?",
        "answer": "By adding fields to the Tooltip shelf"
    },
    {
        "section": "Data Visualization",
        "question": "Which Tableau feature allows you to zoom in and out of a geographical map?",
        "answer": "Map options toolbar"
    },
    {
        "section": "Data Visualization",
        "question": "What is the benefit of using filled maps in Tableau?",
        "answer": "To highlight regions with specific colors based on data values"
    },
    {
        "section": "Data Visualization",
        "question": "What happens if the data used for clustering in Tableau lacks variation?",
        "answer": "Tableau may generate clusters with no meaningful differentiation."
    },
    {
        "section": "Data Visualization",
        "question": "How can users visualize clusters effectively in Tableau?",
        "answer": "By combining clustering with filters and color encoding"
    },
    {
        "section": "Data Visualization",
        "question": "What is the purpose of clustering in Tableau?",
        "answer": "To group similar data points based on specific attributes"
    },
    {
        "section": "Data Visualization",
        "question": "Which type of analysis is clustering in Tableau commonly used for?",
        "answer": "Exploratory data analysis"
    },
    {
        "section": "Data Visualization",
        "question": "Which algorithm does Tableau use for clustering?",
        "answer": "K-Means clustering"
    },

    # --- Section 3: Machine Learning with Python ---
    {
        "section": "Machine Learning",
        "question": "Which of the following is an example of Machine Learning in action?",
        "answer": "Netflix recommending movies based on your viewing and rating history."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following best describes the difference between regression and classification in supervised learning?",
        "answer": "Regression predicts continuous output variables, while classification predicts discrete categories."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following is a characteristic of unsupervised learning?",
        "answer": "The goal is to identify patterns or group data without preassigned labels."
    },
    {
        "section": "Machine Learning",
        "question": "Why is data preprocessing a crucial step in machine learning workflows?",
        "answer": "It organizes raw data into a structured format, addressing issues like missing values and noise, to ensure accurate and efficient model training."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following techniques can be used to handle missing data during preprocessing? (Select all that apply)",
        "answer": "Filling missing values with estimates like the mean, median, or mode."
    },
    {
        "section": "Machine Learning",
        "question": "What is the primary goal of the Least Squares Method in Linear Regression?",
        "answer": "To minimize the squared distance between the data points and the regression line."
    },
    {
        "section": "Machine Learning",
        "question": "What does overfitting in a model indicate?",
        "answer": "The model performs well on training data but poorly on unseen data."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following approaches can help address overfitting in machine learning models? (Select all that apply)",
        "answer": "Using simpler models with fewer predictor variables. Applying regularization techniques like L1 or L2 penalties."
    },
    {
        "section": "Machine Learning",
        "question": "What is the optimal trade-off in the bias-variance tradeoff for a machine learning model?",
        "answer": "A balanced combination of moderate bias and moderate variance to minimize total error."
    },
    {
        "section": "Machine Learning",
        "question": "What are the benefits of performing variable or feature selection in a machine learning model? (Select all that apply)",
        "answer": "Reduces the chances of overfitting by removing irrelevant or redundant features."
    },
    {
        "section": "Machine Learning",
        "question": "When we run the regression and classification tree, does the model use splits?",
        "answer": "True"
    },
    {
        "section": "Machine Learning",
        "question": "Is a random forest a version of Ensemble Learning?",
        "answer": "Yes"
    },
    {
        "section": "Machine Learning",
        "question": "What is the purpose of the 'minimum number split' parameter in a decision tree model?",
        "answer": "It defines the minimum number of samples required to split an internal node."
    },
    {
        "section": "Machine Learning",
        "question": "What is likely to happen if the maximum depth of a decision tree is set to a very high value?",
        "answer": "The tree will be more likely to overfit the data."
    },
    {
        "section": "Machine Learning",
        "question": "How does a Random Forest model make predictions for a regression task?",
        "answer": "It takes the average of predictions from all trees in the forest."
    },
    {
        "section": "Machine Learning",
        "question": "What is the main objective of Support Vector Machines (SVM) in classification problems?",
        "answer": "To find a hyperplane that maximizes the margin between the closest data points of each class, called support vectors."
    },
    {
        "section": "Machine Learning",
        "question": "What is the role of the \"Kernel Trick\" in Support Vector Machines (SVM)?",
        "answer": "It allows SVM to perform non-linear classification by transforming the input space into a higher-dimensional space."
    },
    {
        "section": "Machine Learning",
        "question": "In SVM, what are the support vectors?",
        "answer": "The data points closest to the hyperplane, which influence its position and orientation."
    },
    {
        "section": "Machine Learning",
        "question": "In the K-Nearest Neighbors (KNN) algorithm, what determines the label assigned to a test sample?",
        "answer": "The proximity or distance of K closest training samples and their labels."
    },
    {
        "section": "Machine Learning",
        "question": "What is the effect of choosing a smaller value of K in the K-Nearest Neighbors (KNN) algorithm?",
        "answer": "The model tends to overfit the data, being overly influenced by noise in the training set."
    },
    {
        "section": "Machine Learning",
        "question": "What is the primary purpose of using Naïve Bayes in classification problems?",
        "answer": "To create a simple and interpretable model for predicting class labels."
    },
    {
        "section": "Machine Learning",
        "question": "In the Naïve Bayes algorithm, which principle is used to calculate the probability of a class label given a set of features?",
        "answer": "Bayes' Theorem"
    },
    {
        "section": "Machine Learning",
        "question": "What is the primary difference between Logistic Regression and Linear Regression?",
        "answer": "Logistic Regression is used for binary classification, while Linear Regression is used for predicting continuous outcomes."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following best describes the role of the link function in Logistic Regression?",
        "answer": "It explains the relationship between the mean of the dependent variable and the linear predictor."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following is a disadvantage of Logistic Regression?",
        "answer": "It can only be used for classification problems."
    },
    {
        "section": "Machine Learning",
        "question": "In the K-Means algorithm, we have to specify the number of clusters.",
        "answer": "True"
    },
    {
        "section": "Machine Learning",
        "question": "True or False: Since k-means is guaranteed to converge, initialization is not important for it.",
        "answer": "True"
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following is a disadvantage of the K-Means algorithm?",
        "answer": "It assumes clusters are of equal size, spherical in shape, and distinct from each other."
    },
    {
        "section": "Machine Learning",
        "question": "What is the primary purpose of the Elbow Method in K-Means clustering?",
        "answer": "To select the optimal number of clusters by analyzing the Within-Cluster Sum of Squares (WCSS)."
    },
    {
        "section": "Machine Learning",
        "question": "What is the main difference between Hierarchical Clustering and K-Means clustering?",
        "answer": "Hierarchical Clustering produces a tree-like structure (dendrogram) to represent data relationships, while K-Means does not."
    },
    {
        "section": "Machine Learning",
        "question": "You flip a coin three times, what's the probability that you get at least one heads?",
        "answer": "7/8"
    },
    {
        "section": "Machine Learning",
        "question": "Your grade for this course has the following probability distribution: A: 70%; B: 20%; C: 10%. Your teacher will write either a strong or weak recommendation letter for you based on your grade. The quality of the letter has the following probability distribution given your grade: P(strong|A) = 80%; P(strong|B) = 60%; P(strong|C) = 40%. What's the total (marginal) probability that you will get a strong letter?",
        "answer": "0.72"
    },
    {
        "section": "Machine Learning",
        "question": "What does conditional independence mean in probability theory?",
        "answer": "Two events A and B are independent of each other given the knowledge of a third variable C."
    },
    {
        "section": "Machine Learning",
        "question": "What is the primary objective of the Expectation-Maximization (EM) algorithm in the context of GMMs?",
        "answer": "To iteratively estimate the parameters (mean, variance, and mixing coefficients) of the Gaussian components in the mixture."
    },
    {
        "section": "Machine Learning",
        "question": "In the first step of solving a Machine Learning problem, what is the primary task?",
        "answer": "To identify the insights or target variable that needs to be predicted."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following the a reasonable way to select the number of principle components k?",
        "answer": "Choose k to be the smallest value so that 99% of total variance of the data is explained."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following is not an application of PCA?",
        "answer": "Embedding technique for representation learning."
    },
    {
        "section": "Machine Learning",
        "question": "Which of the following is wrong?",
        "answer": "PCA is susceptible to local optima, try multiple initialization may help."
    },
    {
        "section": "Machine Learning",
        "question": "Why can adding too many features in a Machine Learning model lead to poor performance?",
        "answer": "Too many features can lead to the curse of dimensionality, where noise and irrelevant features degrade the model's predictive power."
    },
    {
        "section": "Machine Learning",
        "question": "Which techniques can help address the issue of having too many features in a dataset? (Select all that apply)",
        "answer": "Singular Value Decomposition (SVD), Manifold Learning, Principal Component Analysis (PCA)"
    }
]

# Initialize Session State to keep track of app memory
if 'deck' not in st.session_state:
    st.session_state.deck = flashcards.copy()
    st.session_state.current_index = 0
    st.session_state.show_answer = False
    st.session_state.score = 0

# App Header
st.title("🧠 D595 Final Exam Study App")
if len(flashcards) > 0:
    st.progress((st.session_state.current_index) / len(flashcards))

# Check if we reached the end of the deck
if st.session_state.current_index >= len(st.session_state.deck):
    st.success(f"🎉 You finished the deck! Your final score: {st.session_state.score} / {len(flashcards)}")
    if st.button("Restart Deck"):
        st.session_state.current_index = 0
        st.session_state.show_answer = False
        st.session_state.score = 0
        st.rerun()
else:
    # Display the current card
    card = st.session_state.deck[st.session_state.current_index]
    
    st.caption(f"Category: {card['section']}")
    st.subheader(card["question"])
    
    st.divider()

    # Toggle Answer
    if not st.session_state.show_answer:
        if st.button("Show Answer"):
            st.session_state.show_answer = True
            st.rerun()
    else:
        st.info(f"**Answer:** {card['answer']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("❌ Missed it"):
                st.session_state.show_answer = False
                st.session_state.current_index += 1
                st.rerun()
        with col2:
            if st.button("✅ Got it!"):
                st.session_state.score += 1
                st.session_state.show_answer = False
                st.session_state.current_index += 1
                st.rerun()

# Sidebar for stats and controls
with st.sidebar:
    st.header("Study Stats")
    st.metric(label="Score", value=f"{st.session_state.score}")
    st.write(f"Cards remaining: {len(flashcards) - st.session_state.current_index}")
    
    st.divider()
    
    # The New Shuffle Button
    if st.button("🔀 Shuffle Deck"):
        st.session_state.deck = flashcards.copy()
        random.shuffle(st.session_state.deck)
        st.session_state.current_index = 0
        st.session_state.show_answer = False
        st.session_state.score = 0
        st.rerun()