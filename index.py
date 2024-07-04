def solution(A, F, M):
    total_sum_needed = (len(A) + F) * M
    sum_needed_for_F = total_sum_needed - sum(A)

    if sum_needed_for_F < F or sum_needed_for_F > 6 * F:
        return [0]

    result = [1] * F
    forgotten_sum_needed = sum_needed_for_F - F  

    
    for i in range(F):
        add_value = min(5, forgotten_sum_needed)
        result[i] += add_value
        forgotten_sum_needed -= add_value

    return result
