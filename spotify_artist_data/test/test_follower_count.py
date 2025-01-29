from spotify_artist_data.src.follower_count import follower_count

def test_returns_dict_with_artist_name_and_followers():
    result = follower_count("Mamas Gun")
    print(result)
    assert result["artist"] == "Mamas Gun"
    assert type(result["followers"]) is int

def test_returns_artist_not_found_for_incorrect_artist_names():
    result = follower_count("ajsdfhu3123s")
    print(result)
    assert result == "Error, artist not found"
