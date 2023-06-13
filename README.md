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
Final result：
<table>
  <tr> <th>排名 </th><th>队伍名</th><th>机构</th><th>分数</th></tr>
  <tr> <th>1 </th> <td>师弟师妹带带我 </td><td>大连理工大学、吉林大学 </td><td>92.13 </td></tr>
  <tr> <th>2 </th> <td>dunnlp </td><td>易盾 </td><td>92.00 </td></tr>
  <tr> <th>3 </th> <td>zut </td><td>中原工学院 </td><td>91.73 </td></tr>
  <tr> <th>4 </th> <td>YNU-HPCC </td><td>云南大学 </td><td>91.63 </td></tr>
  <tr> <th>5 </th> <td>HTDZNLP </td><td>杭州航天电子技术有限公司 </td><td>91.40 </td></tr>
  <tr> <th>6 </th> <td>666 </td><td>浙江工业大学 </td><td>91.24 </td></tr>
  <tr> <th>7 </th> <td>Tryourbest classification </td><td>苏州大学 </td><td>90.94 </td></tr>
  <tr> <th>8 </th> <td>little_spice </td><td>天津科技大学 </td><td>90.72 </td></tr>
</table>


#### Track 2
Final reuslt:
<table>
  <tr> <th>排名 </th><th>队伍名</th><th>机构</th><th>分数</th></tr>
  <tr> <th>1 </th> <td>YNU-HPCC </td><td>云南大学 </td><td>1.656 </td></tr>
  <tr> <th>2 </th> <td>Devs </td><td>东北大学 </td><td>1.562 </td></tr>
  <tr> <th>3 </th> <td>little -spice </td><td>天津科技大学 </td><td>1.409 </td></tr>
  <tr> <th>4 </th> <td>666 </td><td>浙江工业大学 </td><td>1.388 </td></tr>
  <tr> <th>5 </th> <td>ZUT </td><td>中原工学院 </td><td>1.214 </td></tr>
  <tr> <th>6 </th> <td>HTDZNLP </td><td>杭州航天电子技术有限公司 </td><td>1.202 </td></tr>
</table>



### SUBMISSION FORMAT
#### Track 1
For Track 1, the test dataset is named ```datasets_test_track1.jsonl```, which consists of 1500 samples. Participants are required to submit their results with the same number of rows as the test dataset. Each row should contain multiple scores separated by tabs (\t). The number of scores in each row represents the number of replies corresponding to the query. The required format is as follows:
```
0.6
0.6
...
0.6\t0.6\t0.6
```
For each question-answer pair, a probability distribution of 0 and 1 scores is computed based on the ratio of likes and dislikes. The scores are calculated using the formula 1/(1+kl), where kl represents the Kullback-Leibler divergence between the predicted probability distribution and the ground truth. Please refer to the ```evaluation.py``` file for more detailed information.
#### Track 2
For Track 2, the test dataset is named ```datasets_test_track2.jsonl```, which contains 500 samples. Participants are also required to submit their results with the same number of rows as the test dataset. Each row should contain the reply results corresponding to the query. The format should be as follows:
```
不喜欢
在呢
...
不好意思，刚刚走神了
```
We will use manual annotations to assign scores to each reply, with possible scores of 0 (unlikely to be liked), 1 (potentially liked), and 2 (highly likely to be liked). The final score will be the average of these scores.

### UPDATE

#### 2023.03.22 init
#### 2023.04.04 add data
#### 2023.04.25 add evaluation
#### 2023.05.22 add test data

## Licence
* Our dataset is licensed under the CC BY 4.0 and our code is licensed under the Apache License 2.0.

