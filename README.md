# Average channels

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Averages the power spectral density over a user-given list of MEG/EEG channels from a PSD table and outputs the averaged spectrum and a plot.**

Reads the channel-by-frequency PSD TSV, selects the channels in channel_list, averages them into one new channel and plots the mean PSD with its standard deviation band. Use it to summarise the spectrum of a region (for example occipital gradiometers) after computing a PSD. Channel names must match the PSD table exactly.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/psd` |
| 📤 **Outputs** | `neuro/meeg/psd` · `generic/image/png` |
| 🐳 **Container** | `brainlife/mne:0.23dev` |
| ⚙️ **Resources** | 8 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.599](https://doi.org/10.25663/brainlife.app.599) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `psd01` | `neuro/meeg/psd` | yes | Power spectral density table (TSV, channels by frequencies). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/psd` | PSD table containing the averaged channel. |
| `out_figs` | `generic/image/png` | Plot of the averaged PSD with its standard deviation (avg_channels.png). |

<details>
<summary><b>⚙️ Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `channel_list` | string |  | List of channels to average. Example: # Elekta Gradiometers MEG2042, MEG2043, MEG1913, MEG1912, MEG2113, MEG2112, MEG1922, MEG1923, MEG1942, MEG1943, MEG1642, MEG1643, MEG1933, MEG1932, MEG1733, MEG1732, MEG1723, MEG1722, MEG2143, MEG2142, MEG1742, MEG1743, MEG1712, MEG1713, MEG2032, MEG2033, MEG2313, MEG2312, MEG2342, MEG2343, MEG2322, MEG2323, MEG2433, MEG2432, MEG2122, MEG2123, MEG2333, MEG2332, MEG2513, MEG2512, MEG2523, MEG2522, MEG2133, MEG2132, MEG2542, MEG2543, MEG2532, MEG2533 # Elekta Magnetometers MEG2041, MEG1911, MEG2111, MEG1921, MEG1941, MEG1641, MEG1931, MEG1731, MEG1721, MEG2141, MEG1741, MEG1711, MEG2031, MEG2311, MEG2341, MEG2321, MEG2431, MEG2121, MEG2331, MEG2511, MEG2521, MEG2131, MEG2541, MEG2531 |
| `new_name` | string | `avg_occipital` | Name given to the new averaged channel. |

</details>

📚 **References used by this App:**
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809-813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7(267):1-13 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.599-blue.svg)](https://doi.org/10.25663/brainlife.app.599)


## Documentation
Brainlife App to average channels from psd tsv files 


## Authors
- [Guiomar Niso](guiomar.niso@ctb.upm.es), Instituto Cajal, CSIC, Spain

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this app. 

1. **brainlife. io: A decentralized and open source cloud platform to support neuroscience research**. Hayashi, S., Caron, B. A., et al. & Pestilli, F. (2023). ArXiv. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10274934/

2. **MEG and EEG data analysis with MNE-Python**. Gramfort A, et al. & Hämäläinen MS. (2013). Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University
