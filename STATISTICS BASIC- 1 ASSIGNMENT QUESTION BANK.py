#!/usr/bin/env python
# coding: utf-8

# STATISTICS BASIC- 1
# ASSIGNMENT 
# QUESTION BANK

# Q1. What is Statistics?
# 
# Q2. Define the different types of statistics and give an example of when each type might be used.
# 
# Q3. What are the different types of data and how do they differ from each other? Provide an example of
# each type of data.
# 
# Q4. Categorise the following datasets with respect to quantitative and qualitative data types:
# (i) Grading in exam: A+, A, B+, B, C+, C, D, E
# (ii) Colour of mangoes: yellow, green, orange, red
# (iii) Height data of a class: [178.9, 179, 179.5, 176, 177.2, 178.3, 175.8,...]
# (iv) Number of mangoes exported by a farm: [500, 600, 478, 672, ...]
#     
# Q5. Explain the concept of levels of measurement and give an example of a variable for each level.
# 
# Q6. Why is it important to understand the level of measurement when analyzing data? Provide an
# example to illustrate your answer.
# 
# Q7. How nominal data type is different from ordinal data type.
# 
# Q8. Which type of plot can be used to display data in terms of range?
# 
# Q9. Describe the difference between descriptive and inferential statistics. Give an example of each
# type of statistics and explain how they are used.
# 
# Q10. What are some common measures of central tendency and variability used in statistics? Explain
# how each measure can be used to describe a dataset.

# In[ ]:


get_ipython().run_line_magic('pinfo', 'Statistics')

A1. Statistics is the study of the collection, analysis, interpretation, presentation, and organization of data.
    In other words, it is a mathematical discipline to collect, summarize data. Also, we can say that statistics
    is a branch of applied mathematics. However, there are two important and basic ideas involved in statistics;
    they are uncertainty and variation. 


# In[ ]:


Q2. Define the different types of statistics and give an example of when each type might be used.

A2. Statistics is mainly divided into the following two categories. 

       1. Descriptive Statistics

       2. Inferential Statistics


Descriptive Statistics:-
    
    In the descriptive Statistics, the Data is described in a summarized way. The summarization is done from the sample of
    the population using different parameters like Mean or standard deviation. Descriptive Statistics are a way of using charts,
    graphs, and summary measures to organize, represent, and explain a set of Data. 

    Data is typically arranged and displayed in tables or graphs summarizing details such as histograms, pie charts,
    bars or scatter plots.

    Descriptive Statistics are just descriptive and thus do not require normalization beyond the Data collected.


Inferential Statistics:-
    
    In the Inferential Statistics, we try to interpret the Meaning of descriptive Statistics. After the Data has been collected,
    analyzed, and summarised we use Inferential Statistics to describe the Meaning of the collected Data. 

    Inferential Statistics use the probability principle to assess whether trends contained in the research sample can be
    generalized to the larger population from which the sample originally comes.

    Inferential Statistics are intended to test hypotheses and investigate relationships between variables and can be used
    to make population predictions.

    Inferential Statistics are used to draw conclusions and inferences, i.e., to make valid generalizations from samples.


# In[ ]:


Q3. What are the different types of data and how do they differ from each other? Provide an example of
    each type of data.
    
A3. Types of Data In Statistics:
    In statistics, there are four main types of data: nominal, ordinal, interval, and ratio.
    These types of data are used to describe the nature of the data being collected or analyzed, and they help determine 
    the appropriate statistical tests to use.
    
      1.Nominal Data:-
        Nominal data is a type of data that consists of categories or names that cannot be ordered or ranked.
        Nominal data is often used to categorize observations into groups, and the groups are not comparable.
        In other words, nominal data has no inherent order or ranking. Examples of nominal data include gender
        (male/female), race (White/Black/Asian), religion (Christianity/Islam/Judaism), and blood type (A/B/AB/O).
        
      2.Ordinal Data:-
        Ordinal data is a type of data that consists of categories that can be ordered or ranked. However, the 
        distance between categories is not necessarily equal. Ordinal data is often used to measure subjective
        attributes or opinions, where there is a natural order to the responses. Examples of ordinal data include
        education level (elementary/middle/high school/college), job position (manager/supervisor/employee), 
        and Likert scales (strongly agree/agree/disagree/strongly disagree).
        
      3.Interval Data:
        Interval data is a type of data that consists of numerical values where the distance between each value is equal.
        However, there is no true zero point. Interval data is often used to measure attributes such as temperature,
        dates, and time. Examples of interval data include temperature (Celsius/Fahrenheit), dates (days/months/years),
        and time (hours/minutes/seconds).
        
      4.Ratio Data:
        Ratio data is a type of data that has a true zero point and an equal distance between each value. Ratio data is
        considered the most informative type of data because it can be used to make meaningful comparisons and 
        calculations. In addition, ratio data can be used to perform all types of statistical analyses.

        Examples of ratio data include height (inches/centimeters), weight (pounds/kilograms), income (dollars), and 
        distance (miles/kilometers). 


# In[ ]:


Q4. Categorise the following datasets with respect to quantitative and qualitative data types:
(i) Grading in exam: A+, A, B+, B, C+, C, D, E
(ii) Colour of mangoes: yellow, green, orange, red
(iii) Height data of a class: [178.9, 179, 179.5, 176, 177.2, 178.3, 175.8,...]
(iv) Number of mangoes exported by a farm: [500, 600, 478, 672, ...]
    
A4. (i)  Qualitative
    (ii) Qualitative
    (iii)Quantitative
    (iv) Quantitative


# In[ ]:


Q5. Explain the concept of levels of measurement and give an example of a variable for each level.

A5. Levels of measurement refer to the different ways variables can be categorized and measured in scientific research12.
    There are four levels of measurement, which can be ranked from low to high2:-
        
    Nominal: the data can only be categorized. Example: Gender (male/female).
    Ordinal: the data can be categorized and ranked. Example: Educational level (high school, college, graduate).
    Interval: the data can be categorized, ranked, and evenly spaced. Example: Temperature (Celsius or Fahrenheit).
    Ratio: the data can be categorized, ranked, evenly spaced, and has a natural zero. Example: Height (inches or centimeters).


# In[ ]:


Q6. Why is it important to understand the level of measurement when analyzing data? Provide an
example to illustrate your answer.

A6. Levels of measurement are important because they indicate the extent to which statisticians, marketing analysts and 
    financial analysts can use existing data. For instance, if you classify your data at the ordinal level of measurement,
    you know that you can evaluate how items compare to each other based on a specific hierarchy.


# In[ ]:


Q7. How nominal data type is different from ordinal data type.

A8. Nominal data is the simplest data type. It classifies data purely by labeling or naming values e.g. measuring
    marital status, hair, or eye color. It has no hierarchy to it. Ordinal data classifies data while introducing an order,
    or ranking.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'range')

A8. The following types of plots can be used to display data in terms of range:
        Range chart: displays sets of data points, each of which is defined by multiple values for the same category, 
                    and emphasizes the distance between the two values1.
        Histogram: shows bars representing groupings of a given dimension, with each column representing a number of
                    entries that fall into a range2.
        Box-whisker plot: the box is marked by the first and third quartile, and the whiskers extends to the range.


# In[ ]:


Q9. Describe the difference between descriptive and inferential statistics. Give an example of each
    type of statistics and explain how they are used.

A9. Descriptive statistics summarize and describe the main features of a dataset, while inferential statistics use
    sample data to make predictions or draw conclusions about a population12.Examples of descriptive statistics include
    measures of central tendency (mean, median, mode) and measures of dispersion (range, variance, standard deviation)

    1. These statistics are used to describe the characteristics of a dataset, such as its shape, spread, and central location
    1. For example, the mean and standard deviation can be used to describe the average and variability of test scores 
    in a class.
    
    Examples of inferential statistics include hypothesis testing and estimation techniques
    1. These statistics are used to make predictions or draw conclusions about a population based on a sample of data1.
    For example, a researcher might use inferential statistics to test whether a new drug is more effective than a placebo
    in treating a particular condition. 

    The researcher would collect data from a sample of patients and use inferential statistics to determine whether the results 
    are likely to generalize to the larger population of patients with the condition.


# In[ ]:


Q10. What are some common measures of central tendency and variability used in statistics? Explain
    how each measure can be used to describe a dataset.
    
A10. While central tendency tells you where most of your data points lie, variability summarizes how far apart your points
    from each other.

    Data sets can have the same central tendency but different levels of variability or vice versa. Together, 
    they give you a complete picture of your data.

