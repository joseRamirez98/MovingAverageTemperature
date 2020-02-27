# Moving Average Temperature

This python program computes the moving average temperature for each year in a given window period specified by the user. Data temperatures and corresponding years are contained within the csv file named "NorCal-1880-2018". The data begins with the year 1800 and ends in 2018. Each year's calculated moving average temperature is written to a new csv file named moving_average.

##  Calculation for the moving average.

First, prompt the user to input a window period for which they would like to calculate the moving average. Then create a range for the years to be used for the calculation, which is found through using the first year in the csv file + (plus) the window period and the last year in the csv file - (minus) the window period. For example, the first year in the csv file is 1880 and the last is 2018. Given a 60 year window period, the range for this calculation is 1940-1958. Now, let i equal a year contained within the given range, and let k equal the specified window period. The calculation goes as follows: moving_average = (i-k.temperature + ... + i-2.temperature + i-1.temperature + i.temperature + i+1.temperature + i+2.temperature + ... + i+k.temperature) / (2 * k + 1). In the stated example, to calculate the moving average temperture for the year 1940, sum the temperature values from 1880 through 2000 and divid by two times the window period plus one. This process would be repeated for all the years contained in the range.

### Prerequisites

The prerequisite for this program is the "NorCal-1880-2018" csv file, which is included in the repository.

### Example Output
Given a window period of 60, the output of the moving_average csv file should be the following:

Year:    1940     1941    1942  ...   1956    1957     1958

Value: -0.2331  -0.2169  -0.215 ... -0.142  -0.1101  -0.1017

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
