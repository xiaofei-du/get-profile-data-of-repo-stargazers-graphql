# Get Profile Data Of Repo Stargazers GraghQL

This Python has almost the same function as [minimaxir / get-profile-data-of-repo-stargazers](https://github.com/minimaxir/get-profile-data-of-repo-stargazers), but rewritten using the GraphQL API of GitHub, which is much more faster and can overcome the scraw limit in page 1334 using the REST API.

![GH Limit using the REST API](./gh-api-limit.png)

I wrote this on my personal analysis project, the "StarTime-StarCount" chart in that project as below.

![](./chart.png)

This program will store stargazers' "username", "name", "email", "twitter_username", "repo_count", "blog", "company", "bio","avatar_url","hireable" , "num_followers", "num_following","created_at","star_time" in csv format.

## Usage

1. Get an access token from your GitHub account.

2. Run the script with:

   ```bash
   python main.py -r 'username/reponame' -t <GitHub Token>
   ```
3. Check the result file at `username_reponame_date.csv`

## Demo

```bash
➜  python3 main.py -t <GitHub Token Here> -r 'n0vad3v/get-profile-data-of-repo-stargazers-graphql'
100 users processed.
```

```bash
➜  cat n0vad3v__get-profile-data-of-repo-stargazers-graphql.csv
username,name,email,twitter_username,repo_count,blog,company,bio,avatar_url,hireable,num_followers,num_following,created_at,updated_at,star_time
abc1763613206,abc1763613206,,,30,https://abc1763613206.cf,Hanlin Network. @akioi,"The pupil who FAILED the OI.
            
Collaborator of 24OI/OI-wiki.
",https://avatars.githubusercontent.com/u/30773956?v=4,False,126,260,2017-08-06 13:42:03,2021-02-24 07:16:57,2019-04-02 13:07:42
HFO4,AaronLiu,abslant@foxmail.com,aaronliu00,23,https://blog.aoaoao.me/,@microsoft ,"Senior in college, major in Software Engineering.",https://avatars.githubusercontent.com/u/16058869?u=94f378906afe88a3ed3e35713b1fef33640ab156&v=4,True,1036,125,2015-11-28 13:25:43,2021-02-19 09:12:35,2019-04-03 00:27:38
zhengxu001,ztt,zhengxu5511@gmail.com,,22,,,,https://avatars.githubusercontent.com/u/5359345?v=4,True,13,6,2013-09-01 17:24:14,2021-01-07 11:04:46,2019-04-09 19:00:47
huan,Huan (李卓桓),zixia@zixia.net,huan_us,131,https://www.linkedin.com/in/zixia,@Chatie,"Angel Investor, Serial Entrepreneur, Machine Learning PhD Student, Microsoft AI MVP, Google ML GDE, Tencent TVP of Chatbot, Conversational AI Coder with 💖",https://avatars.githubusercontent.com/u/1361891?v=4,True,1143,79,2012-01-21 05:06:58,2021-02-24 05:54:37,2019-09-16 18:23:00
lijiarui,lijiarui,ruiruibupt@gmail.com,,49,https://rui.juzi.bot,@juzibot ,"Co-founder & CEO of JuziBot, Y Combinator Alumni,
Microsoft AI MVP          ",https://avatars.githubusercontent.com/u/6419514?u=0b8ced11f2fca649ed774d66e7d76e6feb19d074&v=4,False,775,40,2014-01-16 12:31:18,2021-02-15 05:46:15,2019-09-16 18:23:04
tianshanghong,Wei Wang,wwang255@usc.edu,,10,,University of Southern California,Explore frontline of civilization continuously.,https://avatars.githubusercontent.com/u/12212282?u=c0c4f4574ab946f73995622f8f636cda1fb2280c&v=4,False,36,162,2015-05-02 17:37:51,2021-02-24 18:04:34,2019-09-16 23:47:11
CZZLEGEND,,,,7,,,,https://avatars.githubusercontent.com/u/17879690?u=c473d1cde29b237c765b1fd368bd0d87c1c2f589&v=4,False,9,63,2016-03-16 13:01:29,2021-01-23 13:28:21,2019-09-18 06:40:55
vintagesucks,Nikolas Evers,,VintageSucks,20,https://nikol.as,@jungehaie,web developer,https://avatars.githubusercontent.com/u/13335308?u=277bfe00f78a5d45a98959ad34bb1e634804b4e9&v=4,False,81,330,2015-07-14 15:31:56,2021-02-19 14:36:28,2019-10-08 19:55:48
Edita2359,,,,0,,,,https://avatars.githubusercontent.com/u/58376949?v=4,False,0,2,2019-12-01 00:26:38,2019-12-19 07:02:38,2019-12-01 09:57:14
abaldwin88,Alex Baldwin,,,11,https://www.simplethread.com/,@simple-thread ,,https://avatars.githubusercontent.com/u/15172605?u=ec351428a12683f51eacf94c763bd8819201b6cd&v=4,False,21,7,2015-10-17 15:37:07,2021-02-23 22:18:58,2020-02-10 01:34:25
alei76,,leixy_hn@126.com,,27,,,,https://avatars.githubusercontent.com/u/6091534?v=4,False,41,1911,2013-12-03 03:03:36,2021-02-25 09:11:58,2020-02-26 13:32:14
nICEnnnnnnnLee,二土,,,36,https://nICEnnnnnnnLee.github.io,@ButterAndButterfly ,lol HoH WoW AoA VoV MoM XoX YoY ToT UoU QaQ,https://avatars.githubusercontent.com/u/19970934?u=c2b80c9627c14edcc9d2d885d8bebe7fb4dae773&v=4,False,40,7,2016-06-16 08:41:45,2021-02-25 13:50:15,2020-04-15 09:30:56
tukideng,Tuki,,,14,,,,https://avatars.githubusercontent.com/u/44869693?u=f061fafac850d4b247db46d291a84371bf42410d&v=4,False,5,2,2018-11-08 13:13:41,2021-02-17 13:00:17,2020-07-07 12:31:35
joel-jaimon,Joel Jaimon,joel.jaimon99@gmail.com,,15,https://joel-jaimon.herokuapp.com,,"Self- driven, Ambitious student. My goal is to grow as a person and as a professional everyday.",https://avatars.githubusercontent.com/u/64752455?u=058ac0a864d175c2630b78a27b48639ca644e209&v=4,True,11,8,2020-05-03 20:28:55,2021-02-19 06:14:03,2020-08-07 22:25:03
paper2code-bot,paper2code - bot,,paper2code,0,https://paper2code.com,@paper2code,Checking Github's trending repository for paper2code,https://avatars.githubusercontent.com/u/69664243?u=52eeb8ecf6189e51432391fac951f2922bee5077&v=4,False,110,95,2020-08-14 04:54:06,2020-09-20 10:52:07,2020-09-05 12:58:40
saber233,,,,4,,,,https://avatars.githubusercontent.com/u/11989805?v=4,False,3,6,2015-04-17 06:36:41,2021-02-18 06:44:18,2020-11-09 07:40:01
FluffyPanda69,Andrei Leuciuc,,,6,,,,https://avatars.githubusercontent.com/u/45459270?v=4,False,1,8,2018-11-29 13:36:47,2021-02-25 08:15:43,2021-02-25 17:15:31

```

## Author

Nova Kwok

## LICENSE

GPLv3
