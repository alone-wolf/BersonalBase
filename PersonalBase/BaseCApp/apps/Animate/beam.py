class AnimateNode:
    Title: str
    CurrentEpisode: int
    BaseUrl: str
    SiteTitle: str

    def __init__(self, title, current_episode, base_url, site_title):
        self.Title = title
        self.CurrentEpisode = current_episode
        self.BaseUrl = base_url
        self.SiteTitle = site_title

    def to_object(self):
        return {
            "title": self.Title,
            "currentEpisode": self.CurrentEpisode,
            "baseUrl": self.BaseUrl,
            "siteTitle": self.SiteTitle
        }