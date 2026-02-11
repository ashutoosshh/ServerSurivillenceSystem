This project is a Python-based system monitoring automation tool designed to collect real-time system information, generate structured log files, and send those logs via email as attachments at regular time intervals. The script monitors key system metrics such as CPU usage, RAM usage, disk utilization, network statistics, and running process details using the psutil library.

The application works by generating a timestamp-based log file inside a specified directory. Each log contains detailed system performance data and process-level information, making it useful for performance tracking, diagnostics, and automated reporting. The generated log file is then securely attached to an email and sent using Gmail’s SMTP server.

The script supports command-line arguments, allowing the user to specify the time interval (in minutes) and the directory name for storing log files. Once executed, the automation runs continuously at the defined interval until manually stopped. The project also demonstrates safe multithreading usage for handling log generation without blocking execution flow.

Email credentials are handled securely using environment variables instead of hard-coded passwords, ensuring better security practices. The project structure is simple and modular, making it easy to extend with additional features such as threshold-based alerts, log compression, or deployment as a background service.

This project demonstrates practical implementation of Python automation concepts, including system monitoring, file handling, SMTP-based email automation, multithreading, and structured logging. It serves as a strong example of real-world automation scripting and can be extended further for production-level monitoring systems.

The reposotory contains 2 files in which The Log File contains The information That has to bee upload on Mail and the Surviellince system contains the actual code.

There is another File name RoughMail.py that contains A simple draft for mail Automation.
