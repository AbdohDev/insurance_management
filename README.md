# Employee Insurance Management Odoo Module

## Introduction

The Insurance Management module is designed for managing employee insurance policies, claims, and reports within the Odoo ecosystem. This project serves as a tool to streamline administrative tasks related to insurance while ensuring accurate tracking and reporting. This module is currently a work in progress and is not intended for commercial use.

## Features
+ **Policy Management**: Create, update, and manage employee insurance policies with ease.
+ **Claims Management**: File and process claims, and track their statuses.
+ **Reporting**: Generate detailed reports to analyze policy and claim data.
+ **User Role Management**: Assign roles and permissions to control access.
+ **Integration**: Seamless integration with Odoo's existing modules for enhanced functionality.

## Tools
+ **Platform**: Odoo framework for building the module.
+ **Database**: PostgreSQL (integrated with Odoo for data storage and management).
+ **Language**: Python for backend development, XML for interface customization.
+ **Frontend**: Odoo's built-in web client for user interactions.

## Getting Started

### Prerequisites
+ [Odoo 14+](https://www.odoo.com/)
+ [Python 3.7+](https://www.python.org/downloads/)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/abdohdev/insurance_management.git

2. Copy the module to your Odoo addons directory:
cp -r insurance_management /path/to/odoo/addons/

3. Refresh the list of available modules in Odoo:
    + Log in to your Odoo backend.
    + Navigate to the "Apps" section and select "Update Apps List."

4. Search for "Insurance Management" in the Apps menu and install the module.

## Running the Module
1. Start your Odoo instance:
./odoo-bin -c /path/to/your/odoo.conf

2. Log in to your Odoo dashboard and navigate to the "Insurance Management" menu to start using the module.
