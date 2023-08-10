# Mitigating Vulnerabilities in LLMs

This project contains examples and guidelines to mitigate vulnerabilities like Prompt Injection and Denial of Service (DoS) in systems utilizing Large Language Models (LLMs). The repository is divided into sections to demonstrate insecure and secure coding practices.

## Structure

- `01-prompt-injection`: Contains examples related to prompt injection vulnerabilities.
- `02-denial-of-service`: This directory includes both insecure and secure examples to mitigate DoS attacks.
  - `base`: Demonstrates an insecure implementation.
    - `insecure_example_openai.py`: An insecure example code that could be prone to DoS attacks.
    - `requirements.txt`: Required libraries and dependencies.
  - `harden-openai`: Contains examples to demonstrate the mitigation strategies.
    - `01-secure_Rate_limit_content_length_openai.py`: Implements rate limiting by content length.
    - `02-secure_adaptive_rate_limit_openai.py`: Implements adaptive rate limiting.
    - `03-secure_auth_and_monitor_openai.py`: Implements secure authentication and monitoring.
    - `requirements.txt`: Required libraries and dependencies for the hardened examples.

## Getting Started

### Prerequisites

- Python 3.6 or above
- Follow the `requirements.txt` file in each directory for specific dependencies.

### Installation

1. Clone the repository: git clone https://github.com/mantiumai/llm-security-examples.git
2. Navigate to the desired directory (e.g., `02-denial-of-service/base` or `02-denial-of-service/harden-openai`).
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

Navigate to the specific directory and run the Python file you want to execute: `python insecure_example_openai.py`


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the terms specified in the `LICENSE` file.

## Acknowledgments

- OpenAI for providing the models and guidelines.
- Community contributors and maintainers.