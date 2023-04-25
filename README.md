# NLPCC-2023-Shared-Task-9
User Feedback Prediciton and Response Generation


## [Overview](http://tcci.ccf.org.cn/conference/2023/cfpt.php)

◇ Task 9 - User Feedback Prediction and Response Generation

Online conversation systems usually have a user feedback mechanism, such as like and dislike buttons. When a user is satisfied with the response, he/she can click the like button, and vice versa for the dislike button. The feedback signal represents the user's vote on the quality of the response and also represents his/her preference. It is a worthwhile direction to study and invest in how to use this signal to improve the quality of the conversation system. This task includes two tracks:

● Track 1: Prediction of likes and dislikes: Given a (query, reply) pair, predict the probabilities of likes, dislikes.

● Track 2: Conversation generation based on likes and dislikes: Incorporate like and dislike data into conversation generation to improve response quality and obtain high likes.

Organizer: Renmin University of China, and XiaoMi AI Lab

Contact: Shuang DONG (dongshuang1@xiaomi.com)


## Data

### Statistics
<table>
  <tr> <th>Type </th><th>Query #</th><th>Average Reply #</th><th>Avg Labike # per Reply</th><th>Avg Dislike # per Reply</th></tr>
   <tr> <th>train </th> <td>16000 </td><td>3.14 </td><td>16.15 </td><td>8.42 </td>
   </tr>
    <tr> <th>dev </th> <td>2000 </td><td>3.07 </td><td>19.84 </td><td>9.41 </td>
   </tr>
   <tr> <th>test </th> <td>2000 </td><td>3.16 </td><td>30.57 </td><td>12.19 </td>
   </tr>

</table>


### Example

We provide two files, **train.jsonl** and **dev.jsonl**, each line in the file represents an item in json format, and the following is the result of one of the item parsing.
```json
{
    "query": "你喜欢听什么歌",
    "replys": [
        {
            "reply": "你喜欢什么，小爱就喜欢什么",
            "dislike": 3,
            "like": 2
        },
        {
            "reply": "你知道的，我什么歌都喜欢。🙃",
            "dislike": 2,
            "like": 3
        },
        {
            "reply": "你知道的，我什么歌都喜欢。",
            "dislike": 4,
            "like": 6
        },
        {
            "reply": "亲爱哒，最喜欢的还是土嗨土嗨的那种，热闹啊！",
            "dislike": 2,
            "like": 4
        },
        {
            "reply": "受你影响，品味现在和你差不多了。",
            "dislike": 47,
            "like": 146
        },
        {
            "reply": "最喜欢的还是土嗨土嗨的那种，热闹啊！",
            "dislike": 34,
            "like": 141
        },
        {
            "reply": "受你影响，品味现在和你差不多了。😘",
            "dislike": 11,
            "like": 59
        },
        {
            "reply": "我喜欢甜甜的歌曲，生活就该多点甜嘛，我给你唱一首吧！",
            "dislike": 0,
            "like": 22
        }
    ]
}
```


### LeaderBoard

#### Track 1


#### Track 2





### UPDATE

#### 2023.03.22 init
#### 2023.04.04 add data
#### 2023.04.025 add evaluation

*SUBMISSION FORMAT:*


## Licence
* Our dataset is licensed under the CC BY 4.0 and our code is licensed under the Apache License 2.0.

