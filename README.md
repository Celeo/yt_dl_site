# yt_dl_site

A very simple site that allows pasting YouTube URLs and will download them to the server via [youtube-dl](https://github.com/ytdl-org/youtube-dl).

## Installing

1. Install [poetry](https://python-poetry.org/)
1. Clone the repo
1. Install dependencies with `poetry install`

## Using

1. Copy the `config.example.json` file to `config.json`
1. Populate with a password to use
1. Run with `poetry run python main.py`

## Developing

### Building

### Requirements

* Git
* Poetry
* Python 3.7+

### Steps

```sh
git clone https://github.com/Celeo/yt_dl_site
cd yt_dl_site
poetry install
```

### Running tests

`poetry run pytest`

## License

Licensed under MIT ([LICENSE](LICENSE)).

## Contributing

Please feel free to contribute. Please open an issue first (or comment on an existing one) so that I know that you want to add/change something.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, as defined in the Apache-2.0 license,
shall be dual licensed as above, without any additional terms or conditions.
