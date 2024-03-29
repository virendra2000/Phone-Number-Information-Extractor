# Phone Number Information Extractor

## Overview

This project is designed to extract valuable information from a given phone number, providing insights into the location, timezone, carrier/service provider, and region associated with the number. The primary use case for this tool is in number verification, user authentication, and telecommunication analytics.

## Features

- Extracts country code and national number from the input phone number.
- Determines the timezone associated with the provided phone number.
- Identifies the carrier or service provider associated with the phone number.
- Specifies the region linked to the phone number.

## Usage

1. **Input:**
   Enter a phone number with the international dialing code.
    ```
    Enter Your Phone Number with +__: +91XXXXXXXXX9
    ```

2. **Output:**
    ```
    Your Entered Phone Number :
        Country Code: 91
        National Number: XXXXXXXXX9
    Timezone: ('Asia/Calcutta',)
    Carrier / Service Provider: Idea
    Region: India
    ```
## Installation

Clone the repository to your local machine:

```
https://github.com/virendra2000/Phone-Number-Information-Extractor.git
cd phone-number-info-extractor
```

### Install the required dependencies:

```
pip install phonenumbers
```

## How to Run

### Run the script and enter the phone number when prompted:

```
python phone_info_extractor.py
```

## Contributions

### Contributions are welcome! If you have any ideas for improvement or find any issues, feel free to open an issue or submit a pull request.

## License

### This project is licensed under the Apache License Version 2.0, January 2004 - see the LICENSE file for details.

### Feel free to modify this content as per your project's specifics.

