from Shows import db


class GetAllLiveShows():
    def __init__(self):
        self.AllLiveShows = db.AllLiveShows()

    def retrieveShows(self):
        end_data = {"Planner": {"Shows": []}}
        for show in self.AllLiveShows.liveshowsQuery():
            print(show)
            this_data = {
                "id": show[0],
                "name": show[1],
                "channel": show[8],
                "series": show[5],
                "episode": show[4]
            }
            end_data["Planner"]["Shows"].append(this_data)
        return end_data

class GetAllODShows():
    def __init__(self):
        self.AllDBShows = db.FetchODShows()

    def retrieveShows(self):
        #ODShows.id, ODShows.name, channels.name, watching, episode, series
        end_data = {"Planner": {"Shows": []}}
        for show in self.AllDBShows.odshowsQuery():
            print(show)
            this_show_tags = self.GetTags(show[0])
            this_data = {
                "id": show[0],
                "name": show[1],
                "channel": show[2],
                "watching": show[3],
                "series": show[5],
                "episode": show[4],
                "tags": this_show_tags
            }
            end_data["Planner"]["Shows"].append(this_data)
        return end_data

    def GetTags(self, show_id):
        tags = []
        fetched_tags = db.ODShowTags(show_id).showTagsQuery()
        for tag in fetched_tags:
            tags.append(tag[0])
        return tags