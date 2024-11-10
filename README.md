# ComfyUI Production Nodes Pack

<img src="https://img.shields.io/badge/ComfyUI-0.2.6+-green" /> <img src="https://img.shields.io/badge/Custom-Nodes-blue" /> <img src="https://img.shields.io/badge/NAI-00-ffae00" />
```py
VERSION: Pre-Alpha Release: 0.1 - Licensed under GNU General Public License V3
NOTE: This project is supported by our community > linkedin.com/groups/13109092/
USER: https://github.com/KoreTeknology
```

## !!! WORK IN PROGRESS !!! (Stay tuned)

This is set of custom nodes for your ComfyUI[^1] production setup. It offers the very basic nodes that are missing in the official "Vanilla" package.
It is a research Node based project on *Artificial Intelligence* using ComfyUI visual editor. This repository also includes a set of workflows to test the nodes.

<img alt="essential Nodes Pack NODES" src="/media/screenshot_CENP_nodes.png">

## 🛡️ Custom Nodes

Here is an overview of the nodes available in this first version of the pack. These correspond to those that I use every day, during my work or in my classes. Others will follow when they are tested and validated. I was inspired by many other developers to create these nodes, even if I had to rewrite most of the scripts myself, for the sake of consistency and integration into comfyUI.

### Image Transform

<table>
<tr><th align="left", width="250">Nodes</th><th align="left", width="432">Values</th><th align="left", width="200">State</th></tr>
<tr><td><a href="/">Image Flip</a></td><td align="left">x / y / xy</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Image Rotate</a></td><td align="left">Degree /Step: 1)</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Image Concatenate</a></td><td align="left">Inputs number, Direction, Match size</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Image Extend</a></td><td align="left">Left, Right, Top, bottom, BG White %</td><td align="left">✔️</td></tr>
</table>

### Image Postprocessing

<table>
<tr><th align="left", width="250">Nodes</th><th align="left", width="432">Values</th><th align="left", width="200">State</th></tr>
<tr><td><a href="/">Image Brigthness</a></td><td align="left">0.0>5.0 / Step: 0.1</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Image Contrast</a></td><td align="left">0.0>5.0 / Step: 0.1</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Image Greyscale</a></td><td align="left">No value</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Image RGB</a></td><td align="left">Red,Green, Blue (0-255 /Step: 1)</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Image Difference</a></td><td align="left">2 input images, no value</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Apply Color Palette</a></td><td align="left">2 input images, intensity, lightness</td><td align="left">⚠️</td></tr>
<tr><td><a href="/">Extract Color Palette</a></td><td align="left">number of colors, line/square</td><td align="left">⚠️</td></tr>
</table>

### Image Compositing

<table>
<tr><th align="left", width="250">Nodes</th><th align="left", width="432">Values</th><th align="left", width="200">State</th></tr>
<tr><td><a href="/">Add Image Layer</a></td><td align="left">2 input images, x, y, alpha (RGBA)</td><td align="left">⚠️</td></tr>
<tr><td><a href="/">Add Text Layer</a></td><td align="left">String, x, y, width, color</td><td align="left">⚠️</td></tr>
</table>

Some extra nodes we need sometimes:

<table>
<tr><th align="left", width="250">Nodes</th><th align="left", width="432">Values</th><th align="left", width="200">State</th></tr>
<tr><td><a href="/">Set Text</a></td><td align="left">String</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Get Text</a></td><td align="left">String</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Note Advanced</a></td><td align="left">String, String</td><td align="left">✔️</td></tr>
<tr><td><a href="/">Math Operation</a></td><td align="left">a, b, Mode, Type</td><td align="left">✔️</td></tr>
</table>

## 🛡️ Menu Items

One of the principles of creating this node pack is to integrate the node names into the menu, in existing categories, rather than creating a new category. It is quite annoying to have to search for nodes when each developer creates a root category, which makes the menu almost unusable.

<img alt="essential Nodes Pack MENUS" src="/media/screenshot_CENP_menu.png">

## 🛡️ Settings

One of the next planned update is to add a dedicated panel into comfyUI settings window to activate/desactivate each node from the pack. 

> [!IMPORTANT]
> User may use these settings if he wants tu use an alternative node from his installed ones. this avoid getting to much "doubles" into the main node menu.

---

## 🛡️ ComfyUI Installation and Custom Nodes

After installing [**ComfyUI**](https://github.com/comfyanonymous/ComfyUI) services with your prefered plateform (i am suggesting the use of [**Stability Matrix**](https://github.com/LykosAI/StabilityMatrix) as it is easy to install and give a lot of controls), make sure you install the additional and necessary custom nodes. Then you need to install [GIT software](https://git-scm.com/) (if it is not done already) on your computer. To install these custom nodes, open a CMD window in the \ComfyUI\custom_nodes folder. And "git clone" the Compositing Pack. Or you can use the integrated manager:

- [ComfyUi-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

> [!TIP]
> If you have already ComfyUI installed and working, you can simply copy and paste the **Compositing nodes Pack** into the custom nodes folder. Enjoy!

---

## 🛡️ Development Plan

I'm currently working on a series of new nodes that will be added progressively to this pack. These are mainly oriented towards compositing and post-processing, using either the PIL library or OpenCV.
If you want to follow the progress or/and participate, I invite you to connect with me on [LINKEDIN](https://www.linkedin.com/in/urieldeveaud/) and [ComfyUI For AI Media Production](https://www.linkedin.com/groups/13109092/), a group of users passionate about AI.

### PRIORITY LEVEL
* Config JS extension panel (activate/desactivate individual nodes
* Property panel with description, tips,etc...
* Help options 
* refactoring for 1.2 release

Follow the development: [Here](DEV.md)

---
## 🛡️ Infos

* Author: **Uriel Deveaud** [NAI-00] - [Kore Teknology](https://github.com/KoreTeknology)
* Partners: **Techman Studio MX** - [techmanstudio.com](https://techmanstudio.com.mx/)
* License: This project is released under the Apache 2.0 License.
* This work is dedicated to all ComfyUI users and to all our students ;)

[^1]: **ComfyUI** is the free and open source AI creation suite. Please, visit [ComfyUI Github page](https://github.com/comfyanonymous/ComfyUI) for more infos.
