# InstagramToMealie

A simple little converter, that imports an instagram URL into mealie

<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">INSTAGRAM TO MEALIE</h1></p>

<p align="center">
	<img src="https://img.shields.io/github/license/JoTec2002/InstagramToMealie?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/JoTec2002/InstagramToMealie?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/JoTec2002/InstagramToMealie?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/JoTec2002/InstagramToMealie?style=default&color=0080ff" alt="repo-language-count">
</p>
<br>

## Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Getting Started](#-getting-started)
    - [ Prerequisites](#-prerequisites)
    - [ Installation](#-installation)
    - [ Usage](#-usage)
    - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

## Overview

With InstagramToMealie, you can simply input an Instagram post URL. The project seamlessly integrates with Mealie API to
create a new recipe with associated image or video assets.


---

## Getting Started

### Prerequisites

1. Make Sure you have OpenAI/ Ollama configured in Mealie. This Project doesn't integrate directly with OpenAI/ Ollama,
   but need it to be configured in Mealie to work Properly. I personally got the best results with `qwen2.5:7b` as the
   Ollama Model.
2. Generate a Mealie API Key. [Mealie Docs](https://docs.mealie.io/documentation/getting-started/api-usage/)
3. Generate a Instagram Session File (!thats the most tricky step). A Helper Script is
   provided https://github.com/JoTec2002/InstagramToMealie/blob/main/helpers/instaloader_login_helper.py ! It's just
   copied from the [Instaloader Docs](https://instaloader.github.io/troubleshooting.html).

### Installation

Install InstagramToMealie using one of the following methods:

**Build from source:**
<details closed>

1. Clone the InstagramToMealie repository:

```sh
❯ git clone https://github.com/JoTec2002/InstagramToMealie
```

2. Navigate to the project directory:

```sh
❯ cd InstagramToMealie
```

3. Install the project dependencies:

</details>

**Use the Provided Docker Image: https://hub.docker.com/repository/docker/jotec2002/instagramtomealie/general**

### Usage

Deploy it via docker-compose allongside your mealie installation

Docker compose example:

```yaml
services:
  mealie:
    image: ghcr.io/mealie-recipes/mealie:v2.1.0
    container_name: mealie
    #Look up in the Mealie Docs for how to use Mealie
  InstagramToMealie:
    image: jotec2002/instagramtomealie
    expose:
      - "9001"
    environment:
      INSTA_USER: "instagram username"
      MEALIE_API_KEY: "MEALIE API KEY"
      MEALIE_URL: "YOU LOCAL MEALIE INSTALLATION"
    volumes:
      - "./session-file:/app/session-file"        #The instagram session file you created in the prerequisits
    depends_on:
      mealie:
        condition: service_healthy
```

---

## Contributing

- **💬 [Join the Discussions](https://github.com/JoTec2002/InstagramToMealie/discussions)**: Share your insights, provide
  feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/JoTec2002/InstagramToMealie/issues)**: Submit bugs found or log feature
  requests for the `InstagramToMealie` project.
- **💡 [Submit Pull Requests](https://github.com/JoTec2002/InstagramToMealie/blob/main/CONTRIBUTING.md)**: Review open
  PRs, and submit your own PRs.

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/JoTec2002/InstagramToMealie/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=JoTec2002/InstagramToMealie">
   </a>
</p>
</details>

---

## License

This project is protected under the MIT License. For more details,
refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- [Mealie](https://github.com/mealie-recipes/mealie/)
- [Instadownloader](https://github.com/instaloader/instaloader)

---
