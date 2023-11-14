# Titiler-PgSTAC
Fork of [https://github.com/stac-utils/titiler-pgstac] with added ability to replace hrefs coming in from pgstac database with hrefs from another stac-fastapi, which is used for
blob signing purposes.


## Environment Variables

The application can be configured using the following environment variables:

| Variable                        | Description |
| ------------------------------- | ----------- |
| `HOST`                          | Application host address |
| `PORT`                          | Application host port |
| `WEB_CONCURRENCY`               | Number of worker processes |
| `WORKERS_PER_CORE`              | Number of workers per core |
| `POSTGRES_USER`                 | Postgres user |
| `POSTGRES_PASS`                 | Postgres password |
| `POSTGRES_DBNAME`               | Postgres database name |
| `POSTGRES_HOST`                 | Postgres host |
| `POSTGRES_PORT`                 | Postgres port (default is 5432) |
| `DB_MIN_CONN_SIZE`              | Minimum database connection pool size |
| `DB_MAX_CONN_SIZE`              | Maximum database connection pool size |
| `GDAL_CACHEMAX`                 | GDAL raster block cache size |
| `GDAL_DISABLE_READDIR_ON_OPEN`  | GDAL configuration for opening directories |
| `GDAL_INGESTED_BYTES_AT_OPEN`   | Number of bytes to ingest when GDAL opens a file |
| `GDAL_HTTP_MERGE_CONSECUTIVE_RANGES` | GDAL configuration for merging HTTP ranges |
| `GDAL_HTTP_MULTIPLEX`           | GDAL configuration for HTTP multiplexing |
| `GDAL_HTTP_VERSION`             | GDAL HTTP version |
| `VSI_CACHE`                     | Enable/disable GDAL's VSI caching mechanism |
| `VSI_CACHE_SIZE`                | Size of GDAL's VSI cache |
| `CPL_VSIL_CURL_CACHE_SIZE`      | Size of GDAL's CURL cache |
| `MOSAIC_CONCURRENCY`            | Concurrency level for mosaic processing |
| `TITILER_PGSTAC_HREF_EXCHANGE_ENABLED` | Enable/disable HREF exchange in TiTiler PgSTAC |
| `TITILER_PGSTAC_HREF_EXCHANGE_STAC_FASTAPI_URL` | URL for STAC FastAPI in TiTiler PgSTAC |


<p align="center">
  <img width="500" src="https://github.com/stac-utils/titiler-pgstac/assets/10407788/24a64ea9-fede-4ee8-ab8d-625c9e94db44"/>
  <p align="center">Connect PgSTAC and TiTiler.</p>
</p>

<p align="center">
  <a href="https://github.com/stac-utils/titiler-pgstac/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/developmentseed/titiler/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/stac-utils/titiler-pgstac" target="_blank">
      <img src="https://codecov.io/gh/stac-utils/titiler-pgstac/branch/main/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/titiler.pgstac" target="_blank">
      <img src="https://img.shields.io/pypi/v/titiler.pgstac?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/stac-utils/titiler-pgstac/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/titiler-pgstac.svg" alt="License">
  </a>
</p>

---

**Documentation**: <a href="https://stac-utils.github.io/titiler-pgstac/" target="_blank">https://stac-utils.github.io/titiler-pgstac/</a>

**Source Code**: <a href="https://github.com/stac-utils/titiler-pgstac" target="_blank">https://github.com/stac-utils/titiler-pgstac</a>

---

**TiTiler-PgSTAC** is a [TiTiler](https://github.com/developmentseed/titiler) extension that connects to a [PgSTAC](https://github.com/stac-utils/pgstac) database to create dynamic **mosaics** based on [search queries](https://github.com/radiantearth/stac-api-spec/tree/master/item-search).

## Installation

To install from PyPI and run:

```bash
# Make sure to have pip up to date
$ python -m pip install -U pip

# Install `psycopg` or `psycopg["binary"]` or `psycopg["c"]`
$ python -m pip install psycopg["binary"]

$ python -m pip install titiler.pgstac
```

To install from sources and run for development:

```
$ git clone https://github.com/stac-utils/titiler-pgstac.git
$ cd titiler-pgstac
$ python -m pip install -e .
```

### `PgSTAC` version

`titiler.pgstac` depends on `pgstac >=0.3.4` (https://github.com/stac-utils/pgstac/blob/main/CHANGELOG.md#v034).

### `psycopg` requirement

`titiler.pgstac` depends on the `psycopg` library. Because there are three ways of installing this package (`psycopg` or , `psycopg["c"]`, `psycopg["binary"]`), the user must install this separately from `titiler.pgstac`.

- `psycopg`: no wheel, pure python implementation. It requires the `libpq` installed in the system.
- `psycopg["binary"]`: binary wheel distribution (shipped with libpq) of the `psycopg` package and is simpler for development. It requires development packages installed on the client machine.
- `psycopg["c"]`: a C (faster) implementation of the libpq wrapper. It requires the `libpq` installed in the system.

`psycopg[c]` or `psycopg` are generally recommended for production use.

In `titiler.pgstac` setup.py, we have added three options to let users choose which psycopg install to use:

- `pip install titiler.pgstac["psycopg"]`: pure python
- `pip install titiler.pgstac["psycopg-c"]`: use the C wrapper (requires development packages installed on the client machine)
- `pip install titiler.pgstac["psycopg-binary"]`: binary wheels

## Launch

You'll need to have `POSTGRES_USER`, `POSTGRES_PASS`, `POSTGRES_DBNAME`, `POSTGRES_HOST`, `POSTGRES_PORT` variables set in your environment pointing to your Postgres database where pgstac has been installed.

```
export POSTGRES_USER=username
export POSTGRES_PASS=password
export POSTGRES_DBNAME=postgis
export POSTGRES_HOST=database
export POSTGRES_PORT=5432
```

```
$ pip install uvicorn
$ uvicorn titiler.pgstac.main:app --reload
```

### Using Docker

```
$ git clone https://github.com/stac-utils/titiler-pgstac.git
$ cd titiler-pgstac
$ docker-compose up --build tiler
```

It runs `titiler.pgstac` using Gunicorn web server. To run Uvicorn based version:

```
$ docker-compose up --build tiler-uvicorn
```

## Contribution & Development

See [CONTRIBUTING.md](https://github.com//stac-utils/titiler-pgstac/blob/main/CONTRIBUTING.md)

## License

See [LICENSE](https://github.com//stac-utils/titiler-pgstac/blob/main/LICENSE)

## Authors

See [contributors](https://github.com/stac-utils/titiler-pgstac/graphs/contributors) for a listing of individual contributors.

## Changes

See [CHANGES.md](https://github.com/stac-utils/titiler-pgstac/blob/main/CHANGES.md).
