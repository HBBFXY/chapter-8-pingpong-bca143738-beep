import random

def simulate_single_game(win_rate_a):
    """模拟单局比赛（11分制，净胜2分）"""
    score_a, score_b = 0, 0
    while True:
        # 根据胜率随机决定得分方
        if random.random() < win_rate_a:
            score_a += 1
        else:
            score_b += 1
        
        # 判断局分胜负
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 1 if score_a > score_b else 0

def simulate_match(win_rate_a, best_of=5):
    """模拟一场比赛（五局三胜制）"""
    wins_a, wins_b = 0, 0
    while wins_a < best_of//2 + 1 and wins_b < best_of//2 + 1:
        result = simulate_single_game(win_rate_a)
        if result == 1:
            wins_a += 1
        else:
            wins_b += 1
    return 1 if wins_a > wins_b else 0

def analyze_competition(win_rate_a, match_count=1000):
    """统计多场比赛的结果，分析竞技规律"""
    a_wins = 0
    for _ in range(match_count):
        a_wins += simulate_match(win_rate_a)
    win_rate = a_wins / match_count
    print(f"选手A胜率{win_rate_a*100}%时，{match_count}场比赛获胜{win_rate*100:.2f}%")
    return win_rate

# 示例：选手A每球胜率60%，模拟1000场比赛
analyze_competition(win_rate_a=0.6, match_count=1000)# 在这个文件里编写代码
