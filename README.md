# CSS Test Calculator

Critical Swim Speed (CSS) is an important metric to understand in the world of swimming. It measures the fastest speed a swimmer can sustain for a given distance without getting tired. Coaches mainly use CSS to set training zones and predict race times. 

Critical Swim Speed Pace is determined by swimming a 200m and a 400m time trial and look at the difference between the times.

  CSS Pace [in secs/100m] = (T400 - T200)/2

The CSS Test Calculator is a Python GUI application created using `tkinter` that allows you to calculate the Critical Swim Speed (CSS) based on the input of 400m and 200m swim times. It also provides options to export the data in XLSX format for your records.

## Features

- Calculate CSS based on 400m and 200m swim times.
- Add and manage multiple test data entries.
- Export data in different formats for further analysis.

## Prerequisites

- Python 3.x
- Required Python libraries: `tkinter`, `pandas`, and `reportlab`

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/vickerys79/css-test-calculator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd css-test-calculator
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Launch the application by running `main.py`.
2. Enter swim test data into the table by filling in the following fields:
   - **Name:** Name of the swim test.
   - **400m Time (mm:ss):** The time taken to swim 400 meters in the format `mm:ss`.
   - **200m Time (mm:ss):** The time taken to swim 200 meters in the format `mm:ss`.

3. Click the "Calculate CSS" button to calculate the Critical Swim Speed (CSS). The CSS will be displayed in the "CSS" column for each entry.

4. To export data, click the "Export Data" button. You will be prompted to enter the file location to save the exported data.

5. The exported data will be saved in XLSX format for your records.

## Contributing

If you would like to contribute to this project or have suggestions for improvements, please follow these steps:

1. Fork the project.
2. Create a new branch for your feature or bugfix: `git checkout -b feature/my-feature` or `git checkout -b bugfix/issue-description`.
3. Make your changes and commit them:  `git commit -m "Your message here"`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Create a pull request to the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Name: Stephen Vickery
- Email: vickerys79@outlook.com
- GitHub: [vickerys79](https://github.com/vickerys79)

## Acknowledgments

This project was created with the help of `tkinter`, `pandas`, and `reportlab`.

## Contact

For any questions or feedback, you can contact the author via email.

Enjoy using the CSS Test Calculator!
