# Get Profile Data Of Repo Stargazers GraghQL

This Python has almost the same function as [minimaxir / get-profile-data-of-repo-stargazers](https://github.com/minimaxir/get-profile-data-of-repo-stargazers), but rewritten using the GraphQL API of GitHub, which is much more faster and can overcome the scraw limit in page 1334 using the REST API.

![GH Limit using the REST API](./gh-api-limit.png)

I wrote this on my personal analysis project, the "StarTime-StarCount" chart in that project as below.

![](./chart.png)

This program will store stargazers' "username", "name", "email", "twitter_username", "repo_count", "blog", "company", "bio","avatar_url","hireable" , "num_followers", "num_following","created_at","star_time" in csv format.

## Usage

1. Get an [access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) from your GitHub account.

2. Run the script with:

   ```bash
   pip install -r requirements.txt
   python main.py -r 'username/reponame' -t <GitHub Token>
   ```
3. Check the result file at `username_reponame_date.csv`

## Demo

```bash
➜  python3 main.py -t <GitHub Token Here> -r 'n0vad3v/get-profile-data-of-repo-stargazers-graphql'
8/29 users processed.
```

```bash
➜  cat n0vad3v_get-profile-data-of-repo-stargazers-graphql_Sep-16-2023.csv
name,email,company,twitter_username,username,bio,num_followers,num_following,star_time,blog,repo_count,avatar_url,hireable,created_at,updated_at
abc1763613206,abc1763613206@163.com,@OI-wiki,,abc1763613206,"The pupil who FAILED the OI.
(upd: trying xcpc instead :) )
            
Collaborator of OI-wiki/OI-wiki.
",160,281,2019-04-02 13:07:42,https://hanlin.press,30,https://avatars.githubusercontent.com/u/30773956?v=4,False,2017-08-06 13:42:03,2023-09-11 00:58:28
AaronLiu,abslant.liu@gmail.com,@microsoft ,aaronliu00,HFO4,Toy Engineer,1473,151,2019-04-03 00:27:38,,24,https://avatars.githubusercontent.com/u/16058869?u=94f378906afe88a3ed3e35713b1fef33640ab156&v=4,True,2015-11-28 13:25:43,2023-09-11 03:49:56
ztt,zhengxu5511@gmail.com,,,zhengxu001,,12,6,2019-04-09 19:00:47,,23,https://avatars.githubusercontent.com/u/5359345?v=4,True,2013-09-01 17:24:14,2023-08-22 10:28:43
Huan Li,huan@chatie.io,@Chatie @PreAngel ,huan_us,huan,"Angel Investor, Serial Entrepreneur, Burner🔥! Microsoft AI MVP, Google ML GDE, Tencent TVP of Chatbot, Conversational AI Coder with 💖",2010,81,2019-09-16 18:23:00,https://www.linkedin.com/in/zixia,137,https://avatars.githubusercontent.com/u/1361891?v=4,True,2012-01-21 05:06:58,2023-08-27 08:31:01
lijiarui,ruiruibupt@gmail.com,@juzibot ,,lijiarui,"Co-founder & CEO of JuziBot, Y Combinator Alumni,
Microsoft AI MVP.     We are hiring! See: https://bit.ly/3ldGAIF         ",956,48,2019-09-16 18:23:04,https://rui.juzi.bot,47,https://avatars.githubusercontent.com/u/6419514?u=233af74883c2ce69b636767940976bb428557e82&v=4,False,2014-01-16 12:31:18,2023-07-30 06:55:25
,leixy_hn@126.com,,,alei76,,85,3987,2020-02-26 13:32:14,,29,https://avatars.githubusercontent.com/u/6091534?v=4,False,2013-12-03 03:03:36,2023-01-28 06:09:24
Santosh Bhavani,santosh.bhavani@live.com,@nvidia,santosh_bhavani,sbhavani,,6,47,2022-06-16 23:17:05,,17,https://avatars.githubusercontent.com/u/182751?v=4,False,2010-01-15 06:17:49,2023-06-14 05:19:53
Venkat Raman,vraman2811@gmail.com,@tiyaro,Venkat2811,Venkat2811,Senior Software Engineer,29,41,2022-06-24 13:24:12,http://Venkat2811.com,15,https://avatars.githubusercontent.com/u/10533729?u=80d9204e1deb291508282f866aec988da89841a5&v=4,True,2015-01-14 16:10:01,2023-07-24 15:01:42
```

## Author

Nova Kwok

## LICENSE

GPLv3
