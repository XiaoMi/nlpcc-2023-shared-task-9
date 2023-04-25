import json
import math
import os


def kl_sim_score(gold, pred):
    score = 0
    for x, y in zip(gold, pred):
        x = max(x, 1e-6)
        x = min(x, 1 - 1e-6)
        y = max(y, 1e-6)
        y = min(y, 1 - 1e-6)
        sc1 = x * math.log(x) + (1 - x) * math.log(1 - x)
        sc2 = x * math.log(y) + (1 - x) * math.log(1 - y)
        score += 1 / (1 + sc1 - sc2)
    return score / len(gold)


def fake_pred(gold_file, pred_file):
    with open(gold_file, 'r', encoding='utf-8') as fr, \
            open(pred_file, 'w', encoding='utf-8') as fw:
        for line in fr:
            d = json.loads(line)
            pred = ['0.66' for i in range(len(d['replys']))]
            fw.write('\t'.join(pred) + '\n')


def evaluation(gold_file, pred_file):
    df = open(gold_file, 'r', encoding='utf-8')
    pf = open(pred_file, 'r', encoding='utf-8')
    scores = []
    for dx, px in zip(df, pf):
        data = json.loads(dx)
        gold = [d['like'] / (d['like'] + d['dislike']) for d in data['replys']]
        pred = [float(x) for x in px.split()]
        assert len(data['replys']) == len(pred)
        scores.append(kl_sim_score(gold, pred))
    df.close()
    pf.close()
    return sum(scores) / len(scores) * 100


if __name__ == "__main__":
    gold_file = "datasets_dev.jsonl"
    pred_file = "predict.txt"
    if not os.path.exists(pred_file):
        fake_pred(gold_file, pred_file)
    print(evaluation(gold_file, pred_file))
