<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/drobb2020/django-example">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Django Example - Using Django-Extensions</h3>

  <p align="center">
    This project was setup to explore django-extensions and lear more about what it can do for me during development.
    <br />
    <a href="https://github.com/drobb2020/django-example"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/drobb2020/django-example">View Demo</a>
    ·
    <a href="https://github.com/drobb2020/django-example/issues">Report Bug</a>
    ·
    <a href="https://github.com/drobb2020/django-example/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project was setup to explore django-extensions and lear more about what it can do for me during development.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Django 4.0.1](https://www.djangoproject.com/)
* [Django Extensions 3.1.5](https://django-extensions.readthedocs.io/en/latest/)
* [Graphviz 0.19.1](https://graphviz.org/)
* See requirements.txt for a full list

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

You will require graphviz to be installed on your OS before you can use graphviz with Django. Graphviz is available for Windows, MacOS, and Linux distros. Please see the graphviz website for details.

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/drobb2020/django-example.git
   ```

2. Create a virtual environment within the project folder.

   ```sh
   Python3 -m virtualenv venv
   ```

3. Activate the virtual environment.

   ```sh
   source /venv/bin/activate
   ```

4. Run pip install.

   ```sh
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Django extensions is a very useful tool to enhance your experience with django development. From shell_plus, to runserver_plus there are a host of utilities for everyone. I created a simple blog application and created a couple of models to experiment with the command extensions.
Here is the results from running the graph_models command:

<a href="https://github.com/drobb2020/django-example">
<img src="images/blog.png" alt="Logo" height="300">
  </a>

My favorite django-extensions are:

* shell_plus
* dumpscript
* export_emails
* generate_password
* Graph models
* reset_db
* runserver_plus
* generate_secret_key

_For more examples, please refer to the [Documentation](https://django-extensions.readthedocs.io/en/latest/command_extensions.html)_

<p align="right">(<a href="#top">back to top</a>)</p>

## Details on the Command Extensions

### shell_plus

* A Django shell with auto-loading of the configured apps database models and subclasses of user-defined classes.
* You can also exclude models by adding the --dont-load app1 to the command line.
* Has a built-in collision resolver.

### dumpscript

* Generates a standalone python script that can be used to repopulate the database using objects.
* Save crucial data when you modify your models.
* Edit the script to create 1000's of entries using for loops, and generated names.

### export_emails

* Exports the email addresses of registered users in the format you specify.
* formats are:
  * address
  * google
  * outlook
  * linkedin
  * vcard
* You can use the generated list for a mailer to all your users.

### generate_password

* Generates a new password that you can then use for a user password.
* Uses the default django password generator.
* You are able to specify the length of the password by adding the --length=XX switch.

### Graph models

* Renders a graphical representation of your entire project or of a specific application.
* You need Graphvis installed on the OS, as well as pygraphviz for this to work.
* Use the GRAPH_MODELS option in settings.py to specify default options.

### reset_db

* Fully resets your current database by running a DROP DATABASE followed by a CREATE DATABASE
* This is a destructive operation!
* You will be prompted to confirm the operation.

### runserver_plus

* This is the typical runserver command with the Werkzeug debugger baked in.
* Requires the Werkzeug package to be installed (Kick ass debugger).
* Allows you to run your development server over https by specifying the --cert-file option.

### generate_secret_key

* Creates a new secret key that you can put in your settings.py module, or more appropriately place it in a dot env file.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

* [X] Document the django-extensions I played with
* [X] Add full CRUD functionality to demonstration
* [ ] Add htmx to project
* [ ] Add a CustomUser app to the project and setup login, logout, and register pages.

See the [open issues](https://github.com/drobb2020/django-example/issues) for a list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

David Robb - [@davidrobb2](https://twitter.com/davidrobb2) - drobb2011@gmail.com

Project Link: [https://github.com/drobb2020/django-example](https://github.com/drobb2020/django-example)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [BugBytes](https://www.youtube.com/channel/UCTwxaBjziKfy6y_uWu30orA)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/drobb2020/django-example.svg?style=for-the-badge
[contributors-url]: https://github.com/drobb2020/django-example/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/drobb2020/django-example.svg?style=for-the-badge
[forks-url]: https://github.com/drobb2020/django-example/network/members
[stars-shield]: https://img.shields.io/github/stars/drobb2020/django-example.svg?style=for-the-badge
[stars-url]: https://github.com/drobb2020/django-example/stargazers
[issues-shield]: https://img.shields.io/github/issues/drobb2020/django-example.svg?style=for-the-badge
[issues-url]: https://github.com/drobb2020/django-example/issues
[license-shield]: https://img.shields.io/github/license/drobb2020/django-example.svg?style=for-the-badge
[license-url]: https://github.com/drobb2020/django-example/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/drobb2020
