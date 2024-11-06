# Wind_Turbine_SCADA_open_data


## Table of open source wind turbine SCADA data sets:

|ID| Dataset                                                                                                        |Location       |Metast  |#TRB   |#Var   |Logs   |Annotations           |&Delta;t   |&sum;t        |Ref | Remarks/License  |
|- |-                                                                                                               |-              |-       |-      |-      |-      |-                     |-          |-             | -  |-                 |
|1 | [EDP Open Data Platform](https://www.edp.com/en/innovation/open-data)                                          |ESP (on)       |x       | 5     |~80    | x     | x<sup>[1](#fn1)</sup>| 10min     | 2y ('16-'17) |  - |  Need to register & log-in to the platform|
|2 | [Winji Gearbox Failure Detection Challenge](https://www.wedowind.ch/blog/winji-register)                       |?              |?       | 5     |~20    | x     | x<sup>[2](#fn2)</sup>| 10min     | 3y ('xx-'xx) |  - |  Need to register & no other application allowed without consent from WinJi AG | 
|3 | [Kelmarsh Wind Farm Data](https://zenodo.org/record/5841834#.YgpBQ_so-V7)                                      |UK (on)        |o       | 6     |~99     | x     | o                    | 10min<sup>[3](#fn3)</sup>     | 5y ('16-'21) |  - | [farm info](https://www.thewindpower.net/windfarm_en_17507_kelmarsh.php)|
|4 | [Penmanshiel Wind Farm Data](https://zenodo.org/record/5946808#.YgpAmvso-V5)                                   |UK (on)        |o       |14     |>150     | x     | o                   | 10min<sup>[3](#fn3)</sup>     | 5y ('16-'21) |  - | [farm info](https://www.thewindpower.net/windfarm_en_23147_penmanshiel.php) |
|5 | [Ørsted Anholt Offshore Wind Farm](https://orsted.com/en/our-business/offshore-wind/offshore-operational-data) |Denmark (off)  |(x)<sup>[4](#fn4)</sup>       | 111  | ?     | ?     | ?                    | 10min     | 2y           |  - | application/NDA required; wave buoy data; [farm info](https://www.thewindpower.net/windfarm_en_10687_anholt.php) |
|6 | [Ørsted Westermost Rough Wind Farm](https://orsted.com/en/our-business/offshore-wind/offshore-operational-data)|UK (off)       |(x)<sup>[4](#fn4)</sup>       | 35   | ?     | ?     | ?                    | 10min     | 2y           |  - | application/NDA required; wave buoy data; [farm info](https://www.thewindpower.net/windfarm_en_21826_westermost-rough.php) | 
|7a| ["CARE to Compare" WF B](https://data.niaid.nih.gov/resources?id=zenodo_10958774)                              |Germany (off)  |?       | 9    |  64| ?     | x                    | 10min     | 2y           |  - | data normalized for anonymization |
|7b| ["CARE to Compare" WF C](https://data.niaid.nih.gov/resources?id=zenodo_10958774)                              |Germany (off)  |?       | 22   | 238| ?     | x                  | 10min     | 2y          |  - | data normalized for anonymization |
|8a | [DS for Wind Energy WF1 onshore](https://zenodo.org/records/5516552)                                          |onshore        |x<sup>[5](#fn6)</sup>| 4     | 7     | o     | o      | 10min     | 1y           |  - | - |
|8b | [DS for Wind Energy WF1 offshore](https://zenodo.org/records/5516552)                                         |offshore       |x<sup>[5](#fn6)</sup>| 2     | 7     | o     | o      | 10min     | 1y           |  - | - | 
|8c | [DS for Wind Energy WF2 onshore](https://zenodo.org/records/5516554)                                          |onshore        |x<sup>[5](#fn6)</sup>| 2     | 7     | o     | o      | 10min     | 1y           |  - | - | 
|8d | [DS for Wind Energy WF2 offshore](https://zenodo.org/records/5516554)                                         |offshore       |x<sup>[5](#fn6)</sup>| 2     | 7     | o     | o      | 10min     | 1y           |  - | - | 
|9 | [Power Curve Working Group (PCWG) Data Sets](https://pcwg.org/)                                                |onshore        |x       | 3     | 1     | o     | o                   | 10min         | o       |  - | includes Lidar wind speed measurements |
|10| [Vestas V52 – Dundalk Institute of Technology Ireland](https://data.mendeley.com/datasets/tm988rs48k/2)        |Ireland (on)   |o       | 1     | 20   | o     | x<sup>[6](#fn6)</sup>| 10min     | 14y          |  - | Urban terrain |
|11| [Kaggle: Wind Turbine SCADA Dataset](https://www.kaggle.com/berkerisen/wind-turbine-scada-dataset)             |Turkey (on)    |o       | 1     | 4     | o     | o                    | 10min     | 1y ('18)     |  - | - | 
|12| [Urban Small Wind Turbine São Paulo](https://zenodo.org/records/7348454)                                       |Brazil (on)|o       | 1     | ~40   | o     | o                        | 1min      | 5y ('18-'23) |  - | Small, urban turbine | 
|13| [Engie "La Haute Borne" Wind Farm](https://opendata-renewables.engie.com/)                                     |FR (on)        |o       | 4     |~80    | o     | o                    | 10min     | 8y ('13-'20) | -  |  Not available anymore; [farm info](https://www.thewindpower.net/windfarm_en_3354_la-haute-borne-vaudeville-le-haut.php) |
|14| [Levenmouth Demonstration Turbine](https://pod.ore.catapult.org.uk/data-collection/ldt-turbine-scada-10min)    |UK (near)  |x       | 1     | >500  | x     | o                        | 10min/1sec| 3y ()'17-'20)|  - | Not for free (~2000 £) |

o = no / x = yes

<div id="fn1"><sup>1</sup> Manual annotations of major failures or component replacements </div>
<div id="fn2"><sup>2</sup> SCADA error log indicator</div>
<div id="fn3"><sup>3</sup> Higher resolution on request</div>
<div id="fn4"><sup>4</sup> Gearbox replacement in 2018-2019 </div>
<div id="fn5"><sup>5</sup> Environmental measures (except wind speed & TI) come from metmast </div>
<div id="fn6"><sup>6</sup> Ground-based LIDAR</div>

## Data Loaders and Overview Plots:
--- to be added ---

## Comunity Annotations:
--- to be added ---

## References:
Many of the above listed datasets are described and analysed in [1].

[1] [Effenberger, Nina, and Nicole Ludwig. "A collection and categorization of open‐source wind and wind power datasets." Wind Energy 25.10 (2022): 1659-1683.](https://onlinelibrary.wiley.com/doi/full/10.1002/we.2766)

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
