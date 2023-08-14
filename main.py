import program as p
import api_ticker as a


def main():
    p.run_program(a.ticker, a.api_key)
    
if __name__ == '__main__':
    main()