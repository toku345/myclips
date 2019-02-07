# myclips

[![Build Status](https://travis-ci.org/toku345/myclips.svg?branch=master)](https://travis-ci.org/toku345/myclips)
[![Maintainability](https://api.codeclimate.com/v1/badges/03ed229224b41962ea14/maintainability)](https://codeclimate.com/github/toku345/myclips/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/03ed229224b41962ea14/test_coverage)](https://codeclimate.com/github/toku345/myclips/test_coverage)


# Requirement

- [Vision Kit](https://aiyprojects.withgoogle.com/vision/)
- gpac
- [Slack Bot Token](https://slack.com/apps/A0F7YS25R-bots)
- Slack channel ID

``` console
# in Vision Kit(RaspberryPi)
$ sudo apt-get install -y gpac
```

# Installation

# Usage

https://slack.com/apps/A0F7YS25R-bots


``` console
$ cd /path/to/myclips
$ env SLACK_TOKEN=xxxxx SLACK_CHANNEL_ID=xxxxx python3 main.py
```

# Development

## Requirement

- Python 3.5.3
- gpac

``` console
# in macOS
$ brew install gpac
```

## Run test

``` console
$ cd /path/to/myclips
$ pip install -r requirements.txt
$ pytest
```
