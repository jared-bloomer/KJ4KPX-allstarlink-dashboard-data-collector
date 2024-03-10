## Description

The files in this repository are used to extract data from an [AllstarLink Node](https://allstarlink.org/) and push it to an [InfluxDB database](https://www.influxdata.com/lp/influxdb-database/?msclkid=9d29bdfb600c1cd23b32d81038793c04).

### Technologies Used

The files in this repository are built using the following technologies:

* [Python](https://www.python.org/)
* [pyenv](https://github.com/pyenv/pyenv)

### Installation

These steps are assuming you already have git and pyenv installed and properly configured on your system. If you do not have those things done, please do those steps first. 

1. Run the command `git clone https://github.com/jared-bloomer/KJ4KPX-allstarlink-dashboard-data-collector.git`
2. Change into the newly created directory with the commnd `cd KJ4KPX-allstarlink-dashboard-data-collector`
3. Ensure the proper version of python is installed using pyend with the command `pyenv install $(cat .python-version)`
4. Activate pyenv with the command `pyenv activate`
5. Install dependent python packages with the command `pip install -f requirements.txt`
6. Copy `config.ini.example` to a file named `config.ini`
7. Edit the file `config.ini` with the appropriate configuration values for your environment

You may now execute any of the scripts manually in this directory. If you wish to use crontab to run the scripts for you, and example crontab entry to run the scripts every minute would be 

```
* * * * * /root/KJ4KPX-allstarlink-dashboard-data-collector/getStats.sh >> /var/log/getStats.log 2>&1;
```

| :warning: WARNING          |
|:---------------------------|
| It is not recommended to attempt to run any of the python scripts (files ending in `.py`) from crontab directly. This is due to needing to properly load `pyenv` before executing the python script. Please reference `getStats.sh` as an example wrapper to execute those python scripts from crontab. |


