import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Loaded CSV files with the 'signup_date' and 'event_time' alongwith columns parsed as dates
users_df = pd.read_csv("users.csv", parse_dates=["signup_date"])
events_df = pd.read_csv("events.csv", parse_dates=["event_time"])

# Merged the two dataframes (events_df and users_df) on the 'user_id' column
merged_df = pd.merge(events_df, users_df, on="user_id", how="left")

# Calculated the number of days since each user signed up. Helping to track user activity based on the time since signup
merged_df["days_since_signup"] = (merged_df["event_time"] - merged_df["signup_date"]).dt.days


# 1. Calculated Day 1 Retention Rate

# Filtered the merged data to get users who had an event on Day 1 (days_since_signup == 1)
day1_retention = merged_df[merged_df["days_since_signup"] == 1][["user_id", "group"]].drop_duplicates()

# - Counted the number of unique users in each group (control and test) who retained on Day 1
day1_counts = day1_retention.groupby("group")["user_id"].nunique()

# Counted the total signups per group (control and test)
signup_counts = users_df.groupby("group")["user_id"].nunique()

# Calculated the Day 1 retention rate for each group: Day 1 Retention Rate = (Number of users who retained / Total number of users in group)
retention_rate_day1 = (day1_counts / signup_counts).fillna(0).round(3)


# 2. Calculated Day 7 Retention Rate (same approach)

# Filtered the merged data to get users who had an event on Day 7 (days_since_signup == 7)
day7_retention = merged_df[merged_df["days_since_signup"] == 7][["user_id", "group"]].drop_duplicates()

# Counted the number of unique users in each group (control and test) who retained on Day 7
day7_counts = day7_retention.groupby("group")["user_id"].nunique()

# Calculated the Day 7 retention rate for each group: Day 7 Retention Rate = (Number of users who retained / Total number of users in group)
retention_rate_day7 = (day7_counts / signup_counts).fillna(0).round(3)


# 3. Calculated Subscription Conversion Rate for the Test Group

# Filtered the merged data to include only users in the test group
test_group_df = merged_df[merged_df["group"] == "test"]

# Counted the number of unique users in the test group who signed up for a subscription
# Subscription signup event type is assumed to be 'subscription_signup' and it's counted within 7 days after signup
subscribed_users = test_group_df[
    (test_group_df["event_type"] == "subscription_signup") &  # Filtered by subscription signup event
    (test_group_df["days_since_signup"] <= 7)  # Only consider signups within 7 days after the user signed up
]["user_id"].nunique()  # Also unique

# The total number of signups in the test group (regardless of subscription)
total_test_signups = users_df[users_df["group"] == "test"]["user_id"].nunique()

# Calculated the subscription conversion rate in the test group: Conversion Rate = (Number of users who subscribed / Total number of test group users)
subscription_conversion_rate = round(subscribed_users / total_test_signups, 3)


# 4. Performed Statistical Significance Test (Z-Test) on Day 7 Retention Rates between Control and Test Groups

# The number of users retained on Day 7 in the control and test groups.
control_day7 = day7_retention[day7_retention["group"] == "control"]["user_id"].nunique()
test_day7 = day7_retention[day7_retention["group"] == "test"]["user_id"].nunique()

# - The total number of signups for control and test groups
control_total = signup_counts.get("control", 0)
test_total = signup_counts.get("test", 0)

# - Setup the number of successes (retained users on Day 7) and the total number of users in each group
successes = np.array([control_day7, test_day7])
totals = np.array([control_total, test_total])

# Performed a Z-test to check if the difference in Day 7 retention rates between control and test groups is statistically significant
z_stat, p_val = proportions_ztest(successes, totals)


# 5. Output: Printing all calculated metrics and the result of the Z-test

print("Day 1 Retention Rate:\n", retention_rate_day1)
print("Day 7 Retention Rate:\n", retention_rate_day7)
print("Subscription Conversion Rate (Test Group):", subscription_conversion_rate)
print("Z-Statistic:", round(z_stat, 3))  # Test statistic from the Z-test
print("P-Value:", round(p_val, 3))  # P-value from the Z-test, indicates statistical significance


# Result Output:

Day 1 Retention Rate:
 group
control    0.432
test       0.214
Name: user_id, dtype: float64
Day 7 Retention Rate:
 group
control    0.227
test       0.304
Name: user_id, dtype: float64
Subscription Conversion Rate (Test Group): 0.321
Z-Statistic: -0.853
P-Value: 0.394
