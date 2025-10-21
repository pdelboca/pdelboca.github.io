title: ckan-rescue: A Python package to rescue (download) CKAN data portals.
date: 2025-09-06

Based on [my experience rescuing Argentinian Data Portals](https://www.youtube.com/watch?v=8dUyi4OYAdM) _[*]_ at the beginning of 2024, I decided to create a small Python cli tool to quiclky download the portal metadata and and all its files. I have some of this logic as part of [django-dcat](https://github.com/pdelboca/django-dcat) but I wanted to extract it into its own package so it is easier to use for people whose only requiement is just to download all the data.

The usage is quite simple, just open a terminal and run:

```
uvx --from ckan-rescue ckan-dcat-download https://datos.gob.ar/data.json
```

The previous command will download the DCAT file with the full metadata and all its files (distributions) in a structured `output` folder. The package is open source, published to PyPi and the code is available in Github: [https://github.com/pdelboca/ckan-rescue](https://github.com/pdelboca/ckan-rescue)

For now, it only works for all the CKAN portals that exports its metadata in a DCAT json file (usually CKAN instances implementing [ckanext-datajson](https://github.com/GSA/ckanext-datajson) but soon I will be adding more features to be able to download from the native CKAN API.


<small>_[*] Luckily all the Argentinian data portals are still up and running! You can visit the main one at [https://datos.gob.ar](https://datos.gob.ar)_</small>
