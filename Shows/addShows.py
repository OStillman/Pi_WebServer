import urllib.request as request
import urllib.parse as parse
import json
import time

class AddShow():
    def __init__(self, service, offset=0):
        self.url = "https://www.freesat.co.uk/tv-guide/api/{}/?channel={}".format(offset, service)
        self.offset = offset

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset):
        self._offset = offset

    def fetch(self, test=False):
        if not test:
            req = request.Request(url=self.url, method='GET')
            request.urlopen(req)
            print(request.urlopen(req).read().decode('utf-8'))
            self.show_data = json.loads(request.urlopen(req).read().decode('utf-8'))
        else:
            if self.offset == 0:
                self.show_data = [{"event": [{"duration": 10800, "description": "The latest news, sport, business and weather from the BBC's Breakfast team. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p06j7xvr.jpg", "evtId": 13099, "tstv": {"mediaLocation": "channel=919&programmeid=m000kk9p&ui_id=4.0.0", "availabilityEnd": 1593849600, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593763200}, "startTime": 1593752400, "hasTstv": True, "name": "Breakfast"}, {"duration": 3600, "description": "The latest national and international stories as they break. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p07jbsw9.jpg", "evtId": 13100, "tstv": {"mediaLocation": "channel=919&programmeid=m000kk9t&ui_id=4.0.0", "availabilityEnd": 1593853200, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593766800}, "startTime": 1593763200, "hasTstv": True, "name": "BBC News"}, {"svcId": 512, "seriesNo": 1, "episodeNo": 15, "duration": 2700, "image": "/ms/img/epg/rb/8df1-p08h310p.jpg", "evtId": 13101, "description": "15/15. As the country starts to consider a return to normality, Matt Allwright and Kym Marsh present a live, one-stop shop for the nation's burning consumer questions. Also in HD. [S]", "tstv": {"mediaLocation": "channel=919&programmeid=m000kk9y&ui_id=4.0.0", "availabilityEnd": 1625219100, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593769500}, "startTime": 1593766800, "hasTstv": True, "name": "Your Money and Your Life"}, {"svcId": 512, "seriesNo": 33, "episodeNo": 19, "duration": 3600, "image": "/ms/img/epg/rb/8df1-p056mv0c.jpg", "evtId": 13102, "description": "19/80. Martin visits a terrace in Mountain Ash in Wales, Martel looks around a bungalow in Gillingham, Kent, and Dion checks out a derelict property in Walsall. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m0005qc9&ui_id=4.0.0", "availabilityEnd": 1596365100, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593773100}, "startTime": 1593769500, "hasTstv": True, "name": "Homes Under The Hammer"}, {"svcId": 512, "seriesNo": 8, "episodeNo": 16, "duration": 1800, "image": "/ms/img/chan/chan-MobilePlaceholder-512.png", "evtId": 13103, "description": "16/20. A jeweller refuses to budge even though he's looking down the barrel of a gun, and a pair of pet pilferers steal a tortoise from a zoo. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m000dcg6&ui_id=4.0.0", "availabilityEnd": 1596366900, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593774900}, "startTime": 1593773100, "hasTstv": True, "name": "Caught Red Handed"}, {"duration": 2700, "seriesNo": 56, "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08j2xmp.jpg", "evtId": 13104, "description": "Christina Trevanion presents today's show. The reds and blues will be battling it out in Lewes High Street. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m000kkb1&ui_id=4.0.0", "availabilityEnd": 1596369600, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593775800}, "startTime": 1593774900, "hasTstv": True, "name": "Bargain Hunt"}, {"duration": 1800, "description": "The latest national and international news from the BBC. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p087fq0y.jpg", "evtId": 13105, "tstv": {"mediaLocation": "channel=919&programmeid=_DTT_m000kkb5&ui_id=4.0.0", "availabilityEnd": 1593865800, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593779400}, "startTime": 1593777600, "hasTstv": True, "name": "BBC News at One"}, {"svcId": 512, "description": "The latest news, sport and weather for the Midlands. [S]", "episodeNo": 68, "duration": 900, "image": "/ms/img/epg/rb/8df1-p07gmln9.jpg", "evtId": 13106, "tstv": {"mediaLocation": "channel=919&programmeid=m000km2j&ui_id=4.0.0", "availabilityEnd": 1593866700, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593780300}, "startTime": 1593779400, "hasTstv": True, "name": "Midlands Today"}, {"svcId": 512, "seriesNo": 1, "episodeNo": 15, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p08hshvr.jpg", "evtId": 13107, "description": "15/30. Indulging his addiction, Mark deserts his kids. Ana and Ryan each try to win over Watto. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m000kkb9&ui_id=4.0.0", "availabilityEnd": 1627046100, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593782100}, "startTime": 1593780300, "hasTstv": True, "name": "The Heights"}, {"svcId": 512, "seriesNo": 3, "episodeNo": 5, "duration": 2700, "image": "/ms/img/epg/rb/8df1-p04lwpn2.jpg", "evtId": 13108, "description": "5/30. Game show in which players score points by answering questions correctly while avoiding the impossible answers. Also in HD. [S]", "tstv": {"mediaLocation": "channel=919&programmeid=b09bbvs8&ui_id=4.0.0", "availabilityEnd": 1596376800, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593784800}, "startTime": 1593782100, "hasTstv": True, "name": "Impossible"}, {"svcId": 512, "seriesNo": 31, "episodeNo": 40, "duration": 2700, "image": "/ms/img/epg/rb/8df1-p04qmb0x.jpg", "evtId": 13109, "description": "40/70. Margherita Taylor visits Shropshire with a couple of keen gardeners on a \u00a3425,000 budget who want to buy a home with space for them and their hot tub. Also in HD. [S,AD]", "startTime": 1593784800, "hasTstv": False, "name": "Escape to the Country"}, {"svcId": 512, "seriesNo": 1, "episodeNo": 20, "duration": 2700, "image": "/ms/img/chan/chan-MobilePlaceholder-512.png", "evtId": 13110, "description": "20/30. In the Bidding Room today, the dealers go head to head over a religious statue, a pair of Bakelite phones, a glimpse into the future and a piece of rock n roll history. Also in HD. [S]", "startTime": 1593787500, "hasTstv": False, "name": "The Bidding Room"}, {"svcId": 512, "description": "The latest news including a Downing Street news conference on the coronavirus pandemic. Also in HD. [S]", "episodeNo": 103, "duration": 5400, "image": "/ms/img/epg/rb/8df1-p07hp9l7.jpg", "evtId": 13474, "startTime": 1593790200, "hasTstv": False, "name": "Coronavirus Update"}, {"duration": 1800, "description": "The latest national and international news stories from the BBC News team, followed by weather. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p086zs44.jpg", "evtId": 13113, "startTime": 1593795600, "hasTstv": False, "name": "BBC News at Six"}, {"svcId": 512, "description": "The latest news, sport and weather for the Midlands. [S]", "episodeNo": 68, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p07gmln9.jpg", "evtId": 13114, "startTime": 1593797400, "hasTstv": False, "name": "Midlands Today"}, {"duration": 1800, "description": "Alex Jones and Alex Scott present the 3000th edition of the show, with Katherine Jenkins and Spaced stars Simon Pegg & Jessica Hynes. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08jckj2.jpg", "evtId": 13115, "startTime": 1593799200, "hasTstv": False, "name": "The One Show"}, {"svcId": 512, "seriesNo": 15, "episodeNo": 2, "duration": 3600, "image": "/ms/img/epg/rb/8df1-p08jp7hk.jpg", "evtId": 13116, "description": "2/18. The first set of heats continue, with four food-obsessed celebrities competing for a semi-final spot. Also in HD. [S,AD]", "startTime": 1593801000, "hasTstv": False, "name": "Celebrity Masterchef"}, {"svcId": 512, "seriesNo": 15, "episodeNo": 3, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p08jp7lq.jpg", "evtId": 13117, "description": "3/18. The remaining four celebrities compete for the first two semi-final places. Also in HD. [S,AD]", "startTime": 1593804600, "hasTstv": False, "name": "Celebrity Masterchef"}, {"svcId": 512, "seriesNo": 2, "episodeNo": 5, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p08f5wbr.jpg", "evtId": 13118, "description": "5/7. With her mum refusing to go, Cathy's hen do invitees are Auntie Dawn, Marilyn, Cat and an old school friend. It doesn't turn out to be the classy, edifying affair Cathy wanted. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=p08d6wws&ui_id=4.0.0", "availabilityEnd": 1602882000, "sid": 919, "mediaAvailable": True, "availabilityStart": 1591387680}, "startTime": 1593806400, "hasTstv": True, "name": "The Other One"}, {"svcId": 512, "seriesNo": 2, "episodeNo": 2, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p064kys7.jpg", "evtId": 13119, "description": "2/4. John and Kayleigh are full of high spirits as they head off on their annual works do. Contains some strong language and some scenes of a sexual nature. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=p04wytv3&ui_id=4.0.0", "availabilityEnd": 1604093400, "sid": 919, "mediaAvailable": True, "availabilityStart": 1589574600}, "startTime": 1593808200, "hasTstv": True, "name": "Peter Kay's Car Share"}, {"duration": 1800, "description": "The latest national and international news, with reports from BBC correspondents worldwide. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08j0mn3.jpg", "evtId": 13120, "startTime": 1593810000, "hasTstv": False, "name": "BBC News at Ten"}, {"svcId": 512, "description": "The latest news, sport and weather for the Midlands. [S]", "episodeNo": 68, "duration": 900, "image": "/ms/img/epg/rb/8df1-p07gmln9.jpg", "evtId": 13121, "startTime": 1593811800, "hasTstv": False, "name": "Midlands Today"}, {"duration": 6900, "description": "To clear his debts, a rancher agrees to escort a dangerous criminal to trial. Contains some strong language and some violent scenes. Also in HD. [2007] [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08hz3lm.jpg", "evtId": 13122, "startTime": 1593812700, "hasTstv": False, "name": "3:10 To Yuma (2007)"}, {"duration": 300, "description": "Detailed weather forecast. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p07hbz98.jpg", "evtId": 13123, "startTime": 1593819600, "hasTstv": False, "name": "Weather for the Week Ahead"}, {"duration": 18900, "description": "BBC One joins the BBC's rolling news channel for a night of news. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p07tdcv8.jpg", "evtId": 13124, "startTime": 1593819900, "hasTstv": False, "name": "BBC News"}], "channelid": "512", "offset": 0}]
            else:
                self.show_data = [{"event": [{"duration": 10800, "description": "The latest news, sport, business and weather from the BBC's Breakfast team. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p06j7xvr.jpg", "evtId": 13099, "tstv": {"mediaLocation": "channel=919&programmeid=m000kk9p&ui_id=4.0.0", "availabilityEnd": 1593849600, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593763200}, "startTime": 1593752400, "hasTstv": True, "name": "Breakfast"}, {"duration": 3600, "description": "The latest national and international stories as they break. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p07jbsw9.jpg", "evtId": 13100, "tstv": {"mediaLocation": "channel=919&programmeid=m000kk9t&ui_id=4.0.0", "availabilityEnd": 1593853200, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593766800}, "startTime": 1593763200, "hasTstv": True, "name": "BBC News"}, {"svcId": 512, "seriesNo": 1, "episodeNo": 15, "duration": 2700, "image": "/ms/img/epg/rb/8df1-p08h310p.jpg", "evtId": 13101, "description": "15/15. As the country starts to consider a return to normality, Matt Allwright and Kym Marsh present a live, one-stop shop for the nation's burning consumer questions. Also in HD. [S]", "tstv": {"mediaLocation": "channel=919&programmeid=m000kk9y&ui_id=4.0.0", "availabilityEnd": 1625219100, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593769500}, "startTime": 1593766800, "hasTstv": True, "name": "Your Money and Your Life"}, {"svcId": 512, "seriesNo": 33, "episodeNo": 19, "duration": 3600, "image": "/ms/img/epg/rb/8df1-p056mv0c.jpg", "evtId": 13102, "description": "19/80. Martin visits a terrace in Mountain Ash in Wales, Martel looks around a bungalow in Gillingham, Kent, and Dion checks out a derelict property in Walsall. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m0005qc9&ui_id=4.0.0", "availabilityEnd": 1596365100, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593773100}, "startTime": 1593769500, "hasTstv": True, "name": "Homes Under The Hammer"}, {"svcId": 512, "seriesNo": 8, "episodeNo": 16, "duration": 1800, "image": "/ms/img/chan/chan-MobilePlaceholder-512.png", "evtId": 13103, "description": "16/20. A jeweller refuses to budge even though he's looking down the barrel of a gun, and a pair of pet pilferers steal a tortoise from a zoo. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m000dcg6&ui_id=4.0.0", "availabilityEnd": 1596366900, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593774900}, "startTime": 1593773100, "hasTstv": True, "name": "Caught Red Handed"}, {"duration": 2700, "seriesNo": 56, "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08j2xmp.jpg", "evtId": 13104, "description": "Christina Trevanion presents today's show. The reds and blues will be battling it out in Lewes High Street. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m000kkb1&ui_id=4.0.0", "availabilityEnd": 1596369600, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593775800}, "startTime": 1593774900, "hasTstv": True, "name": "Bargain Hunt"}, {"duration": 1800, "description": "The latest national and international news from the BBC. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p087fq0y.jpg", "evtId": 13105, "tstv": {"mediaLocation": "channel=919&programmeid=_DTT_m000kkb5&ui_id=4.0.0", "availabilityEnd": 1593865800, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593779400}, "startTime": 1593777600, "hasTstv": True, "name": "BBC News at One"}, {"svcId": 512, "description": "The latest news, sport and weather for the Midlands. [S]", "episodeNo": 68, "duration": 900, "image": "/ms/img/epg/rb/8df1-p07gmln9.jpg", "evtId": 13106, "tstv": {"mediaLocation": "channel=919&programmeid=m000km2j&ui_id=4.0.0", "availabilityEnd": 1593866700, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593780300}, "startTime": 1593779400, "hasTstv": True, "name": "Midlands Today"}, {"svcId": 512, "seriesNo": 1, "episodeNo": 15, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p08hshvr.jpg", "evtId": 13107, "description": "15/30. Indulging his addiction, Mark deserts his kids. Ana and Ryan each try to win over Watto. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=m000kkb9&ui_id=4.0.0", "availabilityEnd": 1627046100, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593782100}, "startTime": 1593780300, "hasTstv": True, "name": "The Heights"}, {"svcId": 512, "seriesNo": 3, "episodeNo": 5, "duration": 2700, "image": "/ms/img/epg/rb/8df1-p04lwpn2.jpg", "evtId": 13108, "description": "5/30. Game show in which players score points by answering questions correctly while avoiding the impossible answers. Also in HD. [S]", "tstv": {"mediaLocation": "channel=919&programmeid=b09bbvs8&ui_id=4.0.0", "availabilityEnd": 1596376800, "sid": 919, "mediaAvailable": True, "availabilityStart": 1593784800}, "startTime": 1593782100, "hasTstv": True, "name": "Impossible"}, {"svcId": 512, "seriesNo": 31, "episodeNo": 40, "duration": 2700, "image": "/ms/img/epg/rb/8df1-p04qmb0x.jpg", "evtId": 13109, "description": "40/70. Margherita Taylor visits Shropshire with a couple of keen gardeners on a \u00a3425,000 budget who want to buy a home with space for them and their hot tub. Also in HD. [S,AD]", "startTime": 1593784800, "hasTstv": False, "name": "Escape to the Country"}, {"svcId": 512, "seriesNo": 1, "episodeNo": 20, "duration": 2700, "image": "/ms/img/chan/chan-MobilePlaceholder-512.png", "evtId": 13110, "description": "20/30. In the Bidding Room today, the dealers go head to head over a religious statue, a pair of Bakelite phones, a glimpse into the future and a piece of rock n roll history. Also in HD. [S]", "startTime": 1593787500, "hasTstv": False, "name": "The Bidding Room"}, {"svcId": 512, "description": "The latest news including a Downing Street news conference on the coronavirus pandemic. Also in HD. [S]", "episodeNo": 103, "duration": 5400, "image": "/ms/img/epg/rb/8df1-p07hp9l7.jpg", "evtId": 13474, "startTime": 1593790200, "hasTstv": False, "name": "Different Show"}, {"duration": 1800, "description": "The latest national and international news stories from the BBC News team, followed by weather. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p086zs44.jpg", "evtId": 13113, "startTime": 1593795600, "hasTstv": False, "name": "BBC News at Six"}, {"svcId": 512, "description": "The latest news, sport and weather for the Midlands. [S]", "episodeNo": 68, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p07gmln9.jpg", "evtId": 13114, "startTime": 1593797400, "hasTstv": False, "name": "Midlands Today"}, {"duration": 1800, "description": "Alex Jones and Alex Scott present the 3000th edition of the show, with Katherine Jenkins and Spaced stars Simon Pegg & Jessica Hynes. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08jckj2.jpg", "evtId": 13115, "startTime": 1593799200, "hasTstv": False, "name": "The One Show"}, {"svcId": 512, "seriesNo": 15, "episodeNo": 2, "duration": 3600, "image": "/ms/img/epg/rb/8df1-p08jp7hk.jpg", "evtId": 13116, "description": "2/18. The first set of heats continue, with four food-obsessed celebrities competing for a semi-final spot. Also in HD. [S,AD]", "startTime": 1593801000, "hasTstv": False, "name": "Celebrity Masterchef"}, {"svcId": 512, "seriesNo": 15, "episodeNo": 3, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p08jp7lq.jpg", "evtId": 13117, "description": "3/18. The remaining four celebrities compete for the first two semi-final places. Also in HD. [S,AD]", "startTime": 1593804600, "hasTstv": False, "name": "Celebrity Masterchef"}, {"svcId": 512, "seriesNo": 2, "episodeNo": 5, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p08f5wbr.jpg", "evtId": 13118, "description": "5/7. With her mum refusing to go, Cathy's hen do invitees are Auntie Dawn, Marilyn, Cat and an old school friend. It doesn't turn out to be the classy, edifying affair Cathy wanted. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=p08d6wws&ui_id=4.0.0", "availabilityEnd": 1602882000, "sid": 919, "mediaAvailable": True, "availabilityStart": 1591387680}, "startTime": 1593806400, "hasTstv": True, "name": "The Other One"}, {"svcId": 512, "seriesNo": 2, "episodeNo": 2, "duration": 1800, "image": "/ms/img/epg/rb/8df1-p064kys7.jpg", "evtId": 13119, "description": "2/4. John and Kayleigh are full of high spirits as they head off on their annual works do. Contains some strong language and some scenes of a sexual nature. Also in HD. [S,AD]", "tstv": {"mediaLocation": "channel=919&programmeid=p04wytv3&ui_id=4.0.0", "availabilityEnd": 1604093400, "sid": 919, "mediaAvailable": True, "availabilityStart": 1589574600}, "startTime": 1593808200, "hasTstv": True, "name": "Peter Kay's Car Share"}, {"duration": 1800, "description": "The latest national and international news, with reports from BBC correspondents worldwide. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08j0mn3.jpg", "evtId": 13120, "startTime": 1593810000, "hasTstv": False, "name": "BBC News at Ten"}, {"svcId": 512, "description": "The latest news, sport and weather for the Midlands. [S]", "episodeNo": 68, "duration": 900, "image": "/ms/img/epg/rb/8df1-p07gmln9.jpg", "evtId": 13121, "startTime": 1593811800, "hasTstv": False, "name": "Midlands Today"}, {"duration": 6900, "description": "To clear his debts, a rancher agrees to escort a dangerous criminal to trial. Contains some strong language and some violent scenes. Also in HD. [2007] [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p08hz3lm.jpg", "evtId": 13122, "startTime": 1593812700, "hasTstv": False, "name": "3:10 To Yuma (2007)"}, {"duration": 300, "description": "Detailed weather forecast. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p07hbz98.jpg", "evtId": 13123, "startTime": 1593819600, "hasTstv": False, "name": "Weather for the Week Ahead"}, {"duration": 18900, "description": "BBC One joins the BBC's rolling news channel for a night of news. Also in HD. [S]", "svcId": 512, "image": "/ms/img/epg/rb/8df1-p07tdcv8.jpg", "evtId": 13124, "startTime": 1593819900, "hasTstv": False, "name": "BBC News"}], "channelid": "512", "offset": 0}]
        
    def search(self, supplied_name):
        self.fetch(test=True)
        listing = []
        for show in self.show_data[0]['event']:
            if self.checkMatch(show["name"], supplied_name):
                listing.append(self.pullOutInfo(show))
        if len(listing) == 0:
            listing.append(["Error, show not found", self.offset])
        return listing

    def checkMatch(self, show_name, supplied_name):
        if supplied_name.lower() in show_name.lower():
            return True
        else:
            return False

    def pullOutInfo(self, matched_show):
        return [self.fixDateTime(matched_show["startTime"]), matched_show['evtId']]


    def fixDateTime(self, epoch):
        return time.strftime('%A %B %d, %Y %H:%M:%S', time.localtime(epoch))

