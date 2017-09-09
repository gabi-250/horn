#!/usr/bin/python3

import argparse


def main(args):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play audio files.')
    parser.add_argument('-t', '--track-list',
                        help='the list of tracks to play',
                        default=[], nargs='+')
    args = parser.parse_args()
    main(args=args.track_list)
