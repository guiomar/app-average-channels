<h1 align="center">Average channels</h1>

<p align="center">
  Averages the power spectral density over a user-given list of MEG/EEG channels from a PSD table and outputs the averaged spectrum and a plot.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.599"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.599-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Averages the power spectral density over a user-given list of MEG/EEG channels from a PSD table and outputs the averaged spectrum and a plot.**

Reads the channel-by-frequency PSD TSV, selects the channels in channel_list, averages them into one new channel and plots the mean PSD with its standard deviation band. Use it to summarise the spectrum of a region (for example occipital gradiometers) after computing a PSD. Channel names must match the PSD table exactly.

| | |
|---|---|
| **Inputs** | `neuro/meeg/psd` |
| **Outputs** | `neuro/meeg/psd` · `generic/image/png` |
| **Container** | `brainlife/mne:0.23dev` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.599](https://doi.org/10.25663/brainlife.app.599) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `psd01` | `neuro/meeg/psd` | yes | Power spectral density table (TSV, channels by frequencies). |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/psd` | PSD table containing the averaged channel. |
| `out_figs` | `generic/image/png` | Plot of the averaged PSD with its standard deviation (avg_channels.png). |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `channel_list` | string |  | List of channels to average. Example: # Elekta Gradiometers MEG2042, MEG2043, MEG1913, MEG1912, MEG2113, MEG2112, MEG1922, MEG1923, MEG1942, MEG1943, MEG1642, MEG1643, MEG1933, MEG1932, MEG1733, MEG1732, MEG1723, MEG1722, MEG2143, MEG2142, MEG1742, MEG1743, MEG1712, MEG1713, MEG2032, MEG2033, MEG2313, MEG2312, MEG2342, MEG2343, MEG2322, MEG2323, MEG2433, MEG2432, MEG2122, MEG2123, MEG2333, MEG2332, MEG2513, MEG2512, MEG2523, MEG2522, MEG2133, MEG2132, MEG2542, MEG2543, MEG2532, MEG2533 # Elekta Magnetometers MEG2041, MEG1911, MEG2111, MEG1921, MEG1941, MEG1641, MEG1931, MEG1731, MEG1721, MEG2141, MEG1741, MEG1711, MEG2031, MEG2311, MEG2341, MEG2321, MEG2431, MEG2121, MEG2331, MEG2511, MEG2521, MEG2131, MEG2541, MEG2531 |
| `new_name` | string | `avg_occipital` | Name given to the new averaged channel. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.599](https://doi.org/10.25663/brainlife.app.599), choose `neuro/meeg/psd` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/psd`, `generic/image/png`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:0.23dev`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "psd": "/path/to/psd01/psd",
       "channel_list": "",
       "new_name": "avg_occipital"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Average channels. brainlife.io App. [doi:10.25663/brainlife.app.599](https://doi.org/10.25663/brainlife.app.599)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7(267):1-13 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Guiomar Niso, Instituto Cajal, CSIC, Spain

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
