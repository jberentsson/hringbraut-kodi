#!/usr/bin/env python3
from hringbraut import Hringbraut

if __name__ == '__main__':
    hr = Hringbraut()

    out = hr.get_shows()
    print(out)

    out = hr.get_episodes('/sjonvarp/thaettir/man/')
    print(out)

    out = hr.get_episode('/sjonvarp/thaettir/bryggjan/bryggjan-6mars/')
    print(out)