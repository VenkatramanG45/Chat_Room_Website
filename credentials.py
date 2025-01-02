import dj_database_url

db_url = "postgresql://chat_room_db_pc4a_user:MelFgDXEB532eBWcGz2C1gwI3okZc4Od@dpg-ctr2hfrtq21c73aedmu0-a.oregon-postgres.render.com/chat_room_db_pc4a"

db_config = dj_database_url.parse(db_url)

# Extract the components (this is more explicit than relying on dj_database_url's dictionary keys directly)
username = db_config['USER']
password = db_config['PASSWORD']
host = db_config['HOST']
database_name = db_config['NAME']


print(f"Username: {username}")
print(f"Password: {password}")
print(f"Host: {host}")
print(f"Database Name: {database_name}")

#In your settings.py use these values like below:

