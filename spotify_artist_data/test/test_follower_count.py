from spotify_artist_data.src.follower_count import follower_count

def test_returns_string_with_artist_name_and_followers():
    result = follower_count("Mamas Gun")
    print(result)
    assert "Artist: Mamas Gun, Followers:" in result
