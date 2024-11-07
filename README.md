# Wind_Turbine_SCADA_open_data


## Table of open source wind turbine SCADA data sets:

|ID| Dataset                                                                                                        |Loc       |Met-<br>mast  |Trb<br>#   |Var<br>#   |Logs<br>x/o  |Labels           |&Delta;T   |&sum;T       |Ref | Remarks/License  |
|--|----------------------------------------------------------------------------------------------------------------|-              |-       |-      |-      |-      |-                     |-          |-             | -  |-                 |
|1 | [EDP Open Data](https://www.edp.com/en/innovation/open-data)                                          |ESP (on)       |x       | 5     |~80    | x     | x<sup>[1](#fn1)</sup>| 10min     | 2y |  - |  register & log-in to platform|
|2 | [Winji Gearbox Challenge](https://www.wedowind.ch/blog/winji-register)                       |?              |?       | 5     |~20    | x     | x<sup>[2](#fn2)</sup>| 10min     | 3y |  - |  register & consent from WinJi | 
|3 | [Kelmarsh Farm](https://zenodo.org/record/5841834#.YgpBQ_so-V7)                                      |UK (on)        |o       | 6     |~99     | x     | o                    | 10min<sup>[3](#fn3)</sup>     | 5y|  - | [farm info](https://www.thewindpower.net/windfarm_en_17507_kelmarsh.php)|
|4 | [Penmanshiel Farm](https://zenodo.org/record/5946808#.YgpAmvso-V5)                                   |UK (on)        |o       |14     |>150     | x     | o                   | 10min<sup>[3](#fn3)</sup>     | 5y|  - | [farm info](https://www.thewindpower.net/windfarm_en_23147_penmanshiel.php) |
|5 | [Ørsted Anholt Offshore](https://orsted.com/en/our-business/offshore-wind/offshore-operational-data) |DEN (off)  |(x)<sup>[4](#fn4)</sup>       | 111  | ?     | ?     | ?                    | 10min     | 2y           |  - | application/NDA; [farm info](https://www.thewindpower.net/windfarm_en_10687_anholt.php) |
|6 | [Ørsted Westermost Rough](https://orsted.com/en/our-business/offshore-wind/offshore-operational-data)|UK (off)       |(x)<sup>[4](#fn4)</sup>       | 35   | ?     | ?     | ?                    | 10min     | 2y           |  - | application/NDA; [farm info](https://www.thewindpower.net/windfarm_en_21826_westermost-rough.php) | 
|7a| ["CAREtoCompare" Wind Farm B](https://data.niaid.nih.gov/resources?id=zenodo_10958774)                              |GER (off)  |?       | 9    |  64| ?     | x                    | 10min     | 2y           |  - | data normalized for anonymization |
|7b| ["CAREtoCompare" Wind Farm C](https://data.niaid.nih.gov/resources?id=zenodo_10958774)                              |GER (off)  |?       | 22   | 238| ?     | x                  | 10min     | 2y          |  - | data normalized for anonymization |
|8 | [Fuhrländer Farm](https://github.com/alecuba16/fuhrlander)                              |? (on)  |o       | 5   | 78| x     | o                  | 5min     | 3y          |  [[2]](#ref2) | - |
|9a | [DSforWind Wind Farm 1a](https://zenodo.org/records/5516552)                                          |? (on)        |x<sup>[6](#fn6)</sup>| 4     | 7     | o     | o      | 10min     | 1y           |  - | - |
|9b | [DSforWind Wind Farm1b](https://zenodo.org/records/5516552)                                         |? (off)       |x<sup>[6](#fn6)</sup>| 2     | 7     | o     | o      | 10min     | 1y           |  - | - | 
|9c | [DSforWind Wind Farm 2a](https://zenodo.org/records/5516554)                                          |? (on)        |x<sup>[6](#fn6)</sup>| 2     | 7     | o     | o      | 10min     | 1y           |  - | - | 
|9d | [DSforWind Wind Farm 2b](https://zenodo.org/records/5516554)                                         |? (off)       |x<sup>[6](#fn6)</sup>| 2     | 7     | o     | o      | 10min     | 1y           |  - | - | 
|10 | [PCWG Data Sets](https://pcwg.org/)                                                |? (on)        |x       | 3     | 1     | o     | o                   | 10min         | o       |  - | - |
|11| [Dundalk IoT](https://data.mendeley.com/datasets/tm988rs48k/2)        |IRE (on)   |o       | 1     | 20   | o     | x<sup>[7](#fn7)</sup>| 10min     | 14y          |  - | urban terrain |
|12| [Kaggle Wind Turbine](https://www.kaggle.com/berkerisen/wind-turbine-scada-dataset)             |TUR (on)    |o       | 1     | 4     | o     | o                    | 10min     | 1y|  - | - | 
|13| [Small São Paulo](https://zenodo.org/records/7348454)                                       |BRZ (on)|o       | 1     | ~40   | o     | o                        | 1min      | 5y|  - | small, urban turbine | 
|14| [Engie La Haute Borne](https://opendata-renewables.engie.com/)                                     |FR (on)        |o       | 4     |~80    | o     | o                    | 10min     | 8y| -  |  offline; [farm info](https://www.thewindpower.net/windfarm_en_3354_la-haute-borne-vaudeville-le-haut.php) |
|15| [Levenmouth Turbine](https://pod.ore.catapult.org.uk/data-collection/ldt-turbine-scada-10min)    |UK (near)  |x       | 1     | >500  | x     | o                        | 10min/1sec| 3y|  - | not for free (~2000 £) |

o = no / x = yes

<div id="fn1"><sup>1</sup> Manual annotations of major failures or component replacements </div>
<div id="fn2"><sup>2</sup> SCADA error log indicator</div>
<div id="fn3"><sup>3</sup> Statistics from wave buoy and ground-based LIDAR data.</div>
<div id="fn4"><sup>4</sup> Higher resolution on request</div>
<div id="fn5"><sup>5</sup> Environmental measures (except wind speed & TI) come from metmast </div>
<div id="fn6"><sup>6</sup> Ground-based LIDAR</div>
<div id="fn7"><sup>7</sup> Gearbox replacement in 2018-2019 </div>

## Data Loaders and Overview Plots:
--- to be added ---

## Comunity Annotations:
--- to be added ---

## References:
Many of the above listed datasets are described and analysed in [[1]](#ref1).

<div id="ref1">[1]</div>[Effenberger, Nina, and Nicole Ludwig. "A collection and categorization of open‐source wind and wind power datasets." Wind Energy 25.10 (2022): 1659-1683.](https://onlinelibrary.wiley.com/doi/full/10.1002/we.2766)

<div id="ref2">[2]</div>[Marti-Puig, P., Blanco-M., A., Cusidó, J. et al. Wind turbine database for intelligent operation and maintenance strategies. Sci Data 11, 255 (2024).](https://www.nature.com/articles/s41597-024-03067-9#citeas)


## How to contribute:
We welcome contributions to expand the collection of open datasets in this repository. If you have an open dataset you'd like to add, please feel free to submit a new pull request.
To contribute a new dataset:

1. Open a new issue in the repository and describe the dataset you would like to add, including the following information:
- Dataset name and Source URL
- Brief description
- License or terms of use
- Any other relevant details


2. Fork the repository to your own GitHub account.
3. Add the new dataset to the Datasets table in the README.md file, following the existing format.
4. Commit your changes and push them to your forked repository.
5. Submit a pull request, referencing the issue you opened earlier. The maintainers will review your contribution and merge it if it meets the repository's guidelines.

We appreciate all contributions that help expand the collection of open datasets available in this repository. If you have any questions or need assistance, please don't hesitate to open a new issue.
