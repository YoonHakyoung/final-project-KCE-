import argparse

def run_load_test(url, initial_user_count, additional_user_count, interval_time, repeat_count, test_id):
    print(f"Running load test on {url} with {initial_user_count} initial users, adding {additional_user_count} users every {interval_time} seconds, for {repeat_count} times.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run load test.')
    parser.add_argument('--url', type=str, required=True, help='Target URL')
    parser.add_argument('--initial_user_count', type=int, required=True, help='Initial number of users')
    parser.add_argument('--additional_user_count', type=int, required=True, help='Additional number of users')
    parser.add_argument('--interval_time', type=int, required=True, help='Interval time between adding users')
    parser.add_argument('--repeat_count', type=int, required=True, help='Number of times to add users')
    parser.add_argument('--test_id', type=int, required=True, help='Test ID')

    args = parser.parse_args()
    
    run_load_test(args.url, args.initial_user_count, args.additional_user_count, args.interval_time, args.repeat_count, args.test_id)
