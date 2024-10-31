# ComfyUI Compositing Nodes Pack

<img src="https://img.shields.io/badge/ComfyUI-0.2.6+-green" /> <img src="https://img.shields.io/badge/Custom-Nodes-blue" /> <img src="https://img.shields.io/badge/NAI-00-ffae00" />
```py
VERSION: Pre-Alpha Release: 0.0.1 - Licensed under Apache License v2.0
```
### A set of custom nodes that everyone needs!

This is set of custom nodes for your ComfyUI[^1] local installation. It offers the very basic nodes that are missing in the official "Vanilla" package.
It is a research Node based project on *Artificial Intelligence* using ComfyUI visual editor. This repository also includes a set of workflows to test the nodes.

<img alt="essential Nodes Pack NODES" src="/media/screenshot_CENP_nodes.png">

## 🛡️ Custom Nodes

Here is an overview of the nodes available in this first version of the pack. These correspond to those that I use every day, during my work or in my classes. Others will follow when they are tested and validated. I was inspired by many other developers to create these nodes, even if I had to rewrite most of the scripts myself, for the sake of consistency and integration into comfyUI.

- **Image Brigthness** &nbsp;&nbsp; Value: 0.0>5.0 
- **Image Contrast** &nbsp;&nbsp; Value: 0.0>5.0
- **Image Greyscale** &nbsp;&nbsp; No Value
- **Image RGB** &nbsp;&nbsp; Values: Red,Green, Blue (0-255)
- **Image Flip** &nbsp;&nbsp; Values: x/y/xy
- **Image Rotate** &nbsp;&nbsp; Value: Degree

Some extra nodes we need sometimes:
- **Get Text** &nbsp;&nbsp; Value: String
- **Set Text** &nbsp;&nbsp; Value: String
- **Note Advanced** &nbsp;&nbsp; Values: String, String
- **Math Operation** &nbsp;&nbsp; Values: a, b, Mode, Type

## 🛡️ Menu Items

One of the principles of creating this node pack is to integrate the node names into the menu, in existing categories, rather than creating a new category. It is quite annoying to have to search for nodes when each developer creates a root category, which makes the menu almost unusable.

<img alt="essential Nodes Pack MENUS" src="/media/screenshot_CENP_menu.png">


---

## 🛡️ ComfyUI Installation and Custom Nodes

After installing [**ComfyUI**](https://github.com/comfyanonymous/ComfyUI) services with your prefered plateform (i am suggesting the use of [**Stability Matrix**](https://github.com/LykosAI/StabilityMatrix) as it is easy to install and give a lot of controls), make sure you install the additional and necessary custom nodes. Then you need to install [GIT software](https://git-scm.com/) (if it is not done already) on your computer. To install these custom nodes, open a CMD window in the \ComfyUI\custom_nodes folder. And "git clone" the Essential Pack. Or you can use the integrated manager:

- [ComfyUi-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

If you have already ComfyUI installed and working, you can simply copy and paste the **Essential nodes Pack** into the custom nodes folder. Enjoy!

---

## 🛡️ Development Plan

I'm currently working on a series of new nodes that will be added progressively to this pack. These are mainly oriented towards compositing and post-processing, using either the PIL library or OpenCV.
If you want to follow the progress or/and participate, I invite you to connect with me on [LINKEDIN](https://www.linkedin.com/in/urieldeveaud/) and [ComfyUI For AI Media Production](https://www.linkedin.com/groups/13109092/), a group of users passionate about AI.

---
## 🛡️ Infos

* Author: **Uriel Deveaud** - [Kore Teknology](https://github.com/KoreTeknology) 
* License: This project is released under the Apache 2.0 License.
* This work is dedicated to all ComfyUI users and to all our students ;)

[^1]: **ComfyUI** is the free and open source AI creation suite. Please, visit [ComfyUI Github page](https://github.com/comfyanonymous/ComfyUI) for more infos.
