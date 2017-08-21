# Mini-Project: Movies Website

import media
import fresh_tomatoes

wu_kong = media.Movie("WU KONG",
                      "Release Date: 2017-07-13",
                      "Starring: Eddie Peng",
                      "http://cdn2.bjweekly.com/uploads/2017-07-17/12572091698070913969.jpg",# NOQA
                      "https://www.youtube.com/watch?v=gafv0BQ_1u0")

operation_mekong = media.Movie("Operation Mekong",
                               "Release Date: 2016-09-30",
                               "Starring: Eddie Peng",
                               "http://img.mp.itc.cn/upload/20170710/704baabfe664472e95ef4f1d23aa393e_th.jpg",# NOQA
                               "https://www.youtube.com/watch?v=WrY6n0gDuAc")

to_the_fore = media.Movie("TO THE FORE",
                          "Release Date: 2016-08-07",
                          "Starring: Eddie Peng",
                          "http://gb.cri.cn/mmsource/images/2015/07/23/ep150723037.jpg",# NOQA
                          "https://www.youtube.com/watch?v=Z7zUTmtuXkk")

hear_me = media.Movie("Hear Me",
                      "Release Date: 2015-08-28",
                      "Starring: Eddie Peng",
                      "http://image11.m1905.com/uploadfile/2009/0910/01141628896.jpg",# NOQA
                      "https://www.youtube.com/watch?v=3WGkMfxJEmE")

unbeatable = media.Movie("Unbeatable",
                         "Release Date: 2013-08-16",
                         "Starring: Eddie Peng",
                         "http://img31.mtime.cn/pi/2013/08/08/144758.80084104.jpg",# NOQA
                         "https://www.youtube.com/watch?v=Twg52dYvzmM")

jump_ashin = media.Movie("Jump Ashin",
                         "Release Date: 2011-12-09",
                         "Starring: Eddie Peng",
                         "http://photocdn.sohu.com/20111209/Img328496379.jpg",
                         "https://www.youtube.com/watch?v=psH3JQ4ZSJI")

movies = [wu_kong, operation_mekong, to_the_fore,
          hear_me, unbeatable, jump_ashin]
fresh_tomatoes.open_movies_page(movies)
