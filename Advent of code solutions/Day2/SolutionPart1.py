def is_safe_report(report):
    increasing = None
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff > 0:
            if increasing is None:
                increasing = True
            elif increasing is False:
                return False
        elif diff < 0:
            if increasing is None:
                increasing = False
            elif increasing is True:
                return False
    return True
with open('Day2/input.txt') as f:
    lines = f.read().splitlines()
safe_reports_count = 0
for line in lines:
    report = list(map(int, line.split()))
    if is_safe_report(report):
        safe_reports_count += 1
print(f"Total safe reports: {safe_reports_count}")