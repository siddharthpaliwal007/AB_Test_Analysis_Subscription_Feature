# A-B_Test_Analysis_Subscription_Feature

## Objective:
The primary goal of this analysis is to evaluate the impact of a new subscription feature on user retention and subscription conversion rates, by comparing the performance of two groups:
Group A (Control) – No new subscription feature.
Group B (Test) – New subscription feature enabled.
By performing this A/B test analysis, we aim to understand how the introduction of a subscription feature affects Day 1 and Day 7 user retention and the conversion rate of users who subscribed within 7 days.

## Background:
The company is rolling out a new subscription feature for users, and the business goal is to increase user retention and conversion rates. The analysis measures the retention rates at Day 1 and Day 7, as well as the conversion rate of users who have subscribed. The hypothesis is that the new subscription feature will lead to better retention rates and higher subscription conversion for users in the test group compared to the control group.

## Data Collection Details:

### 1. Users Data (users.csv)
The user data file contains the following columns:
user_id: Unique identifier for each user.
signup_date: The date when the user signed up for the platform.
group: The group to which the user belongs. Either "control" (no subscription feature) or "test" (with subscription feature).

### 2. Events Data (events.csv)
The events data file contains the following columns:
user_id: Unique identifier for each user.
event_type: The type of event triggered by the user, e.g., 'subscription_signup'.
event_time: The timestamp when the event occurred.

## Steps Taken:
Data Loading: Both users.csv and events.csv files are loaded into pandas DataFrames. Date columns are parsed into appropriate datetime format.
Data Merging: Both datasets are merged based on the user_id to combine the user information with their respective event activities.
Retention Calculation: Retention is calculated at Day 1 and Day 7, by grouping users based on their group (control/test) and counting how many users were active on those days.
Subscription Conversion: The subscription conversion rate is calculated by counting how many users in the test group subscribed within 7 days.
Statistical Test: A z-test is performed to determine if the difference in Day 7 retention between the control and test groups is statistically significant.

## Key Metrics:

### 1. Day 1 Retention Rate:
Control Group: 0.432
Test Group: 0.214
Interpretation:
The Control Group has a Day 1 retention rate of 43.2%, which means that 43.2% of the users who signed up in this group were still active after Day 1.
The Test Group has a Day 1 retention rate of 21.4%. This is lower than the control group, meaning fewer users in the test group retained after Day 1.
Personal Opinion: 
This result makes sense if the new feature introduced in the Test Group (subscription feature) had a negative impact or if other factors affected retention negatively. Generally, you would expect the Test Group to either perform better or worse compared to the control group, depending on the feature's effectiveness.

### 2. Day 7 Retention Rate:
Control Group: 0.227
Test Group: 0.304
Interpretation:
After 7 days, the Control Group has a retention rate of 22.7%, which means 22.7% of the users in this group remained active after 7 days.
The Test Group has a higher Day 7 retention rate of 30.4%, suggesting that the new subscription feature helped increase retention in the long term.
Personal Opinion: 
This result is interesting because, although the Test Group had a lower Day 1 retention rate, it outperforms the Control Group in Day 7 retention. It could mean that the new subscription feature attracted users in the short term but provided more value and engagement in the long term, improving retention after 7 days.


### 3. Subscription Conversion Rate (Test Group): 0.321
Interpretation:
This means that 32.1% of the users in the Test Group converted to the new subscription feature within 7 days of signing up.
Personal Opinion: 
This seems reasonable. A 32.1% conversion rate indicates a strong uptake of the new subscription feature. However, it's important to evaluate whether this conversion rate is sufficient given the business's objectives and user expectations.

### 4. Z-Statistic: -0.853
Interpretation:
The Z-statistic measures the difference between the observed proportions (retention rates in this case) between the two groups in units of standard deviation. A Z-statistic of -0.853 indicates a small difference between the groups, but the difference is not large enough to be statistically significant.
Personal Opinion: 
A negative Z-statistic simply means that the Test Group's retention rate is lower than the Control Group's, but it's not a very large difference. This value suggests that the difference between the groups is relatively small.

### 5. P-Value: 0.394
Interpretation:
The p-value tells us whether the difference between the two groups is statistically significant.
A p-value of 0.394 is greater than the typical threshold of 0.05, meaning the difference between the retention rates of the Control and Test groups is not statistically significant.
Personal Opinion: 
Yes. A p-value of 0.394 indicates that there is a high likelihood that the observed difference between the Control and Test groups could have occurred by chance. Therefore, you cannot reject the null hypothesis, meaning there isn't strong evidence to say the new subscription feature has a significant impact on retention.

## Conclusion:
While the new subscription feature seems to have a positive impact on Day 7 retention, the difference is not statistically significant based on the Z-test. This means that, while there might be an improvement, more data or further testing may be required to confidently conclude that the feature is effective in driving retention.

## Business Impact:
The test results help the product and marketing teams determine whether the new subscription feature is worth rolling out to a wider audience.
The insights gained from retention and conversion rates can help adjust the feature to make it more appealing to users, thus improving long-term user engagement and monetization.
This analysis is foundational for future iterations of the feature and can help define further A/B tests to fine-tune product offerings based on user behavior.




