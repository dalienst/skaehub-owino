import statistics

num = [59, 69, 45, 83, 55, 10]

def basic_stat(num):
    num_mean = statistics.mean(num)
    num_mode = statistics.mode(num)
    num_variance = statistics.variance(num)
    num_median = statistics.median(num)

    dict_stats = {
        'mean':num_mean,
        'mode':num_mode,
        'variance':num_variance,
        'median':num_median
    }

    return dict_stats

print(basic_stat(num))