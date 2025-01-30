from db.connection import connect_to_test_db


def seed_db():
    db = connect_to_test_db()
    db.run('DROP TABLE if exists artist_follower_count')

    db.run(
        'CREATE TABLE artist_follower_count (\
        artist_id SERIAL PRIMARY KEY,\
        artist_name TEXT, \
        follower_count INT NOT NULL, \
        recorded_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP \
        )'
    )

    db.close()
