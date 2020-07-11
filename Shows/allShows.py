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