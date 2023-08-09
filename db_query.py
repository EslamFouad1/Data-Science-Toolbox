conn = sqlite3.connect("data/user_data.db")
conn

query = 'SELECT * FROM users'
users = pd.read_sql(query, conn)
users.head()


query = 'SELECT * FROM device'
device = pd.read_sql(query, conn)
device.head()


query = 'SELECT * FROM transactions'
transactions = pd.read_sql(query, conn)
transactions.head()


# Aggregate data on the number of transactions and the total amount.
query = '''
SELECT user_id, COUNT(*) AS number_transactions, SUM(amount_usd) AS total_amount_USD
FROM transactions
GROUP BY user_id
'''
transactions_agg = pd.read_sql(query, conn)
transactions_agg.head()


# Do a left join, as all users in the users table are of interest.
query = '''
SELECT left_table.*, right_table.device
FROM users AS left_table
LEFT JOIN device AS right_table
ON left_table.user_id = right_table.user_id
'''
users_w_device = pd.read_sql(query, conn)
users_w_device.head()
