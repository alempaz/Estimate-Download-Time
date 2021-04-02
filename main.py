def main():
    print('-' * 20, 'Time left for a download (GB or MB)', '-' * 20, '\nOn what unit is your file? (Answer Gb or Mb!):')
    while True:
        answer_unit = input('\t> ').lower()
        if answer_unit in ['gb', 'gigabyte', 'g']:
            # size_gb()
            get_size(True)
            break
        elif answer_unit in ['mb', 'megabyte', 'm']:
            get_size(False)
            break
        else:
            print('Please, type a valid unit. (GB - Gigabyte // MB - Megabyte)')


def get_size(flag):
    print('What is the size of your file?:')
    while True:
        try:
            answer_size = float(input('\t> '))
            if flag:
                get_download_speed(answer_size, True)
            else:
                get_download_speed(answer_size, False)
            break
        except ValueError:
            print('Please, type a valid size.')


def get_download_speed(size, flag):
    print('What is your current download speed? (Type the speed in mbps)')
    while True:
        try:
            answer_speed = float(input('\t> '))
            if flag:
                calculate_time(size, answer_speed, True)
            else:
                calculate_time(size, answer_speed, False)
            break
        except ValueError:
            print('Please, type a valid download speed.')


def calculate_time(size, speed, flag):
    if flag:
        _total_seconds = (size * 1024) / speed
    else:
        _total_seconds = size / speed

    _days_left = _total_seconds // (24 * 3600)
    _total_seconds = _total_seconds % (24 * 3600)

    _hours_left = _total_seconds // 3600
    _total_seconds %= 3600

    _minutes_left = _total_seconds // 60
    _total_seconds %= 60

    _seconds_left = _total_seconds
    estimated_time(_days_left, _hours_left, _minutes_left, _seconds_left)


def estimated_time(days, hours, minutes, seconds):
    print(f'\n\tTime left for your file to download: {int(days)} Day(s) -- '
          f'{int(hours)} Hour(s) -- {int(minutes)} Minutes -- {int(seconds)} Seconds. ')
    try_again()


def try_again():
    print('\n Type any key to get a new conversion. Type N to quit:')
    answer = input('> ').lower()
    if answer != 'n':
        if __name__ == '__main__':
            main()
    else:
        print('GoodBye')
        exit()


if __name__ == '__main__':
    main()
