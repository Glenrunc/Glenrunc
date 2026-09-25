<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img alt="Glenrunc — building systems that read, see and reason" src="assets/hero-dark.svg" width="100%">
</picture>

<br>

<a href="https://github.com/Glenrunc?tab=followers">
  <img alt="Followers" src="https://img.shields.io/github/followers/Glenrunc?style=flat-square&labelColor=0D1117&color=7C5CFF&logo=github&logoColor=white&label=followers"></a>
<a href="https://github.com/Glenrunc?tab=repositories">
  <img alt="Stars" src="https://img.shields.io/github/stars/Glenrunc?style=flat-square&labelColor=0D1117&color=FF4D8D&logo=github&logoColor=white&label=stars"></a>
<img alt="Location" src="https://img.shields.io/badge/Qu%C3%A9bec-Canada-22D3EE?style=flat-square&labelColor=0D1117&logo=googlemaps&logoColor=white">
<img alt="Schools" src="https://img.shields.io/badge/UTBM%20%C2%B7%20AGH%20%C2%B7%20UQAC-computer%20science%20%26%20AI-A78BFA?style=flat-square&labelColor=0D1117">
<img alt="Focus" src="https://img.shields.io/badge/focus-deep%20learning%20%2F%20from%20scratch-F59E0B?style=flat-square&labelColor=0D1117">

</div>

<br>

> *I like the layer underneath.*
> The compiler, not the language. The convolution, not the `import`. The retrieval, not the prompt.
> Most of what is here was written to find out how the thing actually works — and a few of them
> turned into something worth shipping.

<br>

## <samp>$ whoami --verbose</samp>

```console
name        Mattéo  ·  @Glenrunc
role        computer science student, currently majoring in artificial intelligence
path        UTBM (France)  →  AGH Kraków (Poland)  →  UQAC (Québec, Canada)
learned     deep learning & image processing during the Kraków semester — never left
principle   local-first: if it needs an API key to think, it is not mine
building    document intelligence, retrieval pipelines, and neural nets with no imports
```

<table>
<tr>
<td width="33%" valign="top">

**🧭 Working on**

Local, private document
intelligence — OCR, field
extraction and Q&A that never
leaves the machine.

</td>
<td width="33%" valign="top">

**🔬 Learning**

Transformer internals, the
honest way: re-deriving the
attention block instead of
calling it.

</td>
<td width="33%" valign="top">

**🤝 Open to**

AI / ML internships,
research-flavoured work, and
anything involving GPUs and
bad ideas taken seriously.

</td>
</tr>
</table>

<br>

## <samp>$ ls ./featured</samp>

<table>
<tr>

<td width="50%" valign="top">

### 🧠 [Slopformer](https://github.com/Glenrunc/slopformer)

> *“An Image is Worth 16×16 Brainrots”*

A research paper that is a joke and an implementation that is not. A ViT with three real
architectural modifications, a full LaTeX paper, and a test suite that actually passes —
built to understand vision transformers by breaking one on purpose.

`PyTorch` · `LaTeX` · `pytest`

<img alt="" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
<img alt="" src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white">
<img alt="" src="https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white">

</td>

<td width="50%" valign="top">

### 📄 [DocuFlow AI](https://github.com/Glenrunc/DocuflowAI)

> *Administrative documents, understood offline.*

OCR with **docTR**, extraction and natural-language Q&A with a **local LLM** via Ollama.
A durable job queue serialises the GPU, field schemas live once and are consumed by both
Pydantic and TypeScript, and every bounding box traces back to a real word.

`FastAPI` · `docTR` · `Ollama` · `Postgres` · `React`

<img alt="" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
<img alt="" src="https://img.shields.io/badge/Postgres-4169E1?style=flat-square&logo=postgresql&logoColor=white">
<img alt="" src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB">

</td>

</tr>
<tr>

<td width="50%" valign="top">

### 🔎 [Chatbot UQAC](https://github.com/Glenrunc/Chatbot_UQAC)

> *RAG over a 400-page institutional manual.*

Retrieval-augmented answering on UQAC's management handbook: `bge-m3` embeddings, a
MultiBERT cross-encoder for reranking, `qwen3:8b` for generation — the whole stack running
on a laptop, served through Streamlit.

`RAG` · `Ollama` · `Streamlit` · `reranking`

<img alt="" src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white">
<img alt="" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
<img alt="" src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white">

</td>

<td width="50%" valign="top">

### ⚙️ [CNN from scratch](https://github.com/Glenrunc/CNN_from_scratch)

> *No libraries. No AI assistant. No excuses.*

A convolutional neural network in raw C++ — tensors, convolutions, backpropagation and the
optimiser, all hand-written. The rule taped to the repo: use a library once and the whole
point is gone.

`C++` · `autograd` · `linear algebra`

<img alt="" src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white">
<img alt="" src="https://img.shields.io/badge/zero%20dependencies-2E7D32?style=flat-square">
<img alt="" src="https://img.shields.io/badge/from%20scratch-7C5CFF?style=flat-square">

</td>

</tr>
</table>

<details>
<summary><b>&nbsp;📦&nbsp; The rest of the shelf</b> &nbsp;<sub>(compilers, search, IoT, genetics and one social network)</sub></summary>

<br>

| Project | What it is | Stack |
| :--- | :--- | :--- |
| **[Hack-Compiler-Suite](https://github.com/Glenrunc/Hack-Compiler-Suite)** | Assembler and VM translator for the Hack architecture — the road from symbolic code to machine words, built by hand | `C++` |
| **[Rasende Roboter](https://github.com/Glenrunc/Rasende_Roboter)** | Search algorithms solving the Ricochet Robots board — BFS, heuristics, and a lot of pruning | `Python` |
| **[MI7 · segmentation & deepfake](https://github.com/Glenrunc/MI7_seg_impaint_deepfake)** | Detecting, erasing and re-synthesising humans in video streams | `PyTorch` `Jupyter` |
| **[HUMAN-RECOGNITION](https://github.com/Glenrunc/HUMAN-RECOGNITION)** | Fundamental algorithms for human recognition in images | `Python` `OpenCV` |
| **[ConwayGame](https://github.com/Glenrunc/ConwayGame)** | Conway's Game of Life, in C, because everyone should write it once | `C` |
| **[Genetic algorithm](https://github.com/Glenrunc/Genetic-algorithm-first-approach-)** | A first, deliberate approach to evolutionary optimisation | `C` |
| **[Aquaponics IoT](https://github.com/Glenrunc/Aquaponic-project-IoT-Simulation)** | Simulation of a sensor-driven aquaponics system | `C++` `IoT` |
| **[TheSocialNetwork](https://github.com/Glenrunc/TheSocialNetwork)** | A full social platform, back when PHP and MySQL were the whole world | `PHP` `MySQL` |

</details>

<br>

## <samp>$ cat ./toolbox</samp>

<table>
<tr><td><b>&nbsp;Languages&nbsp;</b></td><td>

<img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
<img alt="C++" src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white">
<img alt="C" src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black">
<img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white">
<img alt="Java" src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white">
<img alt="PHP" src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white">
<img alt="SQL" src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white">
<img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white">

</td></tr>
<tr><td><b>&nbsp;AI / ML&nbsp;</b></td><td>

<img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white">
<img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white">
<img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white">
<img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white">
<img alt="Ollama" src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white">
<img alt="LangChain" src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white">
<img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black">

</td></tr>
<tr><td><b>&nbsp;Backend&nbsp;</b></td><td>

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
<img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white">
<img alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white">
<img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
<img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">

</td></tr>
<tr><td><b>&nbsp;Frontend&nbsp;</b></td><td>

<img alt="React" src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB">
<img alt="Vite" src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white">
<img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black">
<img alt="CSS" src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white">

</td></tr>
<tr><td><b>&nbsp;Tooling&nbsp;</b></td><td>

<img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
<img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white">
<img alt="GitHub Actions" src="https://img.shields.io/badge/Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white">
<img alt="Neovim" src="https://img.shields.io/badge/Neovim-57A143?style=flat-square&logo=neovim&logoColor=white">
<img alt="CMake" src="https://img.shields.io/badge/CMake-064F8C?style=flat-square&logo=cmake&logoColor=white">

</td></tr>
</table>

<br>

## <samp>$ git log --stat</samp>

<div align="center">

<!--
  These two cards are generated by scripts/gen_cards.py and refreshed daily by
  .github/workflows/cards.yml — no third-party service, no broken images.
-->

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/stats-light.svg">
  <img alt="GitHub statistics" src="assets/stats-dark.svg" width="100%">
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/heatmap-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/heatmap-light.svg">
  <img alt="Contribution calendar" src="assets/heatmap-dark.svg" width="100%">
</picture>

</div>

<br>

## <samp>$ ping</samp>

<div align="center">

<a href="https://github.com/Glenrunc">
  <img alt="GitHub" src="https://img.shields.io/badge/GitHub-@Glenrunc-0D1117?style=for-the-badge&logo=github&logoColor=white"></a>
<!-- TODO: drop your real LinkedIn URL in here (or delete this badge). -->
<a href="https://www.linkedin.com/in/">
  <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://github.com/Glenrunc?tab=repositories">
  <img alt="Repositories" src="https://img.shields.io/badge/Projects-browse-7C5CFF?style=for-the-badge&logo=archiveofourown&logoColor=white"></a>

</div>

<br>

---

<div align="center">

<sub><i>Built from scratch, on purpose. — <b>@Glenrunc</b></i></sub>

<br><br>

<details>
<summary><sub>⚠️&nbsp; do not open this</sub></summary>
<br>
<img src="rick.gif" width="320" alt="you knew exactly what this was">
<br><br>
<sub><i>the only dependency I will never remove.</i></sub>
</details>

</div>
