from github_art.datepoints import GithubDatePoints

def test_datetime_star_point():
    points = GithubDatePoints(())
    start_point = points.get_datetime_start_point()
    assert start_point