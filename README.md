# Funpay Bot
![Python](https://img.shields.io/badge/python-v3.11-blue)
![Docker](https://img.shields.io/badge/docker-latest-blue)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2F4erdenko%2FFunPayVertex-mod%2Fbadge%3Fref%3Dmain&style=flat)](https://actions-badge.atrox.dev/4erdenko/FunPayVertex-mod/goto?ref=main)  
This repository is a fork of the [FunPayVertex](https://github.com/NightStrang6r/FunPayVertex) project and contains the code for the Funpay Bot, a Telegram bot built with Python.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage locally](#usage-locally)
5. [Deployment](#deployment)
6. [Custom Changes](#custom-changes)
7. [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose
- Python 3.11

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Navigate to the project root directory, and install the necessary Python dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. To create your `_main.cfg` configuration file, run the bot locally using `python main.py`. This step will generate the `_main.cfg` file which includes all your bot settings. It is crucial for the operation of your bot. Remember to include the correct token for your Telegram bot in this configuration file. Also, note that according to Funpay rules, you may need to periodically update your `golden_key`.  

4. Once you have your environment set up and the necessary configuration file, use the following command to start the bot:

    ```bash
    python main.py
    ```

5. After your `_main.cfg` is set up correctly, it can be used to set up your Github secrets for CI/CD.

### Usage locally

You can use Docker Compose to run your bot. To install Docker, please follow the instructions for your specific operating system:

- [Install Docker on Windows](https://docs.docker.com/desktop/windows/install/)
- [Install Docker on Mac](https://docs.docker.com/desktop/mac/install/)
- [Install Docker on Linux](https://docs.docker.com/engine/install/)

Ensure that your `_main.cfg` is placed in the `/configs/` directory. Then, you can use the following command to run your bot with Docker Compose:

```bash
docker compose up -d
```

## Deployment

This application uses CI/CD with Github Actions. To deploy this on a live system, you will need to have a server running Docker and Docker Compose.

Set the following secrets in your Github repository:
   - `DOCKERHUB_USERNAME`: Your Dockerhub username.
   - `DOCKERHUB_PASSWORD`: Your Dockerhub password.
   - `HOST`: Your host for SSH connections.
   - `USER`: Your SSH username.
   - `SSH_KEY`: Your private SSH key.
   - `SSH_PASSPHRASE`: The passphrase for your SSH key.
   - `PROJECT_PATH_ON_HOST`: The project path on your host.
   - `_MAIN_CFG`: Your bot configuration, found in the `_main.cfg` file.

These secrets will be used in the Github Actions CI/CD pipeline to automate the process of testing, building, and deploying your bot.

## Custom Changes
Code refactoring a little bit, closely to PEP8.
This fork includes a special feature in the `handlers.py` file. Specifically, within the `deliver_goods` function (line 682), the `else` block includes the following code:

```python
lot_number = c.AD_CFG.sections().index(cfg_obj.name)
lot = c.AD_CFG.sections()[lot_number]
c.AD_CFG.remove_section(lot)
c.save_config(c.AD

_CFG, 'configs/auto_delivery.cfg')
logger.info(f'Lot {lot} has been removed from auto delivery configuration.')
```

This code automatically removes a lot from the auto delivery configuration file and deletes the bot's record of the lot.

## Contributing

Any contributions you make are greatly appreciated. Please fork the project, make your changes, and open a Pull Request if your updates are ready for submission.

Remember to maintain the forked repository by periodically pulling from the original repository if you're planning on making additional updates or improvements to the bot.
